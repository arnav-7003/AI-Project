#Importing Libraries
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, confusion_matrix, classification_report,
                             ConfusionMatrixDisplay)

BASE = Path(__file__).resolve().parent.parent
OUT = BASE / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(BASE / "data" / "sonar.csv", header=None)
df.columns = [f"f{i}" for i in range(60)] + ["label"]

print("Shape:", df.shape)
print("Missing values:", df.isnull().sum().sum())
print(df.head())
print(df["label"].value_counts())

# Class distribution graph
counts = df["label"].value_counts()
plt.bar(["Rock", "Mine"], [counts["R"], counts["M"]], color=["tab:blue", "tab:orange"])
plt.title("Class distribution")
plt.xlabel("Class")
plt.ylabel("Number of samples")
plt.savefig(OUT / "class_distribution.png")
plt.close()
print("Saved outputs/class_distribution.png")
#Average signal of rock vs Mine across the 60 frequency bands 
feaature_cols = [f"f{i}" for i in range(60)]
plt.figure(figsize=(8,4))
plt.plot(df[df["label"] == "R"][feature_cols].mean().values, label="Rock", color="tab:blue")
plt.plot(df[df["label"] == "M"][feature_cols].mean().values, label="Mine", color"tab:orange")
plt.title("Average sonar signal: Rock vs Mine")
plt.xlabel("Feature number (frequency band)")
plt.ylabel("Average energy")
plt.legend()
plt.grid(alpha=0.25)
plt.savefig(OUT / "avg_signal_rock_vs_mine.png")
X=df.drop("label", axis=1)
y = df["label"].map({"R": 0, "M": 1})   #Rock = 0, Mine = 1
X_train, X_tests, y_train, y_test = train_test_split(
  X, y, test_size=0.20, random_state=42, stratify=y)
print("\nTrain:", X_train.shape, "Test:", X_test.shape)

#Normalization: standardScaler (fit only on training data)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

#correlation between features (training data only)
corr = X_train.corr()
plt.figure(figsize=(6,5))
plt.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
plt.colorbar(label="Correlation")
plt.title("Feature correlaation (training data)")
plt.xlabel("Feature number")
plt.ylabel("Feature number")
plt.savefig(OUT / "feature_correlation (training data)")
plt.close()
print("saved outputs/feature_correlation.png")

#Correlation of each feature with the label 
corr_with_label = X_train.apply(lambda col: col.corr(y_train))
top20 = corr_with_label.abs().sort_values(asccending=False).head(20)
print("\nTop 10 features most correlated with the label:")
print(corr_with_label[top20.index[:10].round(3).to_string())

#Feature selection: keep the 20 features most correlated with the label 
selected_features = list(top20.index)
idx = [list(X.columns).index(C) for c in selected_features]  #column positions
X_train_sel = X_train_scaled[:, idx]
X_test_sel = X_test_scaled[:, idx]
print("selected", len(selected_features), "features")

















            




















































# confusion matrix
ConfusionMatrixDisplay.from_predictions(y_test,y_pred_all,display_labels=["Rock","Mine"],cmap="Blues")
plt.title("confusion matrix:all 60 features")
plt.savefig( OUT / "confusion_matrix.png")
plt.close()
print("saved outputs/confusion_matrix.png")

#training plot : accuracy vs training plot size
sizes = np.linspace(0.1,1.0,10)
train_scores,test_scores=[],[]
for frac in sizes:
    n=int(frac*len(x_train_scaled))
    m=train_model(x_train_scaled[:n],y_train.iloc[:n])

train_scores.append(accuracy_score(y_train.iloc[:n],m.predict(x_train_scaled[:n])))
test_scores.append(accuracy_score(y_test,m.predict(x_test_scaled)))

plt.figure(figsize=(7,4))
plt.plot(sizes * 100, train_scores, marker="o", label="Training accuracy")
plt.plot(sizes * 100, test_scores, marker="o", label="Test accuracy")
plt.title("accuracy vs training set size")
plt.xlabel("Training set size (%)")
plt.ylabel("accuracy")
plt.legend()
plt.grid(alpha=0.25)
plt.savefig( OUT/ "training_plot.png")
plt.close()
print("saved outputs/training_plot.png")
                                        
#metrics comparision
results_df.set_index("Model")[["Accuracy","Precision","Recall","F1"]].plot(kind="bar",figsize=(8,4))
plt.title("logistic regression:all features vs selected features")
plt.ylabel("score")
plt.ylim(0,1.05)
plt.xticks(rotation=0)
plt.grid(axis=y,alpha=0.25)
plt.savefig( OUT / "metrics_comparision.png")
plt.close()
print("saved outputs/metrics_comparision.png")

# actual vs predicted class counts 
actual=[(y_test==0).sum(),(y_test==1).sum()]
predicted=[(y_pred_all==0).sum(),(y_pred_all==1).sum()]
x = np.arange(2)
plt.figure(figsize=(6,4))
plt.bar(x-0.2,actual,width=0.4,label="actual")
plt.bar(x+0.2,predicted,width=0.4,label="predicted")
plt.xticks(x,["Rock","Mine"])
plt.title("actual vs predicted class counts(test set)")
plt.xlabel("class")
plt.ylabel("no of samples")
plt.legend()
plt.savefig( OUT / "actual_vs_predicted.png")
plt.close()
print("saved outputs/actual_vs_predicted.png")

#top 10 features by coefficients
coef=model_all.coef_[0]
top=np.argsort(np.abs(coef))[-10:]
plt.figure(figsize=(7,5))
plt.barh([f"feature{i}"for i in top],coef[top],color=['tab:orange' if coef[i]>0 else 'tab:blue' for i in top])
plt.title("top 10 featues orange:mine , blue:rock")
plt.xlabel("coefficient value")
plt.tight_layout()
plt.savefig( OUT / "top_features.png")
plt.close()
print("saved outputs/top_features.png")

#results table as an image
fig,ax=plt.subplots(figsize=(8,1.8))
ax.axis("off")
table=ax.table(cellText=results_df.round(3).values,colLabels=results_df.columns,loc="center",cellLoc="center")
table.auto_set_font_size(False)
table.set_fontsize(11)
table.auto_set_column_width(col=list(range(len(results_df.columns))))
table.scale(1,1.6)
for col in range(len(results_df.columns)):
    table[(0,col)].set_facecolor("#d9e2f3")
plt.savefig(OUT /"results_table.png",bbox_inches="tight",dpi=150)
plt.close()
print("saved outputs/results_table.png")
print("\nDone! Plots and results.csv saved in outputs/")
