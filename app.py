import torch
import subprocess


cuda = torch.cuda.is_available()
devices = torch.cuda.device_count()

print("lspci:")
subprocess.run("lspci | grep -i nvidia", shell=True)
print("nvidia-smi:")

subprocess.run("nvidia-smi", shell=True)

print("CUDA Available:", cuda)

print("CUDA Devices:", devices)
for d in range(devices):
    print(d, ":", torch.cuda.get_device_name(d))
