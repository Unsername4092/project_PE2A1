import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('../res/csv/result.csv')
wafernumber = data['Wafer']
wafer = list(set(data['Wafer']))
spec = data['Rsq of Ref. spectrum (6th)']
one_V = data['I at 1V[A]']
minone_V = data['I at -1V[A]']

fig = plt.figure(figsize=(16, 10))
ax1=fig.add_subplot(2,3,1)
ax2=fig.add_subplot(2,3,2)
ax3=fig.add_subplot(2,3,3)
ax4=fig.add_subplot(2,3,4)
ax5=fig.add_subplot(2,3,5)
ax6=fig.add_subplot(2,3,6)
plt.suptitle('Result of wafer-to-wafer using csv file', fontsize=20)

ax1.set_xlabel('Wafer')
ax1.set_ylabel('Max transmission Ref.spec.(dB)')

ax2.set_xlabel('Wafer')
ax2.set_ylabel('I at -1V')

ax3.set_xlabel('Wafer')
ax3.set_ylabel('I at 1V')

for i in range(len(wafernumber)):
    if str(wafernumber[i]) == 'D07':
        ax1.scatter(wafernumber[i], spec[i], c='red')
        ax2.scatter(wafernumber[i], one_V[i], c='red')
        ax3.scatter(wafernumber[i], minone_V[i], c='red')
    elif str(wafernumber[i]) == 'D08':
        ax1.scatter(wafernumber[i], spec[i], c='blue')
        ax2.scatter(wafernumber[i], one_V[i], c='blue')
        ax3.scatter(wafernumber[i], minone_V[i], c='blue')
    elif str(wafernumber[i]) == 'D23':
        ax1.scatter(wafernumber[i], spec[i], c='green')
        ax2.scatter(wafernumber[i], one_V[i], c='green')
        ax3.scatter(wafernumber[i], minone_V[i], c='green')
    elif str(wafernumber[i]) == 'D24':
        ax1.scatter(wafernumber[i], spec[i], c='purple')
        ax2.scatter(wafernumber[i], one_V[i], c='purple')
        ax3.scatter(wafernumber[i], minone_V[i], c='purple')

sns.boxplot(x='Wafer', y='Rsq of Ref. spectrum (6th)', data=data, palette='RdBu_r', ax=ax4)
sns.boxplot(x='Wafer', y='I at -1V[A]', data=data, palette='RdBu_r', ax=ax5)
sns.boxplot(x='Wafer', y='I at 1V[A]', data=data, palette='RdBu_r', ax=ax6)

plt.tight_layout()
plt.show()