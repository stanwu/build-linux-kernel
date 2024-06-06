#!/bin/bash

if [ -z "$1"]; then
    default="6.1.92"
else
    default="$1"
fi    

echo "Downloading kernel source"
[ ! -f linux-${default}.tar.xz ] && wget https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-${default}.tar.xz
echo "Extracting kernel source"
[ ! -f linux-${default}/Makefile ] && tar -xf linux-${default}.tar.xz

echo "Make kernel"
cd linux-${default}/
cp ../.config .
make

