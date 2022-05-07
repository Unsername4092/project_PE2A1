import os
import xml.etree.ElementTree as etree

projectpath = '{}/project_PE2A1'.format(os.path.dirname(os.getcwd()))
datpath ='{}/dat'.format(projectpath)                                           # dat폴더의 경로입니다.
filepath=[]
filename=[]
for (root, directories, files) in os.walk(datpath):       # 분석해야하는 모든 파일의 경로를 알아냅니다.
    for file in files:
        if '.xml' in file:                                # xml파일만 골라냅니다.
            file_path = os.path.join(root, file)
            filepath.append(file_path)
            file_name=os.path.basename(file_path)
            filename.append(file_name.replace('.xml',''))
print('존재하는 데이터파일 리스트입니다.')
for i in range(len(filepath)):
    print('[{}]'.format(i+1),filename[i])
global index
enter='임시문자열'
while enter!='exit' :
    enter = input('파일 검색을 원하시면 1, 번호를 입력하시려면 2를 입력해주세요. \n : ')
    if enter == '1':
        search = input('검색어를 입력해주세요. 입력한 문자열을 포함하는 데이터나 해당 번호의 파일 보여줍니다.\n : ')
        number = 0
        for i in range(len(filename)) :
            if search == str(i+1):
                print('[{}]'.format(i+1),filename[i])
                number=number+1
            elif search in filename[i] :
                print('[{}]'.format(i+1),filename[i])
                number=number+1
        if number==0 :
            print('검색결과가 존재하지 않습니다.')
    elif enter == '2':
        index = input('번호를 입력해주세요. \n : ')
        if index not in list(map(str,range(1,len(filename)+1))) :
            print('자연수가 아니거나 해당 번호가 존재하지 않습니다.')
        else:
            print('결과를 출력합니다.')
            break
    elif enter!='exit':
        print('잘못된 입력입니다.')
    else:
        print('프로그램을 종료합니다.')
        exit()
xml = etree.parse(filepath[int(index)-1])
root = xml.getroot()
filename=filename[int(index)-1]
