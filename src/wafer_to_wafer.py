import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('../res/csv/result.csv')
wafernumber = data['Wafer']
spec = data['Rsq of Ref. spectrum (6th)']
one_V = data['I at 1V[A]']
minone_V = data['I at -1V[A]']

plt.figure(figsize=(16, 10))
plt.suptitle('Result of wafer-to-wafer using csv file', fontsize=20)
for i in range(len(wafernumber)):
    plt.subplot(1, 3, 1)
    if str(wafernumber[i]) == 'D07':
        plt.scatter(wafernumber[i], spec[i], c='red')
    elif str(wafernumber[i]) == 'D08':
        plt.scatter(wafernumber[i], spec[i], c='blue')
    elif str(wafernumber[i]) == 'D23':
        plt.scatter(wafernumber[i], spec[i], c='green')
    elif str(wafernumber[i]) == 'D24':
        plt.scatter(wafernumber[i], spec[i], c='purple')

for i in range(len(wafernumber)):
    plt.subplot(1, 3, 2)
    if str(wafernumber[i]) == 'D07':
        plt.scatter(wafernumber[i], one_V[i], c='red')
    elif str(wafernumber[i]) == 'D08':
        plt.scatter(wafernumber[i], one_V[i], c='blue')
    elif str(wafernumber[i]) == 'D23':
        plt.scatter(wafernumber[i], one_V[i], c='green')
    elif str(wafernumber[i]) == 'D24':
        plt.scatter(wafernumber[i], one_V[i], c='purple')

for i in range(len(wafernumber)):
    plt.subplot(1, 3, 3)
    if str(wafernumber[i]) == 'D07':
        plt.scatter(wafernumber[i], minone_V[i], c='red')
    elif str(wafernumber[i]) == 'D08':
        plt.scatter(wafernumber[i], minone_V[i], c='blue')
    elif str(wafernumber[i]) == 'D23':
        plt.scatter(wafernumber[i], minone_V[i], c='green')
    elif str(wafernumber[i]) == 'D24':
        plt.scatter(wafernumber[i], minone_V[i], c='purple')

plt.show()