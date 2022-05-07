import matplotlib as plt
from filepath import projectpath, filename
import IV,IL
from IL import fig

fig.suptitle(filename, fontsize=13, fontweight='bold')
fig.set_size_inches((25, 17), forward=False)
fig.savefig('{}/res/{}.png'.format(projectpath,filename))

