import torch
import pandas as pd
from model import FireRiskModel

PROCESSED_DIR = 'data/processed'

data = pd.read_csv(f'{PROCESSED_DIR}/dataset.csv')
X = torch.tensor(data.drop(columns=['label']).values, dtype=torch.float32)
y = torch.tensor(data['label'].values, dtype=torch.float32).unsqueeze(1)

model = FireRiskModel(X.shape[1])
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
loss_fn = torch.nn.BCELoss()

for _ in range(20):
    optimizer.zero_grad()
    preds = model(X)
    loss = loss_fn(preds, y)
    loss.backward()
    optimizer.step()

torch.save(model.state_dict(), f'{PROCESSED_DIR}/model.pt')
