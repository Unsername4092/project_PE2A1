import matplotlib.pyplot as plt
import numpy as np
from filepath import root
L = []
IL = []
DCBias = []
for i in root.iter('WavelengthSweep'):  # L과 IL, DC bias 데이터 수집
    L.append(list(map(float, i[0].text.split(','))))
    IL.append(list(map(float, i[1].text.split(','))))
    DCBias.append('DC = {}'.format(i.attrib['DCBias']))
DCBias[-1] = 'Reference'


def poly(x, y, deg):  # 결정계수 구하기
    coeffs = np.polyfit(x, y, deg)
    # r-squared
    p = np.poly1d(coeffs)
    yhat = p(x)
    ybar = np.sum(y) / len(y)           # or sum(y)/len(y) 평균값
    ssreg = np.sum((yhat - ybar) ** 2)  # or sum([ (yihat - ybar)**2 for yihat in yhat]) 실제값과 예측값 사이
    sstot = np.sum((y - ybar) ** 2)     # or sum([ (yi - ybar)**2 for yi in y]) 실제값과 평균값 사이
    results = ssreg / sstot
    return results


Rref = poly(L[-1], IL[-1], 6)         # 6차 결정계수
fit_L = np.polyfit(L[-1], IL[-1], 6)  # IL fitting
fit_IL = np.polyval(fit_L, L[-1])

for i in range(1, 4):  # 그래프 그리기
    plt.subplot(2, 3, i)
    if i == 1:  # raw data
        for r in range(len(L)):
            plt.plot(L[r], IL[r], label=DCBias[r])
    if i == 2:  # reference fitting
        plt.plot(L[-1], IL[-1], 'r', label='reference')
        plt.plot(L[-1], fit_IL, 'c-', label='{0}th Rsqure={1}'.format(6, Rref))
        plt.ylim(-60, -5)
    if i == 3:  # raw data - reference fitting
        for j in range(len(L)):
            plt.plot(L[j], IL[j] - fit_IL, label=DCBias[j])
plt.xlabel('Wavelength[nm]', fontsize=10)
plt.ylabel('Transmission[dB]', fontsize=10)
plt.title('Transmission spectra as measured', fontsize=12, fontweight='bold')
plt.legend(loc='best', ncol=2, fontsize=8)
plt.tight_layout()
fig=plt.figure(1)
fig.show()
