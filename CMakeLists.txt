# Minimum CMake version required to generate
# our build system
cmake_minimum_required(VERSION 3.0)

# Name of our Project
project(buttons)

# add_executable creates an executable with
# The given name. In our case it is "Hello"
# Source files are given as parameters. In our
# Case we only have one source file Hello.cpp
add_executable(buttons buttons.cpp)