# import torch
# import yaml
# import numpy as np

# # ---- PATHS: sostituire con il modello desiderato ----
# policy_path = "logs/rl_games/omniquad_flat/2025-07-22_13-45-01/nn/omniquad_flat.pth"
# agent_yaml = "logs/rl_games/omniquad_flat/2025-07-22_13-45-01/params/agent.yaml"

# # ---- 1. Carica la config della rete (dal yaml) ----
# with open(agent_yaml, "r") as f:
#     agent_config = yaml.safe_load(f)
# input_size = 41 # agent_config["model"]["input_shape"][0]
# output_size = 12 #agent_config["model"]["output_shape"][0]
# print(f"Input size: {input_size}, Output size: {output_size}")

# # ---- 2. Carica il modello (policy) ----
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# # model = torch.jit.load(policy_path, map_location=device)  # RL-Games salva la policy come torchscript
# model.load_state_dict(ckpt['model'])
# model.eval()

# # ---- 3. Prepara un vettore input finto (dummy) o reale ----
# # ES: crea un vettore random compatibile col tuo input shape
# # In alternativa, metti qui un input reale che vuoi testare
# obs = np.zeros((input_size,), dtype=np.float32)
# # Esempio: obs = np.array([...], dtype=np.float32)

# # ---- 4. Esegui inferenza ----
# obs_tensor = torch.tensor(obs, dtype=torch.float32).unsqueeze(0).to(device)  # batch dimension
# with torch.no_grad():
#     output = model(obs_tensor)
# print("Output della policy:", output.cpu().numpy().squeeze())




import torch
import torch.nn as nn
import numpy as np

policy_path = "logs/rl_games/omniquad_flat/2025-07-22_13-45-01/nn/omniquad_flat.pth"

class MLPPolicy(nn.Module):
    def __init__(self, input_size=41, output_size=12):
        super().__init__()
        self.mlp = nn.Sequential(
            nn.Linear(input_size, 128),
            nn.ELU(),
            nn.Linear(128, 128),
            nn.ELU(),
            nn.Linear(128, 128),
            nn.ELU(),
            nn.Linear(128, output_size)
        )
    def forward(self, x):
        return self.mlp(x)

model = MLPPolicy()
ckpt = torch.load(policy_path, map_location="cpu")
model.load_state_dict(ckpt["model"], strict=False)  # <--- questa è la chiave giusta!
model.eval()

# Dummy observation di input (41 elementi)
obs = np.zeros((41,), dtype=np.float32)
obs_tensor = torch.tensor(obs, dtype=torch.float32).unsqueeze(0)
with torch.no_grad():
    output = model(obs_tensor)
print("Output della policy:", output.cpu().numpy().squeeze())
