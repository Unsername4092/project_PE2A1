from src.parse import xmlparse
from src.IV import *
from src.IL import *
from src.plot import *
from src.savefig import *
from src.save_csv import *
from src.makefolder import *
import glob2
import os
import xml.etree.ElementTree as etree

def filename(filenamelist):
    file_name = []
    path = './dat/**/*LMZ*.xml'
    file_name_list = glob2.glob(path)
    filepath=[]
    for f in range(len(file_name_list)):
        file_basename = os.path.basename(file_name_list[f])
        file_name.append(file_basename)
        filesplit = file_basename.split('_')
        filefind=[]
        for fsp in range(len(filesplit)):
            if filenamelist[fsp] == []:
                filefind.append(filesplit[fsp])
            else:
                for nl in range(len(filenamelist[fsp])):
                    if filenamelist[fsp][nl] in filesplit[fsp]:
                        filefind.append(filesplit[fsp])
        if len(filefind)==6:
            filepath.append(file_name_list[f])
    filenamebase=[]
    for j in range(len(file_name)):
        base_name = os.path.basename(file_name[j])
        filenamebase.append(base_name.replace('.xml',''))
    root = []
    for k in filepath:
        xml = etree.parse(k)
        root.append(xml.getroot())
    return root, filenamebase