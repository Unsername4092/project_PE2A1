import numpy as np
from numpy import exp
from lmfit import Model
import statsmodels.api as sm


def IVfitting(V, I):
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
    return x, y, result


# R-squared
def IVR(y, result):
    yhat = result.best_fit
    ybar = np.sum(y) / len(y)
    sse = np.sum((yhat - ybar) ** 2)
    sst = np.sum((y - ybar) ** 2)
    return sse / sst