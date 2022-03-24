import csv 
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt 

plt.style.use('ggplot')

with open('data.csv') as csv_file:
  csv_reader = csv.DictReader(csv_file)

  language_counter = Counter()

  for row in csv_reader:
    language_counter.update(row['LanguagesWorkedWith'].split(';'))

print(language_counter)


# ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# x_indexes = np.arange(len(ages_x))
# width= .25

# dev_y = [38496, 42000, 46752, 49320, 53200,
#          56000, 62316, 64928, 67317, 68748, 73752]     

# plt.bar(x_indexes - width, dev_y, width=width, color='#444444', linestyle='--', label='All Devs')

# py_dev_y = [45372, 48876, 53850, 57287, 63016,
#             65998, 70003, 70000, 71496, 75370, 83640]
# plt.bar(x_indexes, py_dev_y, width=width, linewidth=3, label='Python')

# js_dev_y = [37810, 43515, 46823, 49293, 53437,
#             56373, 62375, 66674, 68745, 68746, 74583]

# plt.bar(x_indexes + width, js_dev_y, width=width, linewidth=3, label='Javascript')

# plt.xlabel('Ages')
# plt.ylabel('Median Salary (USD)')
# plt.title('Median Salary by Age')

# plt.legend()
# plt.xticks(ticks=x_indexes, labels=ages_x)
# plt.tight_layout()
# plt.show()