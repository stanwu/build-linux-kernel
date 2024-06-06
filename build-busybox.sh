#!/bin/bash

echo "Updating package list and installing dependencies..."
sudo apt-get update
sudo apt-get install -y build-essential libncurses5-dev bison flex git

echo "Cloning BusyBox repository..."
[ ! -f busybox/Makefile ] && git clone git://busybox.net/busybox.git
cd busybox || { echo "Failed to change directory to busybox"; exit 1; }

echo "Configuring build with default configuration..."
make defconfig

echo "Compiling BusyBox..."
make
