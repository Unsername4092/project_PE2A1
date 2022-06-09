from src.final import *
import time
start = time.time() # start time

'''Enter the desired lot'''
lot_id = ['HY202103']

'''Enter the desired wafer'''
wafer_id = []

'''Enter the desired (row,column)'''
row_column_id = []

'''Enter the desired Maskset'''
maskset_id = ['LION1']

'''Enter the desired testsite'''
testsite_id = ['LMZ']

run(lot_id, wafer_id, row_column_id, maskset_id, testsite_id)
print("time :", round(time.time()-start, 1), 's')  # now - start time = run time