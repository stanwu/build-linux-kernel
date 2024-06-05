#!/bin/bash

#Init build environment
sudo apt update && sudo apt install build-essential libncurses-dev bison flex libssl-dev libelf-dev fakeroot dwarves
echo "Build environment installed"
