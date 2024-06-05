#!/bin/bash

# Update package manager and install required packages
sudo apt update -y
sudo apt install -y build-essential libncurses-dev bison flex libssl-dev bc git

# Download the kernel source code (example using AOSP common branch)
[ ! -f common/Makefile ] && git clone https://android.googlesource.com/kernel/common.git

echo "Make kernel"
cd common
# Configure the kernel (using default configuration)
make ARCH=x86 defconfig
# Compile the kernel
make ARCH=x86 -j$(nproc)

