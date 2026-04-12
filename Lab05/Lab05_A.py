import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('sales_data.csv')
plt.xkcd()
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
ax1.plot(data[['month_number']],data[['bathingsoap']],"-o",c='black',linewidth='2')
ax1.set_title("Sales data of a Bathingsoap",fontdict={'size': 12})
ax1.set_yticks(np.linspace(7500,12500,3))
ax2.plot(data[['month_number']],data[['facewash']],"-o",c='black',linewidth='2')
ax2.set_title("Sales data of a Fashwash",fontdict={'size': 12})
ax2.set_xticks(np.linspace(1,12,12))
ax2.set_yticks(np.linspace(1500,2000,2))
fig.supxlabel('Month Number',fontsize='13',y=0)
fig.supylabel('Sales units in number',x=0)

plt.show()