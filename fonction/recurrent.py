import os.path
from os import listdir

def get_wallets_name():
    path = os.path.join(os.getcwd(), "content\\wallets\\")
    files = []
    for i, file in enumerate(listdir(path)):
        if not os.path.isdir(path + "\\" + file):
            files.append(os.path.splitext(file)[0])
    return files

def get_blocks_hash():
    path = os.path.join(os.getcwd(), "content\\blocs\\")
    files = []
    for i, file in enumerate(listdir(path)):
        if not os.path.isdir(path + "\\" + file) and file != "00.json":
            files.append(os.path.splitext(file)[0])
    return files