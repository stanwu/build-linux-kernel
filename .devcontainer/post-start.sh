#!/bin/bash

echo "Downloading kernel source"
[ ! -f linux-6.9.3.tar.xz ] && wget https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-6.9.3.tar.xz
[ ! -f linux-6.9.3/Makefile ] && tar -xvf linux-6.9.3.tar.xz

echo "Make kernel"
cd linux-6.9.3/
cp ../.config .
make

