import os

import matplotlib.pyplot as plt


def save_fig(fig, filename):
    fig.suptitle(filename, fontsize=13, fontweight='bold')
    fig.set_size_inches((25, 17), forward=False)
    savefig = input('그래프 저장하시겠습니까? (TRUE =1 or FALSE =0) : ')
    if savefig == 1:
        fig.savefig('{}/res/{}.png'.format(os.getcwd(), filename))
    showfig = input('그래프 출력하시겠습니까? (TRUE =1 or FALSE =0) : ')
    if showfig == 1:
        plt.show(fig)
    elif showfig ==0:
        plt.close(fig)