import torch
import pandas as pd
from sklearn.metrics import roc_auc_score
from src.model.model import FireRiskModel
from pathlib import Path

def main():
    project_root = Path(__file__).resolve().parents[2]
    data_dir = project_root / "data" / "processed"
    data = pd.read_csv(data_dir / "dataset.csv")
    X = torch.tensor(data.drop(columns=['label']).values, dtype=torch.float32)
    y = data['label'].values

    model = FireRiskModel(X.shape[1])
    model.load_state_dict(torch.load(data_dir / "model.pt"))
    model.eval()

    with torch.no_grad():
        preds = model(X).numpy().ravel()

    print(roc_auc_score(y, preds))

def predict():
    pass