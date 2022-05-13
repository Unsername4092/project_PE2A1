from src.parse import *
from src.IV import *
from src.IL import *
from src.plot import *
from src.savefig import save_fig
from src.save_csv import *


for r in range(len(root)):          #range(1)을 range(len(root)) 로 바꾸기
    Varray, Iarray, result = IVfitting(V[r], I[r])
    IV_R = IVR(Iarray, result)
    IVplot(V[r], I[r], Varray, IV_R, result, r+1)        # IVplot(V_list,I_list,V_array,IV_Rsq,lmfit.result,figure_num)
    IL_R, fit_IL = ILfitting(L[r], IL[r])
    ILplot(L[r], IL[r], DCBias[r], fit_IL, IL_R, r+1)    # ILplot(L_list,IL_list,DCBias_list,reference_fitting,Rsq,figure_num)
    save_fig(plt.figure(r+1), filenamebase[r])
    plt.close(plt.figure(r+1))
    data_dict(root[r],V[r],I[r],fit_IL,IV_R,IL_R)        # data_dict(root,I_list,V_l)
save_csv(dict,'data')






