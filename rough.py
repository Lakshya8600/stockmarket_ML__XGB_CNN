import torch

# print("CUDA Available:",torch.cuda.is_available())
# print("Number of GPUs:", torch.cuda.device_count())
# if torch.cuda.is_available():
#     print("GPU Name:",torch.cuda.get_device_name(0))

print("pytorch version:",torch.__version__)
print("cuda available:",torch.cuda.is_available())
print("cuda version:",torch.version.cuda)
print("gpu name:",torch.cuda.get_device_name(0) if torch.cuda.is_available() else "None")

