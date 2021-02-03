# Pytorch学习笔记

记录一下自己学习Pytorch的过程（对于官方文档进行下载尝试并翻译）



# 安装操作

## CUDA

这里采用的是Windows10的电脑，有一张英伟达3090显卡（是游戏台式机这种型号）

所以要自己进行cuda的配置，Pytorch当前支撑的最新cuda是11.0，同时考虑本机配置所以使用11.0

下载位置https://developer.nvidia.com/cuda-11.0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exenetwork

驱动程序启动会先检查是否可以，所以直接莽一波先下载也还好，不用特别仔细对照英伟达的参数表。

选择了自定义安装操作，都勾选了没有改动，保险起见路径没有换，还是放在C盘了。

发现需要安装Visual Studio才可以继续，所以还要再安装VS。

`nvcc -V`可以查看（不需要手动设置环境，如果没有就重启一次）

## cuDNN

需要先注册英伟达才能下载

下载对应cuda版本的内容，下载的是一个zip，解压后三个子文件夹在`C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.0`下面有对应项，把zip里面的内容复制到CUDA里面就可以了。





## Pytorch

注意，官网的`-c`是指定了channel，所以用了国外源，很慢，最好是删掉。

安装之后尝试

```python
import torch
print(torch.cuda.is_available())  #返回True则说明已经安装了cuda
from torch.backends import  cudnn 
print(cudnn.is_available())  #返回True则说明已经安装了cuDNN
```

但是在`import torch`这里就出问题了，报错是：

`OSError: [WinError 126] 找不到指定的模块。 Error loading "D:\Anaconda3\lib\site-packages\torch\lib\asmjit.dll" or one of its dependencies.`而且确实那个位置没有这个文件。

先尝试重启看看能不能解决问题

简单重启不行，但是安装[Microsoft Visual C++ Redistributable再重启](https://aka.ms/vs/16/release/vc_redist.x64.exe)就可以了，估计是因为裸机的C++内容不全？







