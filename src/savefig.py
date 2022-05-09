import matplotlib as plt
from src.filepath import projectpath, filename
from src import IV,IL
from src.IL import fig

fig.suptitle(filename, fontsize=13, fontweight='bold')
fig.set_size_inches((25, 17), forward=False)
fig.savefig('{}/res/{}.png'.format(projectpath,filename))
