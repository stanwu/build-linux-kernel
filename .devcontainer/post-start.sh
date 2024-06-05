#!/bin/bash

pwd
#Init build environment
sudo apt update && sudo apt install build-essential libncurses-dev bison flex libssl-dev libelf-dev fakeroot dwarves
echo "Build environment installed"

[ ! -f linux-6.9.3.tar.xz ] && wget https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-6.9.3.tar.xz
[ ! -f linux-6.9.3/Makefile ] && tar -xvf linux-6.9.3.tar.xz
cd linux-6.9.3/
cp ../.config .
make

