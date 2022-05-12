from src.input import root, filenamebase

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
        Ifloat = list(map(float, i.text.split(',')))
        I.append(list(map(abs, Ifloat)))
    # I-L graph
    LL = []
    ILL = []
    DCL = []
    for i in r.iter('WavelengthSweep'):  # L과 IL, DC bias 데이터 수집
        LT=list(map(float, i[0].text.split(',')))
        ILT=list(map(float, i[1].text.split(',')))
        LL.append(LT)
        ILL.append(ILT)
        DCL.append('DC = {}'.format(i.attrib['DCBias']))
    for l in range(len(LL)):                              # IL[-1]과 L의 리스트길이가 다를때, 같게 만들어줍니다.
        if len(LL[l])>len(ILL[-1]) :
            for m in range(len(LL[l])-len(ILL[-1])):
                del LL[l][-1]
                del ILL[l][-1]
        elif len(LL[l])<len(ILL[-1]) :
            for m in range(len(ILL[-1])-len(LL[l])):
                del ILL[l][-1]


    DCL[-1] = 'Reference'
    L.append(LL)
    IL.append(ILL)
    DCBias.append(DCL)



