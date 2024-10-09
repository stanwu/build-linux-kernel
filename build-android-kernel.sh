#!/bin/bash

# Check Ubuntu version
if [[ $(lsb_release -rs) != "20.04" ]]; then
    echo "This script is designed for Ubuntu 20.04."
    exit 1
fi

# Update package manager and install required packages
sudo apt update -y
sudo apt install -y build-essential libncurses-dev bison flex libssl-dev bc git

# Download the Android 12 kernel 5.10 source code
[ ! -d common ] && git clone --depth 1 --branch android12-5.10 https://android.googlesource.com/kernel/common.git

echo "Make Android's latest kernel"
cd common
# Configure the kernel (using default configuration)
make ARCH=x86 defconfig
# Compile the kernel
make ARCH=x86 -j$(nproc)

