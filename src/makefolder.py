import os

folder_path = './res'
if not os.path.isdir(folder_path):
    os.mkdir('./res/')

Lots_path = './res/Lots'
if not os.path.isdir(Lots_path):
    os.mkdir('./res/Lots/')

csv_path = './res/csv'
if not os.path.isdir(csv_path):
    os.mkdir('./res/csv/')