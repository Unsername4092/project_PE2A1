import matplotlib.pyplot as plt
import numpy as np
from numpy import exp
from lmfit import Model
import statsmodels.api as sm
from src.parse import *

plt.figure(1, [18, 8])
plt.subplot(2, 3, 4)
plt.plot(V, I, 'b.', label='data')
plt.yscale('log')
plt.title('I-V analysis')
plt.xlabel('Voltage[V]')
plt.ylabel('Current[A]')
plt.legend(loc='best')

def fitting(V, I):
    x = np.array(V[:])
    y = np.array(I[:])
    fit1 = np.polyfit(x, y, 12)
    fit1 = np.poly1d(fit1)

    def IV_fit(X, Is, Vt):
        return (Is * (exp(X / Vt) - 1) + fit1(X))

    model = Model(IV_fit)
    result = model.fit(I, X=V, Is=10 ** -15, Vt=0.026)

    initial_list = []
    for i in V:
        x_value = IV_fit(i, 10e-16, 0.026)
        initial_list.append(x_value)

    initial = sm.add_constant(np.abs(y))
    result1 = sm.OLS(initial_list, initial).fit()
    return y,result

# R-squared
def IVR(y, result):
    yhat = result.best_fit
    ybar = np.sum(y) / len(y)
    sse = np.sum((yhat - ybar) ** 2)
    sst = np.sum((y - ybar) ** 2)
    return sse / sst

    # plt.plot(x, result.best_fit, label='best_fit')
    # plt.plot(x, result.best_fit, 'r-', label='R-squared ={}'.format(IVR(y)))
    # plt.legend(loc='best')