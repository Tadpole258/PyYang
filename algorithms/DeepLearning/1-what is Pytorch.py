from __future__ import print_function
import torch

x = torch.tensor([5.3,3])

x = x.new_ones(5,3,dtype=torch.double)

x = torch.rand_like(x,dtype=torch.float)
y = torch.rand(5,3)