import torch
import pandas as pd
from sklearn.metrics import roc_auc_score
from src.model.model import FireRiskModel

def main():
    data = pd.read_csv(f'..\\..\\data\\processed\\dataset.csv')
    X = torch.tensor(data.drop(columns=['label']).values, dtype=torch.float32)
    y = data['label'].values

    model = FireRiskModel(X.shape[1])
    model.load_state_dict(torch.load(f'..\\..\\data\\processed\\model.pt'))
    model.eval()

    with torch.no_grad():
        preds = model(X).numpy().ravel()

    print(roc_auc_score(y, preds))

def predict():
    pass