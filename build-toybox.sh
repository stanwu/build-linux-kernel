#!/bin/bash

# Check Ubuntu version
if [[ $(lsb_release -rs) != "20.04" ]]; then
    echo "This script is designed for Ubuntu 20.04."
    exit 1
fi

echo "Updating package list and installing dependencies..."
sudo apt-get update
sudo apt-get install -y build-essential git

echo "Cloning Toybox repository..."
[ ! -f toybox/Makefile ] && git clone --depth 1 https://github.com/landley/toybox.git
cd toybox || { echo "Failed to change directory to toybox"; exit 1; }

echo "Configuring build with default configuration..."
make defconfig

echo "Compiling Toybox..."
make || { echo "Failed to build toybox"; exit 1; }
echo "Done!"