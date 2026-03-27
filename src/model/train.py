import torch
import pandas as pd
from src.model.model import FireRiskModel
from pathlib import Path
import sqlite3

def main():
    project_root = Path(__file__).resolve().parents[2]
    data_dir = project_root / "data" / "processed"

    with sqlite3.connect(data_dir / "dataset.db") as conn:
        data = pd.read_sql_query("SELECT * FROM dataset", conn)

    X = torch.tensor(data.drop(columns=['label']).values, dtype=torch.float32)
    y = torch.tensor(data['label'].values, dtype=torch.float32).unsqueeze(1)

    device = 'cuda' if torch.cuda.is_available() else 'cpu' # NEED TO GET PROPER ENVIRONMENT SET UP FOR USING CUDA
    print(f'USING {device} device')

    model = FireRiskModel(X.shape[1])
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    loss_fn = torch.nn.BCELoss()

    model.to(device)

    for _ in range(20):
        optimizer.zero_grad()
        preds = model(X)
        loss = loss_fn(preds, y)
        print(loss)
        loss.backward()
        optimizer.step()

    torch.save(model.state_dict(), data_dir / "model.pt")
