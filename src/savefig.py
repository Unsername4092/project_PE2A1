import os


def save_fig(fig, filename):
    fig.suptitle(filename, fontsize=13, fontweight='bold')
    fig.set_size_inches((25, 17), forward=False)
    fig.savefig('{}/res/{}.png'.format(os.getcwd(), filename))



