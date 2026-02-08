import torch
import pandas as pd
from src.model.model import FireRiskModel

def main():
    data = pd.read_csv(f'..\\..\\data\\processed\\dataset.csv')
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

    torch.save(model.state_dict(), f'..\\..\\data\\processed\\model.pt')
