from src.input import root

V = []
I = []
L = []
IL = []
DCBias = []

for r in root:
    # I-V graph
    for v in r.iter('Voltage'):
        V.append(list(map(float, v.text.split(','))))
    for i in r.iter('Current'):
        I.append(list(map(float, i.text.split(','))))
        I = list(map(abs, I))

    # I-L graph
    LL=[]
    ILL=[]
    DCL=[]
    for i in r.iter('WavelengthSweep'):  # L과 IL, DC bias 데이터 수집
        LL.append(list(map(float, i[0].text.split(','))))
        ILL.append(list(map(float, i[1].text.split(','))))
        DCL.append('DC = {}'.format(i.attrib['DCBias']))
    DCL[-1] = 'Reference'
    L.append(LL)
    IL.append(ILL)
    DCBias.append(DCL)
