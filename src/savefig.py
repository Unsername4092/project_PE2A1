import os

import matplotlib.pyplot as plt

def fig_input():
    savefig = input('그래프 저장하시겠습니까? (TRUE =1 or FALSE =0) : ')
    showfig = input('그래프 출력하시겠습니까? (TRUE =1 or FALSE =0) : ')
    return savefig, showfig

def save_fig(fig, filename, savefig, showfig):
    fig.suptitle(filename, fontsize=13, fontweight='bold')
    fig.set_size_inches((25, 17), forward=False)
    if savefig == '1':
        fig.savefig('{}/res/{}.png'.format(os.getcwd(), filename))
    elif savefig != '0':
        print('잘못된 입력입니다.')
        exit()
    if showfig == '1':
        plt.show()
    elif showfig == '0':
        plt.close(fig)
    else:
        print('잘못된 입력입니다.')
        exit()