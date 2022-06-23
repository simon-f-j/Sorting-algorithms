#%%
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('./csv_files/heap_bubble_random_1000.csv')

algorithm = 'heap'
algorithm_2 = 'bubble'


algorithm_time = df[f' {algorithm}_time']
algorithm_n = df[f'   n']

algorithm2_time = df[f' {algorithm_2}_time']


plt.plot(algorithm_time,algorithm_n)
plt.plot(algorithm2_time,algorithm_n)
plt.title(f'{algorithm}-sort')
plt.xlabel('Time [ms]')
plt.ylabel('n')
plt.legend([f'heap-sort'])
plt.legend(f'{algorithm}-sort')
plt.show()




# %%
