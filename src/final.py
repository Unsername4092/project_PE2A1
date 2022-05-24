from src.filename import *
import time

def run(lot_id, wafer_id, row_column_id, maskset_id, testsite_id):
    start=time.time()
    filenamelist=[lot_id, wafer_id, row_column_id, maskset_id, ['DCM'], testsite_id]
    root, filenamebase, file_path = filename(filenamelist)
    savefig,showfig = fig_input()
    I, V, L, IL, DCBias=xmlparse(root)
    pathlist=create_folder(file_path)
    for r in range(len(root)):
        Varray, Iarray, result = IVfitting(V[r], I[r])
        IV_R = IVR(Iarray, result)
        IVplot(V[r], I[r], Varray, IV_R, result, r+1)                   # IVplot(V_list,I_list,V_array,IV_Rsq,lmfit.result,figure_num)
        IL_R, fit_IL = ILfitting(L[r], IL[r])
        ILplot(L[r], IL[r], DCBias[r], fit_IL, IL_R, r+1)               # ILplot(L_list,IL_list,DCBias_list,reference_fitting,Rsq,figure_num)
        save_fig(plt.figure(r+1), filenamebase[r], savefig, showfig, pathlist[r])
        data_dict(root[r], V[r], I[r], fit_IL, IV_R, IL_R)              # data_dict(root,I_list,V_l)
    save_csv(dict,'result')
    print(time.time()-start)