import numpy as np
from sklearn.metrics import r2_score
import warnings

warnings.simplefilter('ignore', np.RankWarning)

# 결정계수 구하기
def ILR(x, y, deg):
    coeffs = np.polyfit(x, y, deg)
    # r-squared
    p = np.poly1d(coeffs)
    yhat = p(x)
    ybar = np.sum(y) / len(y)           # or sum(y)/len(y) 평균값
    ssreg = np.sum((yhat - ybar) ** 2)  # or sum([ (yihat - ybar)**2 for yihat in yhat]) 실제값과 예측값 사이
    sstot = np.sum((y - ybar) ** 2)     # or sum([ (yi - ybar)**2 for yi in y]) 실제값과 평균값 사이
    results = ssreg / sstot
    return results

def ILfitting(L, IL):
    #Rref = np.poly(L[-1], IL[-1], 6)     # 6차 결정계수
    fit_L = np.polyfit(L[-1], IL[-1], 6)  # IL fitting
    fit_IL = np.polyval(fit_L, L[-1])
    Rref=r2_score(IL[-1],fit_IL)
    return Rref, fit_IL
