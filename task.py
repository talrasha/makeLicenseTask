import os
import pandas as pd
import numpy as np
import random
import subprocess
import psutil

global installPythonPackage
# with MAC
subprocess.call(['pip3', 'install', 'pandas'])
subprocess.call(['pip3', 'install', 'numpy'])
subprocess.call(['pip3', 'install', 'psutil'])

# with windows
#installPythonPackage = ['pip3 install pandas numpy psutil']
#os.system('start cmd /k ' + installPythonPackage[0])

desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',25)



def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process

    # With MAC
    process = subprocess.Popen('pgrep '+processName, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    my_pid, err = process.communicate()
    if my_pid:
        return True
    else:
        return False
    # Up till here is fo mac

    # This is for windows
    #for proc in psutil.process_iter():
    #    try:
    #        # Check if process name contains the given name string.
    #        if processName.lower() in proc.name().lower():
    #            return True
    #    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
    #        pass
    #return False
    # UP till here is for windows

############### Get 'howmany' random files ###############
############### Save a randomFiles.txt file ###############
############### Save a empty results.csv file ###############

def getRandomFileList(howmany):
    with open('filelist.txt', 'r', encoding='utf-8') as txtfile:
        filelist = [x.strip('\n') for x in txtfile.readlines()]
    randomlist = random.sample(range(0, 380953), howmany)
    with open('randomFiles.txt', 'a', encoding='utf-8') as txtfile:
        for number in randomlist:
            txtfile.write(filelist[number]+'\n')
    atempdict = {}
    atempdict['file'] = [filelist[x] for x in randomlist]
    atempdict['license'] = ['']*howmany
    df = pd.DataFrame.from_dict(atempdict)
    df.to_csv('results.csv', index=False)

############### Start work with the unfinished business ###############

def startworking():
    # with MAC
    subprocess.call(['open', '-a', 'Microsoft Excel', 'results.csv'])
    # with windows
    #os.system("start excel.exe " + 'results.csv')
    df = pd.read_csv('results.csv')
    unfinished = df.loc[df['license'].isna(), 'file'].values.tolist()
    print("There are still "+str(len(unfinished))+" files to go! You are almost there!\n")
    running = 1
    for file in unfinished:
        running = 1
        print(file)
        print('\n')
        # with MAC
        subprocess.call(['open', '-a', 'TextEdit', file])
        # with windows
        # os.system("notepad.exe " + file)
        while running:
            running = checkIfProcessRunning('TextEdit')

        #break

startworking()