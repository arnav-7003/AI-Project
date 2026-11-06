# Kashish 2026AIB1048 : METRICS GRAPH , ACTUAL VS PREDICTED, TOP FEATURES, RESULT TABLE IMAGE
import numpy as np
import matplotlib.pyplot as plt
from member_a_load_eda import OUT

def plot_metrics(result_df):
    """ BAR CHART OF ACCURACY, PRECISION ,RECALL AND F1 SCORE OF THE MODEL"""
row = result_df.iloc[0] 
names = ['Accuracy', 'Precision', 'Recall', 'F1']
values=[row[n] for n in names]
plt.figure(figsize=(6,4))
bars = plt.bar(names,values,color=["tab:blue", "tab:orange", "tab:green", "tab:red"])
for bars, v in zip(bars,values):
    plt.text(bars.get_x() + bars.get_width()/2, v + 0.02, f'{v:.2f}', ha='center')
plt.ylim(0,1.1)  
plt.title('logistic regression :metrics on dataset') 
plt.savefig(OUT / "metrics_bar.png")
plt.close()
print('saved outputs/metrics_bar.png')