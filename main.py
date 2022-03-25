from matplotlib import pyplot as plt 

plt.style.use('ggplot')

slices = [60, 40]

plt.pie(slices)

plt.title('Pie Chart')
plt.tight_layout()
plt.show()
