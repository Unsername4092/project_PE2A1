import statsmodels.api as sm
from dateutil.parser import parse
import numpy as np
import os
import pandas as pd

dict = {'Lot':[],'Wafer':[],'Mask':[],'TestSite':[],'Name':[],'Date':[],'Operator':[],'DieRow':[],'DieColumn':[],'AnalysisWavelength (nm)':[],'Rsq of Ref. spectrum (6th)':[] ,'Max transmission of Ref. spec. (dB)':[], 'Rsq of IV':[], '1 at -1V[A]':[], '1 at 1V[A]':[]}


def data_dict(root,I,V,ref,IVRsq,ILRsq):
    AlignWavelength = next(root.iter('AlignWavelength'))
    Modulator = next(root.iter('Modulator'))
    TestSiteInfo = root.find('TestSiteInfo')
    times = root.attrib['CreationDate']
    times = parse(times).strftime('%Y%m%d_%H%M%S')
    dict['Lot'].append(TestSiteInfo.attrib['Batch'])
    dict['Wafer'].append(TestSiteInfo.attrib['Wafer'])
    dict['Mask'].append(TestSiteInfo.attrib['Maskset'])
    dict['TestSite'].append(TestSiteInfo.attrib['TestSite'])
    dict['Name'].append(Modulator.attrib['Name'])
    dict['Date'].append(times)
    dict['Operator'].append(root.attrib['Operator'])
    dict['DieRow'].append(TestSiteInfo.attrib['DieRow'])
    dict['DieColumn'].append(TestSiteInfo.attrib['DieColumn'])
    dict['AnalysisWavelength (nm)'].append(AlignWavelength.text)
    dict['Rsq of Ref. spectrum (6th)'].append(ILRsq)
    dict['Max transmission of Ref. spec. (dB)'].append(max(ref))
    dict['Rsq of IV'].append(IVRsq)
    dict['1 at -1V[A]'].append(I[V.index(-1.0)])
    dict['1 at 1V[A]'].append(I[V.index(1.0)])

def save_csv(dict_,filename):
    frame = pd.DataFrame(dict_)
    frame.to_csv('{}/res/{}.csv'.format(os.getcwd(), filename), index=False)






'''IVdic = {I: V for V, I in zip(result.best_fit, V)}

initial_list = []
for i in x:
    x_value = IV_fit(i, 10e-16, 0.026)
    initial_list.append(x_value)
initial = sm.add_constant(np.abs(y))
result1 = sm.OLS(initial_list, initial).fit()
Rsq = result1.rsquared
print(Rsq)'''
