from src.final import *
import time
start = time.time() # start time

'''원하는 lot을 입력하시오'''
lot_id = ['HY202103']

'''원하는 wafer를 입력하시오'''
wafer_id = ['D07']

'''원하는 (row,column)를 입력하시오'''
row_column_id = []

'''원하는 Maskset을 입력하시오'''
maskset_id = ['LION1']

'''원하는 testsite를 입력하시오'''
testsite_id = ['LMZ']

run(lot_id, wafer_id, row_column_id, maskset_id, testsite_id)
print("time :", round(time.time()-start, 1), 's')  # now - start time = run time