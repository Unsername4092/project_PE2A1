import glob2
import os
import xml.etree.ElementTree as etree

location = int(input('data file이 project_PE2A1 폴더 안에 있나요? (TRUE = 1 or FALSE = 0) : '))
number_range = int(input('전체 xml 파일과 특정 xml 파일 중 선택하시오. (전체 = 1 or 특정 = 0) : '))

def filename():
    if location == 1:
        path = '../dat/**/*LMZ*.xml'
    elif location == 0:
        sub_path = input('data 경로를 입력하세요 : ')
        path = str(sub_path) + '/**/*LMZ*.xml'
        print('data location 외부 경로')
    if number_range == 1:
        file_name = glob2.glob(path)
    elif number_range == 0:
        lot_id = input('lot_id를 입력하시오.(전체 lot을 원할 경우 enter) : ')
        wafer_id = input('wafer_id를 입력하시오.(전체 wafer를 원할 경우 enter) : ')
        row_column_id = input('row,column을 입력하시오.(전체 row,column을 원할 경우 enter) : ')
        testsite_id = input('TestSite를 입력하시오.(전체 TestSite를 원할 경우 enter) : ')
        file_name_list = glob2.glob(path)
        file_name = []
        for i in range(len(file_name_list)):
            if lot_id in file_name_list[i]:
                if wafer_id in file_name_list[i]:
                    if row_column_id in file_name_list[i]:
                        if testsite_id in file_name_list[i]:
                            file_name.append(file_name_list[i])
        file_name_base = []
        for j in range(len(file_name)):
            base_name = os.path.basename(file_name[j])
            file_name_base.append(base_name.replace('.xml',''))
        # print(file_name_base)
        # print(file_name, '분석')
        return file_name, file_name_base
# filename()
a,b=filename()
# print(a)

root = []
for k in a:
    xml = etree.parse(k)
    root.append(xml.getroot())