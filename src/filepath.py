import os
import xml.etree.ElementTree as etree
projectpath = '{}/project_PE2A1'.format(os.path.dirname(os.getcwd()))
datpath ='{}/dat'.format(projectpath)                                           # dat폴더의 경로입니다.
filepath=[]
for (root, directories, files) in os.walk(datpath):       # 분석해야하는 모든 파일의 경로를 알아냅니다.
    for file in files:
        if '.xml' in file:                                # xml파일만 골라냅니다.
            file_path = os.path.join(root, file)
            filepath.append(file_path)

xml = etree.parse(filepath[0])
root = xml.getroot()
filename=os.path.basename(filepath[0])