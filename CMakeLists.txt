cmake_minimum_required(VERSION 3.18)
project(torch_extension)

# Find required packages
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)
find_package(Torch REQUIRED)

# Add the src file
add_library(torch_extension SHARED src.cpp)

# Include directories
target_include_directories(torch_extension PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/include
    ${TORCH_INCLUDE_DIRS}
)

# Link against PyTorch
target_link_libraries(torch_extension PRIVATE
    ${TORCH_LIBRARIES}
    Python3::Python
) 