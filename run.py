# from src.parse import *
# from src.IV import *
# from src.IL import *
# from src.plot import *
# from src.savefig import save_fig
# from src.save_csv import *
import glob2
import os

#Input paramters
# 조건문

lot_id = ['HY202103']
wafer_id = []
row_column_id = ['0,0']
testsite_id = ['LMZ']
filenamelist=[lot_id,wafer_id,row_column_id,['LION1'],['DCM'],testsite_id]

# print(os.listdir('dat/D07/20190715_190855'))


file_name = []
path = './dat/**/*LMZ*.xml'
file_name_list = glob2.glob(path)
for f in range(len(file_name_list)):
    file_basename = os.path.basename(file_name_list[f])
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
        print(filefind)


'''for i in range(len(file_name_list)):
    for lot in lot_id:
        if lot in file_name_list[i]:
            for wafer in wafer_id:
                if wafer in file_name_list[i]:
                    for rowcolum in row_column_id:
                        if rowcolum in file_name_list[i]:
                            for testsite in testsite_id:
                                if testsite in file_name_list[i]:
                                    file_name.append(file_name_list[i])'''






# for r in range(len(root)):                               # range(1)을 range(len(root)) 로 바꾸기
#     Varray, Iarray, result = IVfitting(V[r], I[r])
#     IV_R = IVR(Iarray, result)
#     IVplot(V[r], I[r], Varray, IV_R, result, r+1)        # IVplot(V_list,I_list,V_array,IV_Rsq,lmfit.result,figure_num)
#     IL_R, fit_IL = ILfitting(L[r], IL[r])
#     ILplot(L[r], IL[r], DCBias[r], fit_IL, IL_R, r+1)    # ILplot(L_list,IL_list,DCBias_list,reference_fitting,Rsq,figure_num)
#     save_fig(plt.figure(r+1), filenamebase[r])
#     plt.close(plt.figure(r+1))
#     data_dict(root[r],V[r],I[r],fit_IL,IV_R,IL_R)        # data_dict(root,I_list,V_l)
# save_csv(dict,'data')






