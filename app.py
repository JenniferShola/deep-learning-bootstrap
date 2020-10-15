import torch

cuda = torch.cuda.is_available()
devices = torch.cuda.device_count()


print("CUDA Available:", cuda)

print("CUDA Devices:", devices)
for d in range(devices):
    print(d, ":", torch.cuda.get_device_name(d))
