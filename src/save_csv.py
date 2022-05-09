import statsmodels.api as sm
from dateutil.parser import parse
import numpy as np
import pandas as pd
from filepath import root,projectpath,filename
from IV import V, x, y, IV_fit, result,IVR
from IL import L, IL, Rref

TestSiteInfo=root.find('TestSiteInfo')
dict = {'Lot':[],'Wafer':[],'Mask':[],'TestSite':[],'Name':[],'Date':[],'Operator':[],'DieRow':[],'DieColumn':[],'AnalysisWavelength (nm)':[],'Rsq of Ref. spectrum (6th)':[] ,'Max transmission of Ref. spec. (dB)':[], 'Rsq of IV':[], '1 at -1V[A]':[], '1 at 1V[A]':[]}
AlignWavelength = next(root.iter('AlignWavelength'))
Modulator = next(root.iter('Modulator'))

IVdic = {I: V for V, I in zip(result.best_fit, V)}

initial_list = []
for i in x:
    x_value = IV_fit(i, 10e-16, 0.026)
    initial_list.append(x_value)
initial = sm.add_constant(np.abs(y))
result1 = sm.OLS(initial_list, initial).fit()
Rsq = result1.rsquared


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
dict['Rsq of Ref. spectrum (6th)'].append(Rref)
dict['Max transmission of Ref. spec. (dB)'].append(max(IL[-1]))
dict['Rsq of IV'].append(IVR(y))
dict['1 at -1V[A]'].append(IVdic[-1.0])
dict['1 at 1V[A]'].append(IVdic[1.0])
frame = pd.DataFrame(dict)
frame.to_csv('{}/res/{}.csv'.format(projectpath,filename),index=False)