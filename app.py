import time
import torch
import subprocess
import pytorch_lightning as pl
import wandb
import matplotlib as mpl
import numpy as np


print("lspci:")
p = subprocess.Popen(
    "lspci | grep -i nvidia", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
)
p.wait()
print(p.stdout.read().decode("utf-8"))


print("nvidia-smi:")
p = subprocess.Popen(
    "nvidia-smi", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
)
p.wait()
print(p.stdout.read().decode("utf-8"))


print("CUDA Available:", torch.cuda.is_available())


devices = torch.cuda.device_count()
print("CUDA Devices:", devices)
for d in range(devices):
    print(d, ":", torch.cuda.get_device_name(d))
