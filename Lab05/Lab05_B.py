import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

excel = pd.read_excel ('Scatter.xlsx')
filtcc = excel['Genotype']==0
filtCc = excel['Genotype']==1
filtCC = excel['Genotype']==2
fig = plt.figure(figsize=(6,6))
grid = plt.GridSpec(3, 3, wspace=0.7, hspace=0.7, figure=fig)
ax1 = fig.add_subplot(grid[0:2, 0])
ax2 = fig.add_subplot(grid[2, 0])
ax3 = fig.add_subplot(grid[0:2, 1:])
ax4 = fig.add_subplot(grid[2, 1:])

ax1.hist([excel.loc[filtcc]['PC2'],excel.loc[filtCc]['PC2'], excel.loc[filtCC]['PC2']], rwidth=0.8, edgecolor='k', stacked=True, orientation='horizontal', color=['#ff8084','#feff92','#80c8ff'])
ax1.set_xticks(np.linspace(0,10,3))
ax1.set_yticks(np.linspace(-400,400,5))
ax1.set_xlabel("Frequency")
ax1.set_ylabel("PC2")
ax2.axes.xaxis.set_visible(False)
ax2.axes.yaxis.set_visible(False)
ax3.scatter(excel.loc[filtcc]['PC1'],excel.loc[filtcc]['PC2'],c='#ff8084',marker='^', label='c/c', edgecolor='k')
ax3.scatter(excel.loc[filtCc]['PC1'],excel.loc[filtCc]['PC2'],c='#feff92',marker='o', label='C/c', edgecolor='k')
ax3.scatter(excel.loc[filtCC]['PC1'],excel.loc[filtCC]['PC2'],c='#80c8ff',marker='s', label='C/C', edgecolor='k')
ax3.legend(bbox_to_anchor =(-0.3,-0.3),frameon=False, markerscale=2)
ax3.set_title("Scatter Plot",fontdict={'size': 12})
ax3.set_xlabel("PC1")
ax3.set_ylabel("PC2")
ax3.set_xticks(np.linspace(-400,400,5))
ax3.set_yticks(np.linspace(-400,400,5))
ax4.hist([excel.loc[filtcc]['PC1'],excel.loc[filtCc]['PC1'], excel.loc[filtCC]['PC1']], rwidth=0.8, edgecolor='k', stacked=True, color=['#ff8084','#feff92','#80c8ff'])
ax4.set_xlabel("PC1")
ax4.set_ylabel("Frequency")
ax4.set_xticks(np.linspace(-400,400,5))
ax4.set_yticks(np.linspace(0,10,3))

plt.show()