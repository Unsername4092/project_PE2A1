import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('../res/csv/result.csv')
wafernumber = data['Wafer']
wafer = list(set(data['Wafer']))
spec = data['Rsq of Ref. spectrum (6th)']
one_V = data['I at 1V[A]']
minone_V = data['I at -1V[A]']

fig = plt.figure(figsize=(16, 10))
ax1 = fig.add_subplot(2, 3, 1)
ax2 = fig.add_subplot(2, 3, 2)
ax3 = fig.add_subplot(2, 3, 3)
ax4 = fig.add_subplot(2, 3, 4)
ax5 = fig.add_subplot(2, 3, 5)
ax6 = fig.add_subplot(2, 3, 6)
plt.suptitle('Result of wafer-to-wafer using csv file', fontsize=20)

# spec
spdt1=[]
spdt2=[]
spdt3=[]
spdt4=[]
#one_V
onedt1=[]
onedt2=[]
onedt3=[]
onedt4=[]
# minone_V
min1 = []
min2 = []
min3 = []
min4 = []

for i in range(len(wafernumber)):
    if str(wafernumber[i]) == 'D07':
        spdt1.append(spec[i])
        onedt1.append(one_V[i])
        min1.append(minone_V[i])
        ax1.scatter(wafernumber[i], spec[i], c='red')
        ax2.scatter(wafernumber[i], one_V[i], c='red')
        ax3.scatter(wafernumber[i], minone_V[i], c='red')
        # ax4.boxplot([spec])
    elif str(wafernumber[i]) == 'D08':
        spdt2.append(spec[i])
        onedt2.append(one_V[i])
        min2.append(minone_V[i])
        ax1.scatter(wafernumber[i], spec[i], c='blue')
        ax2.scatter(wafernumber[i], one_V[i], c='blue')
        ax3.scatter(wafernumber[i], minone_V[i], c='blue')
    elif str(wafernumber[i]) == 'D23':
        spdt3.append(spec[i])
        onedt3.append(one_V[i])
        min3.append(minone_V[i])
        ax1.scatter(wafernumber[i], spec[i], c='green')
        ax2.scatter(wafernumber[i], one_V[i], c='green')
        ax3.scatter(wafernumber[i], minone_V[i], c='green')
    elif str(wafernumber[i]) == 'D24':
        spdt4.append(spec[i])
        onedt4.append(one_V[i])
        min4.append(minone_V[i])
        ax1.scatter(wafernumber[i], spec[i], c='purple')
        ax2.scatter(wafernumber[i], one_V[i], c='purple')
        ax3.scatter(wafernumber[i], minone_V[i], c='purple')

ax4.boxplot([spdt1, spdt2, spdt3, spdt4],notch=0, sym='+')
ax4.set_xticklabels(wafer, fontsize=8)
ax5.boxplot([onedt1, onedt2, onedt3, onedt4],notch=0, sym='+')
ax5.set_xticklabels(wafer, fontsize=8)
ax6.boxplot([min1, min2, min3, min4] ,notch=0, sym='+')
ax6.set_xticklabels(wafer, fontsize=8)
    # if str(wafernumber[i]) == 'D07':
    #     plt.boxplot([spec])
    # elif str(wafernumber[i]) == 'D08':
    #     plt.boxplot([spec])
    # elif str(wafernumber[i]) == 'D23':
    #     plt.boxplot([spec])
    # elif str(wafernumber[i]) == 'D24':
    #     plt.boxplot([spec])
    # plt.boxplot([spec])
    # plt.subplot(2, 3, 5)
    # plt.boxplot([one_V])
    # plt.subplot(2, 3, 6)
    # plt.boxplot([minone_V])

plt.tight_layout()
plt.show()
