import torch
torch.ops.load_library("build/libtorch_extension.so")
torch.ops.torch_extension
a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([4.0, 5.0, 6.0])
c = torch.ops.torch_extension.sin_and_add(a, b)
print(c)
