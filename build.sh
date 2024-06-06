#!/bin/bash

default="6.9.3"

echo "Downloading kernel source"
[ ! -f linux-${default}.tar.xz ] && wget https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-${default}.tar.xz
echo "Extracting kernel source"
[ ! -f linux-${default}/Makefile ] && tar -xf linux-${default}.tar.xz

echo "Make kernel"
cd linux-${default}/
cp ../.config .
make