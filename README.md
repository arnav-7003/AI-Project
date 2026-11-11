# Sonar: Mines vs Rocks Classifier

Classifies sonar signals as **Rock (R)** or **Mine (M)** using Logistic Regression.

`AI101 Mini-Project` · `Team 55`

## Team and roles

| Member | Entry no. | Role |
|--------|-----------|------|
| Rishabh Mahar | 2026EEB1399 | PPT lead |
| Dhiraj Kumar Yadav | 2026MCB1525 | Execution lead |
| Arnav Yadav | 2026EEB1326 | Documentation lead |
| Kashish  | 2026AIB1048 | Video lead |

## Project structure
```
AI-Project/
├── data/
│   └── sonar.csv                  # 208 rows, 60 features + label (R/M)
├── src/
│   └── main.py                    # single script: EDA, feature selection, model, plots
├── outputs/                       # created when you run main.py
│   ├── class_distribution.png
│   ├── avg_signal_rock_vs_mine.png
│   ├── feature_correlation.png
│   ├── confusion_matrix.png
│   ├── training_plot.png
│   ├── metrics_comparison.png
│   ├── actual_vs_predicted.png
│   ├── top_features.png
│   ├── results_table.png
│   └── results.csv
├── media/                         # screenshots used in README
│   ├── result1.jpg                # results table
│   ├── result2.jpg                # terminal output part 1
│   └── result3.jpg                # terminal output part 2
├── Project Presentation Team 55.pptx
├── requirements.txt
└── README.md
```
## Dataset

UCI Connectionist Bench (Sonar, Mines vs. Rocks):
https://archive.ics.uci.edu/dataset/151/connectionist+bench+sonar+mines+vs+rocks
The file `data/sonar.csv` is already included in this repo (original file `sonar.all-data`, renamed, no header row).

## Setup

Tested on Python 3.14 (Windows).
Run following commands one by one.

```
git clone https://github.com/arnav-7003/AI-Project.git
cd AI-Project
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## How to run

1. `python src/main.py`
2. The script prints metrics and saves 10 files in `outputs/`.
3. Expected runtime: under 1 minute.


## Expected output

![Terminal output part 1](media/result2.jpg)
![Terminal output part 2](media/result3.jpg)


## Results

![Result](media/result1.jpg)

## Links

Video - https://youtu.be/NlTKFqgT7nQ

PPT - https://github.com/arnav-7003/AI-Project/blob/main/Project%20Presentation%20Team%2055.pptx

## AI-use disclosure

AI tools were used for limited assistance with code development, debugging, code review, basic Git commands, and language refinement for the PPT. All AI-generated suggestions were reviewed, modified, and verified by us. We take full responsibility for the final work, its accuracy, and implementation.
