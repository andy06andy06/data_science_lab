import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('StudentsPerformance.csv')

temp = data[['math score','reading score','writing score']]
data['average score'] = temp.mean(axis=1)
print(data.info())
print(data.corr())

fig = plt.figure(figsize=(11,7))
ax1 = fig.add_subplot(4,4,1)
ax1.hist(data['math score'], bins=30, color='r')
ax1.set_title('math score')
ax2 = fig.add_subplot(4,4,2)
ax2.hist(data['reading score'], bins=30, color='g')
ax2.set_title('reading score')
ax3 = fig.add_subplot(4,4,3)
ax3.hist(data['writing score'], bins=30, color='b')
ax3.set_title('writing score')
ax4 = fig.add_subplot(4,4,4)
ax4.hist(data['average score'], bins=30, color='k')
ax4.set_title('average score')

ax5 = fig.add_subplot(4,4,5)
ax5.pie(data['gender'].value_counts(), textprops={'fontsize': 8}, autopct='%1.1f%%', labels=data['gender'].value_counts().index.to_list())
ax5.set_title('gender')
ax6 = fig.add_subplot(4,4,6)
ax6.pie(data['race/ethnicity'].value_counts(), textprops={'fontsize': 8}, autopct='%1.1f%%', labels=data['race/ethnicity'].value_counts().index.to_list())
ax6.set_title('race/ethnicity')
ax7 = fig.add_subplot(4,4,7)
ax7.pie(data['parental level of education'].value_counts(), textprops={'fontsize': 8}, autopct='%1.1f%%', labels=data['parental level of education'].value_counts().index.to_list())
ax7.set_title('parental level of education')
ax8 = fig.add_subplot(4,4,8)
ax8.pie(data['lunch'].value_counts(), textprops={'fontsize': 8}, autopct='%1.1f%%', labels=data['lunch'].value_counts().index.to_list())
ax8.set_title('lunch')
ax9 = fig.add_subplot(4,4,9)
ax9.pie(data['test preparation course'].value_counts(), textprops={'fontsize': 8}, autopct='%1.1f%%', labels=data['test preparation course'].value_counts().index.to_list())
ax9.set_title('test preparation course')

ax10 = fig.add_subplot(4,4,10)
ax10.boxplot([data['math score'], data['reading score'], data['writing score']],vert=False)
ax10.set_yticklabels(['math', 'reading', 'writing'])
ax10.set_title('score')

filt_groupA = data['race/ethnicity']=='group A'
filt_groupB = data['race/ethnicity']=='group B'
filt_groupC = data['race/ethnicity']=='group C'
filt_groupD = data['race/ethnicity']=='group D'
filt_groupE = data['race/ethnicity']=='group E'
ax11 = fig.add_subplot(4,4,11)
ax11.boxplot([data[filt_groupA]['average score'],data[filt_groupB]['average score'],data[filt_groupC]['average score'],data[filt_groupD]['average score'],data[filt_groupE]['average score']])
ax11.set_xticklabels(['A', 'B', 'C', 'D', 'E'])
ax11.set_title('race vs average')

filt_bachlor = data['parental level of education']=="bachelor's degree"
filt_somecol = data['parental level of education']=="some college"
filt_master = data['parental level of education']=="master's degree"
filt_associate = data['parental level of education']=="associate's degree"
filt_high = data['parental level of education']=="high school"
filt_somehigh = data['parental level of education']=="some high school"
ax12 = fig.add_subplot(4,4,12)
ax12.boxplot([data[filt_high]['average score'], data[filt_somehigh]['average score'], data[filt_somecol]['average score'], data[filt_associate]['average score'], data[filt_bachlor]['average score'], data[filt_master]['average score']])
ax12.set_title('parental edu vs average')
ax12.set_xticklabels(['H','SH','SC','A','B','M'])

filt_standard = data['lunch']=='standard'
filt_free = data['lunch']=='free/reduced'
ax13 = fig.add_subplot(4,4,13)
ax13.boxplot([data[filt_free]['average score'], data[filt_standard]['average score']])
ax13.set_title('lunch vs average')
ax13.set_xticklabels(['free/reduce','standard'])

filt_none = data['test preparation course']=='none'
filt_complete = data['test preparation course']=='completed'
ax14 = fig.add_subplot(4,4,14)
ax14.boxplot([data[filt_none]['average score'],data[filt_complete]['average score']])
ax14.set_title('prepare vs average')
ax14.set_xticklabels(['none','completed'])

ax15 = fig.add_subplot(4,4,15)
ax15 = sns.boxplot(x=data['average score'], y=data['lunch'], hue=data['gender'], orient='h')
ax15.legend(bbox_to_anchor= (0.3,1), fontsize=7)

ax16 = fig.add_subplot(4,4,16)
ax16 = sns.boxplot(x=data['average score'], y=data['test preparation course'], hue=data['gender'], orient='h')
ax16.legend(bbox_to_anchor= (0.3,1), fontsize=7)

plt.tight_layout()
plt.show()
