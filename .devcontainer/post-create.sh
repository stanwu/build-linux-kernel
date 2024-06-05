#!/bin/bash

pwd
#Init build environment
sudo apt -y update && sudo apt -y install build-essential libncurses-dev bison flex libssl-dev libelf-dev fakeroot dwarves
echo "Build environment installed"
