#pragma once

#include <torch/all.h>

torch::Tensor sin_and_add(torch::Tensor x, torch::Tensor y) {
    return torch::sin(x) + y;
}

TORCH_LIBRARY(torch_extension, m) {
    m.def("sin_and_add", &sin_and_add);
} 
