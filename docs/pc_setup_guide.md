# DAugmentor: PC Setup Guide

### PC/Workstation requirements for the project **DAugmentor**

Following are the specification of the machine that has been used to develop the project **DAugmentor** 

- Machine Type - Gaming Laptop 
- CPU - Intel(R) Core(TM) I7-8750H 
- CPU Cores - 6 and 12 LP
- Memory - 16GB
- GPU - NVIDIA GeForce GTX 1050 Ti

Following are the necessary steps you need to follow in oreder to prepare your PC to run the project **DAugmentor** 

#### Step 01 - Setting up GPU 
- To Install comapatible latest NVIDIA drivers visit[NVIDIA Driver Downloads](https://www.nvidia.com/Download/index.aspx).
- Select your GPU and download the relevant installer and install it.
- Also, you can install [GeForce Experience](https://www.nvidia.com/en-us/geforce/geforce-experience/) software to keep your machine up-to-date with latest GPU drivers.

#### Step 02 - Setting up CUDA
If you are curious about what's this fancy word **'CUDA'** don't  forget to learn about **CUDA** from [**here**](https://blogs.nvidia.com/blog/2012/09/10/what-is-cuda-2/) .

- Download the latest compatible CUDA version from the **[NVIDIA site](https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exenetwork)**.
- If you are using a **windows OS**, **before you install CUDA**, you need to install **Visual Studio** or you need to have it on your machin. Becuase CUDA uses a specific c compiler from Visual Studio resources.
- [Download Visual Studio (Community Edition)](https://visualstudio.microsoft.com/downloads/) .
- If you have install Visual Studio and **C++ development related resources** you can go ahead and install CUDA now.
- In order to make sure that CUDA is properly working you can try out  one of the CUDA Samples on Visual Studio. 
- The version of the CUDA Toolkit can be checked by running `nvcc -V` in a Command Prompt window.

**Useful links** 

- [CUDA Installation](https://www.youtube.com/watch?v=cL05xtTocmY)
- [To solve CUDA Samples not running issue](https://devtalk.nvidia.com/default/topic/933708/cuda-setup-and-installation/compiling-and-setting-up-cuda-libraries-on-windows-10/post/4869753/).
