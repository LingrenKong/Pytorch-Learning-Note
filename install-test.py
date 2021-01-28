# 测试是否安装成功了GPU版本的Pytorch

import torch
print(torch.cuda.is_available())  #返回True则说明已经安装了cuda
#判断是否安装了cuDNN
from torch.backends import  cudnn 
print(cudnn.is_available())  #返回True则说明已经安装了cuDNN