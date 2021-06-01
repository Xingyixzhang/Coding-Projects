# plotly auto-scales visualization to fit viewer's screen. Interactive features provided.
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die = Die()

results = []
for roll_num in range(1000):
	result = die.roll()
	results.append(result)

frequencies = []
for value in range(1, die.num_sides + 1):
	frequency = results.count(value)
	frequencies.append(frequency)
print(frequencies)

x_values = list(range(1, die.num_sides + 1)) # plotly does not accept range() result, needs to convert to list explicitly.
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}

my_layout = Layout(title='Result of rolling one D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)

# generate the plot, needing a dict of data and layout obj.
offline.plot({'data': data, 'layout': my_layout}, filename='web_pages/one_d6.html')
