import matplotlib.pyplot as plt # graphing capabilities
import numpy as np              # function unique to summarize die rolls
import random                   # random number generation
import seaborn as sns           # graphing capabilities
from matplotlib.text import Text

rolls = [random.randrange(1, 7) for i in range(600)]

# return_counts=True: tells unique to count each unique val's number of occurrences.
# if it's set to False, only the list of unique vals is returned.
vals, freq = np.unique(rolls, return_counts = True)

title = f'Rolling a Six-Sided Die {len(rolls):,} Times' # Display number with thousands separators.
sns.set_style('whitegrid')
axes = sns.barplot(x=vals, y=freq, palette='bright')

axes.set_title(title)
# output: Text(0.5, 1, 'Rolling a Six-Sided Die 600 times')

axes.set(xlabel='Die Value',   ylabel='Frequency')
# output: [Text(92.6667,0.5,'Frequency'), Text(0.5,58.7667,'Die   Value')]

axes.set_ylim(top=max(freq) * 1.10)

for bar, frequency in zip(axes.patches, freq):
    text_x = bar.get_x() + bar.get_width() / 2.0  
    text_y = bar.get_height()
    text = f'{frequency:,}\n{frequency / len(rolls):.3%}'
    axes.text(text_x, text_y, text,
              fontsize=11,   ha='center', va='bottom')

# plt.cla() -- clear axes
plt.show()
