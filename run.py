import glob2

location = int(input('data file이 project_PE2A1 파일 안에 있나요? (TRUE = 1 or FALSE = 0) : '))
number_range = int(input('전체 xml 파일과 특정 xml 파일 중 선택하시오. (전체 = 1 or 특정 = 0) : '))

if location == 1:
    path = './dat/**/*LMZ*.xml'
elif location == 0:
    sub_path = input('data 경로를 입력하세요 : ')
    path = str(sub_path) + '**/*LMZ*.xml'
    print('data location 외부경로')

if number_range == 1:
    file_name = glob2.glob(path)
elif number_range == 0:
    lot_id = input('lot_id를 입력하시오(모든 lot_id를 원할 시 enter) : ')
    wafer_id = input('wafer_id를 입력하시오(모든 wafer_if를 원할 시 enter) : ')
    row_column_id = input('row,column을 입력하시오(모든 row,column을 원할 시 enter) : ')
    file_name_list = glob2.glob(path)

    file_name = []
    for i in range(0, len(file_name_list)):
        if wafer_id in file_name_list[i]:
            if row_column_id in file_name_list[i]:
                file_name.append(file_name_list[i])
    print(file_name, '분석')
