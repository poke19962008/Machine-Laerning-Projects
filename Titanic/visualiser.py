import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('train.csv')

def survivalFreq(X='Age',diff=False):
    groupS = df.groupby(['Survived']).get_group(1)
    groupS = groupS.groupby([X])[X].aggregate(len)
    groupS = pd.DataFrame({X: groupS.index, 'Frequency': groupS.values})

    groupD = df.groupby(['Survived']).get_group(0)
    groupD = groupD.groupby([X])[X].aggregate(len)
    groupD = pd.DataFrame({X: groupD.index, 'Frequency': groupD.values})

    group = pd.merge(groupD, groupS, how='inner', on=X, suffixes=('Dead', 'Survived'))
    if not diff:
        group[['FrequencyDead', 'FrequencySurvived']].plot.bar(x=group[X], title='%s And Survival Frequency'%X, stacked=True)
    else:
        group['diff'] = group.FrequencySurvived - group.FrequencyDead
        group[['diff']].plot.bar(x=group[X], title='%s And Survival Frequency'%X, stacked=True); plt.axhline(0, color='k')

if __name__ == '__main__':
    survivalFreq('Pclass', diff=False)

    plt.show()
