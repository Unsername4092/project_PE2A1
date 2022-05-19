from src.filename import *

'''원하는 lot을 입력하시오'''
lot_id = ['HY202103']

'''원하는 wafer를 입력하시오'''
wafer_id = ['D07', 'D08']

'''원하는 (row,column)를 입력하시오'''
row_column_id = ['(0,0)']

'''원하는 Maskset을 입력하시오'''
maskset_id = ['LION1']

'''원하는 testsite를 입력하시오'''
testsite_id = ['LMZ']

filenamelist=[lot_id,wafer_id,row_column_id,maskset_id,['DCM'],testsite_id]
root, filenamebase = filename(filenamelist)

savefig,showfig = fig_input()
I,V,L,IL,DCBias=xmlparse(root)
for r in range(len(root)):
    Varray, Iarray, result = IVfitting(V[r], I[r])
    IV_R = IVR(Iarray, result)
    IVplot(V[r], I[r], Varray, IV_R, result, r+1)        # IVplot(V_list,I_list,V_array,IV_Rsq,lmfit.result,figure_num)
    IL_R, fit_IL = ILfitting(L[r], IL[r])
    ILplot(L[r], IL[r], DCBias[r], fit_IL, IL_R, r+1)    # ILplot(L_list,IL_list,DCBias_list,reference_fitting,Rsq,figure_num)
    save_fig(plt.figure(r+1), filenamebase[r], savefig, showfig)
    data_dict(root[r], V[r], I[r], fit_IL, IV_R, IL_R)        # data_dict(root,I_list,V_l)
save_csv(dict,'data')