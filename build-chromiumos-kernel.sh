#!/bin/bash

# Check Ubuntu version
if [[ $(lsb_release -rs) != "20.04" ]]; then
    echo "This script is designed for Ubuntu 20.04."
    exit 1
fi

# Update package manager and install necessary packages
sudo apt update
sudo apt install -y git build-essential libncurses-dev bison flex libssl-dev bc

# Clone the ChromeOS kernel source code from the repository
[ ! -f kernel/Makefile ] && git clone --depth 1 https://chromium.googlesource.com/chromiumos/third_party/kernel
cd kernel

echo "Copy the base configuration file and run oldconfig to update it"
cp chromeos/config/chromeos/base.config .config
make olddefconfig

echo "Compile the kernel using all available CPU cores"
make -j$(nproc)
make bzImage
echo "The bzImage will be located in arch/x86/boot/ if compiled for x86 architecture"
