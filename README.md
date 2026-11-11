# Sonar: Mines vs Rocks Classifier

Classifies sonar signals as **Rock (R)** or **Mine (M)** using Logistic Regression.

`AI101 Mini-Project` · `Team XX`

## Team and roles




## Project structure
```
sonar-mines-vs-rocks/
├── data/sonar.csv
├── src/
│   ├── main.py
├── requirements.txt
└── README.md
```
## Dataset

UCI Connectionist Bench (Sonar, Mines vs. Rocks):
https://archive.ics.uci.edu/dataset/151/connectionist+bench+sonar+mines+vs+rocks
The file `data/sonar.csv` is already included in this repo (original file `sonar.all-data`, renamed, no header row).

## Setup

```
git clone https://github.com/arnav-7003/AI-Project
cd sonar-mines-vs-rocks
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## How to run

1. `python src/main.py`
2. The script prints metrics and saves 4 files in `outputs/`.
3. Expected runtime: under 1 minute.

