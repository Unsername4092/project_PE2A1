import os
from src.filename import *

def make_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('ERROR')

def create_folder(file_path):
    for i in range(len(list(set(file_path)))):
        split = file_path[i].split('/')
        path = split[-1].split('\\')
        make_folder('./res/Lots/{}/{}/'.format(path[-3], path[-2]))
        make_folder('./res/csv/')