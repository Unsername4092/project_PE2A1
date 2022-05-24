import statsmodels.api as sm
from dateutil.parser import parse
import numpy as np
import os
import pandas as pd

dict = {'Lot':[],'Wafer':[],'Mask':[],'TestSite':[],'Name':[],'Date':[],'Operator':[],'DieRow':[],'DieColumn':[], 'ErrorFlag':[], 'Error description':[], 'AnalysisWavelength (nm)':[],'Rsq of Ref. spectrum (6th)':[] ,'Max transmission of Ref. spec. (dB)':[], 'Rsq of IV':[], '1 at -1V[A]':[], '1 at 1V[A]':[]}

def data_dict(root, V, I, ref, IVRsq, ILRsq):
    AlignWavelength = next(root.iter('AlignWavelength'))
    Modulator = next(root.iter('Modulator'))
    TestSiteInfo = root.find('TestSiteInfo')
    times = root.attrib['CreationDate']
    times = parse(times).strftime('%Y%m%d_%H%M%S')
    if 0.99 >= ILRsq:
        ErrorFlage = '1'
        Error_description = 'Ref.spec.Error'
    else:
        ErrorFlage = '0'
        Error_description = 'No error'
    dict['Lot'].append(TestSiteInfo.attrib['Batch'])
    dict['Wafer'].append(TestSiteInfo.attrib['Wafer'])
    dict['Mask'].append(TestSiteInfo.attrib['Maskset'])
    dict['TestSite'].append(TestSiteInfo.attrib['TestSite'])
    dict['Name'].append(Modulator.attrib['Name'])
    dict['Date'].append(times)
    dict['Operator'].append(root.attrib['Operator'])
    dict['DieRow'].append(TestSiteInfo.attrib['DieRow'])
    dict['DieColumn'].append(TestSiteInfo.attrib['DieColumn'])
    dict['ErrorFlag'].append(ErrorFlage)
    dict['Error description'].append(Error_description)
    dict['AnalysisWavelength (nm)'].append(AlignWavelength.text)
    dict['Rsq of Ref. spectrum (6th)'].append(ILRsq)
    dict['Max transmission of Ref. spec. (dB)'].append(max(ref))
    dict['Rsq of IV'].append(IVRsq)
    dict['1 at -1V[A]'].append(I[V.index(-1.0)])
    dict['1 at 1V[A]'].append(I[V.index(1.0)])

def save_csv(dict_,filename):
    frame = pd.DataFrame(dict_)
    frame.to_csv('{}/res/csv/{}.csv'.format(os.getcwd(), filename), index=False)

