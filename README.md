# torch_cmake_example

# how to compile

```bash
export CMAKE_PREFIX_PATH=$(python -c "import torch; print(torch.utils.cmake_prefix_path + '/Torch/')"):${CMAKE_PREFIX_PATH}
cmake -B build -S . -G Ninja
cmake --build build
```