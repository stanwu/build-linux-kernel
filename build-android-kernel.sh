#!/bin/bash

# Check Ubuntu version
if [[ $(lsb_release -rs) != "20.04" ]]; then
    echo "This script is designed for Ubuntu 20.04."
    exit 1
fi

# Check if a branch name is provided as an argument
if [ -z "$1" ]; then
    git ls-remote --heads https://android.googlesource.com/kernel/common.git | awk -F/ '{print $3}' | grep -i ^android
    echo "Please give a branch to build, for example android12-5.10"
    exit 1
else
    branch=$1
    # Check branch should be start with android
    if [[ $branch != "android"* ]]; then
        echo "Branch name should start with android"
        exit 1
    fi
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

