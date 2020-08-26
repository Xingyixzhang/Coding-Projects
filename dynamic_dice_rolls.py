"""Dynamically graphing frequencies of die   rolls."""

from matplotlib import animation
import matplotlib.pyplot as plt # graphing capabilities
import random                   # random number generation
import seaborn as sns           # graphing capabilities
import sys

def update(frame_num, rolls, faces, freq):
    """Configures bar plot contents for each   animation frame."""
    for i in range(rolls):
        freq[random.randrange(1, 7) - 1] += 1
    
    # Reconfigure plot for updated die frequencies:
    plt.cla()
    axes = sns.barplot(faces, freq, palette='bright')
    axes.set_title(f'Die frequencies for {sum(freq):,} Rolls')
    axes.set(xlabel='Die Value', ylabel='Frequency')
    axes.set_ylim(top=max(freq) * 1.10)

    for bar, frequency in zip(axes.patches, freq):
        text_x = bar.get_x() + bar.get_width() / 2.0
        text_y = bar.get_height()
        text = f'{frequency:,}\n{frequency / sum(freq):.3%}'
        axes.text(text_x, text_y, text, ha='center', va='bottom')

# Read command-line arguments for number of frames and rolls per frame
number_of_frames = 50
rolls_per_frame = 500 
sns.set_style('whitegrid')  # white background with gray grid lines
figure = plt.figure('Rolling a Six-Sided Die')  # Figure for animation
values = list(range(1, 7))  # die faces for display on x-axis
freq = [0] * 6  # six-element list of die frequencies

# Configure and start animation that calls function update
die_animation = animation.FuncAnimation(
    figure, update, repeat=False, frames=number_of_frames, interval=33,
    fargs = (rolls_per_frame, values, freq))

plt.show()  # display window
