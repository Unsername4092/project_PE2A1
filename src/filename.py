import glob2
import os
import xml.etree.ElementTree as etree

def filename(filenamelist):
    file_name = []
    file_path = []
    path = './dat/**/*LMZ*.xml'
    file_name_list = glob2.glob(path)
    for f in range(len(file_name_list)):
        file_basename = os.path.basename(file_name_list[f])   # file_basename: HY202103_D07_(-1,-1)_LION1_DCM_LMZC.xml
        file_name.append(file_basename)                       # file_name: file_basename list
        file_split = file_basename.split('_')                 # file_split: HY202103, D07, (-1,-1), LION1, DCM, LMZC.xml
        file_find = []                                        # file_find: find correct file name list
        for fsp in range(len(file_split)):
            if filenamelist[fsp] == []:
                file_find.append(file_split[fsp])
            else:
                for nl in range(len(filenamelist[fsp])):
                    if filenamelist[fsp][nl] in file_split[fsp]:
                        file_find.append(file_split[fsp])
        if len(file_find) == 6:
            file_path.append(file_name_list[f])
    filenamebase = []
    for j in range(len(file_name)):
        filenamebase.append(file_name[j].replace('.xml', ''))  # file_namebase: HY202103_D07_(-1,-1)_LION1_DCM_LMZC
    root = []
    for k in file_path:
        xml = etree.parse(k)
        root.append(xml.getroot())
    return root, filenamebase, file_path