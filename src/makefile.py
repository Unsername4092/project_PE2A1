import os
#import importlib

# csv
from src.filepath import filename
from src.save_csv import frame

os.makedirs('../res/csv', exist_ok=True)
frame.to_csv('../res/csv/{}.csv'.format(filename),index=False)

# fig
from src.IL import fig
os.makedirs('../res/fig', exist_ok=True)
fig.savefig('../res/{}.png'.format(filename))





