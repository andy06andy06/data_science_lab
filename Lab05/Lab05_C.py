import matplotlib.pyplot as plt
import pandas as pd

score = pd.read_csv('Score.csv')
score.loc[len(score['Round'])] = [12, 'P', '', 0]
score.loc[len(score['Round'])] = [11, 'P', '', 0]
filt_K = score['Team']=='K'
filt_D = score['Team']=='D'
filt_P = score['Team']=='P'

y1 = score.loc[filt_D]['Score'].values
y2 = score.loc[filt_K]['Score'].values
fig, ax = plt.subplots(1, 1,zorder=3)
p2 = ax.barh(score.loc[filt_D]['Round'],score.loc[filt_D]['Score'], color='#9fd959',label='Team D', zorder=2, edgecolor='w', height=0.6)
p1 = ax.barh(score.loc[filt_K]['Round'],score.loc[filt_K]['Score'], left=y1, color='#62b0ff',label='Team K', zorder=2, edgecolor='w', height=0.6)
p3 = ax.barh(score.loc[filt_P]['Round'],score.loc[filt_P]['Score'], left=y1+y2, color='#ffc003',label='Team P', zorder=2, edgecolor='w', height=0.6)
pp=[p1,p2,p3]
ax.legend([p1,p2.patches[0],p3],[p.get_label() for p in pp], bbox_to_anchor =(0.86,0.3), handlelength=1.7, handleheight=2.2)
ax.grid(which='major', zorder=0, axis='x')
ax.set_xticks(range(0,180,20))
ax.xaxis.tick_top()
ax.set_title('Points')
ax.tick_params(left=False, top=False)
ax.bar_label(p1, labels=score.loc[filt_D]['Leader'].values, label_type='center')
ax.bar_label(p2, labels=score.loc[filt_K]['Leader'].values, label_type='center')
ax.bar_label(p3, labels=score.loc[filt_P]['Leader'].values, label_type='center')

ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.bottom.set_visible(False)

plt.show()
