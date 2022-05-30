import matplotlib.pyplot as plt

def IVplot(V, I, x, R, result, figure):
    plt.figure(figure,[18,8])
    plt.subplot(2, 3, 4)
    plt.plot(V, I, 'b.')
    plt.yscale('log')
    plt.title('I-V analysis')
    plt.xlabel('Voltage[V]')
    plt.ylabel('Current[A]')
    plt.plot(x, result.best_fit, label='best_fit')
    plt.plot(x, result.best_fit, 'r-', label='R-squared ={}'.format(R))
    plt.legend(loc='best')

def ILplot(L, IL, DCBias, fit_IL, Rref, figure):
    plt.figure(figure,[18,8])
    for i in range(1, 4):  # 그래프 그리기
        plt.subplot(2, 3, i)
        plt.xlabel('Wavelength[nm]', fontsize=10)
        plt.ylabel('Transmission[dB]', fontsize=10)
        plt.title('Transmission spectra as measured', fontsize=12, fontweight='bold')
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
        plt.legend(loc='best', ncol=2, fontsize=8)
    plt.tight_layout()