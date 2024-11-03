#!/usr/bin/python3

import os
import platform
import subprocess
import sys
import json
from datetime import datetime

# Set the database file name
database_file = "build_results.json"

# Initialize the database
if not os.path.exists(database_file):
    with open(database_file, "w") as f:
        json.dump([], f)

# Load the build results from the database
def load_database():
    with open(database_file, "r") as f:
        return json.load(f)

# Update the database
def update_database(data):
    with open(database_file, "w") as f:
        json.dump(data, f, indent=4)

# Check if the branch has already been built
def is_branch_built(database, branch_name):
    return any(entry["branch_name"] == branch_name for entry in database)

# Check the Ubuntu version
def check_ubuntu_version():
    try:
        result = subprocess.run(["lsb_release", "-rs"], capture_output=True, text=True, check=True)
        if result.stdout.strip() != "20.04":
            print("This script is designed for Ubuntu 20.04.")
            sys.exit(1)
    except subprocess.CalledProcessError:
        print("Unable to determine Ubuntu version.")
        sys.exit(1)

# List available branches
def get_available_branches():
    branches = subprocess.run(
        ["git", "ls-remote", "--heads", "https://android.googlesource.com/kernel/common.git"],
        capture_output=True, text=True
    )

    # Exclude deprecated branches
    deprecated_keywords = ["deprecated", "old", "legacy"]
    branch_names = [
        line.split("/")[-1] for line in branches.stdout.splitlines()
        if line.split("/")[-1].startswith("android") and not any(keyword in line.split("/")[-1] for keyword in deprecated_keywords)
    ]
    branch_names.sort()
    return branch_names

# Validate branch name
def validate_branch_name(branch):
    if not branch.startswith("android"):
        print("Branch name should start with android")
        sys.exit(1)

# Install required packages
def install_required_packages():
    subprocess.run(["sudo", "apt", "update", "-y"], check=True)
    subprocess.run([
        "sudo", "apt", "install", "-y", "build-essential", "libncurses-dev", "bison", "flex", "libssl-dev", "bc", "git"
    ], check=True)

# Clone the specified branch
def clone_repository(branch):
    if not os.path.isdir("common"):
        subprocess.run(
            ["git", "clone", "--depth", "1", "--branch", branch, "https://android.googlesource.com/kernel/common.git"],
            check=True
        )

# Build the kernel
def build_kernel():
    os.chdir("common")
    try:
        subprocess.run(["make", "ARCH=x86", "defconfig"], check=True)
        subprocess.run(["make", "ARCH=x86", f"-j{os.cpu_count()}"], check=True)
        return "success"
    except subprocess.CalledProcessError:
        return "failed"
    finally:
        os.chdir("..")

# Get build environment information
def get_build_environment():
    environment = {
        "os": platform.system(),
        "os_version": platform.release(),
        "architecture": platform.machine(),
        "cpu_cores": os.cpu_count()
    }
    return environment

# Main function
def main():
    # Load the database
    database = load_database()

    # Check the Ubuntu version
    check_ubuntu_version()

    # Check if a branch name is provided
    if len(sys.argv) < 2:
        available_branches = get_available_branches()
        print("Available branches:")
        for branch in available_branches:
            print(branch)
        print("Please give a branch to build, for example android12-5.10")
        sys.exit(1)
    
    branch = sys.argv[1]
    
    # Validate branch name
    validate_branch_name(branch)
    
    # Check if the branch has already been built
    if is_branch_built(database, branch):
        print(f"Branch {branch} has already been built, skipping")
        sys.exit(0)

    # Install required packages
    install_required_packages()
    
    # Clone the repository
    clone_repository(branch)
    
    # Build the kernel and save the result
    print(f"Building branch {branch}...")
    build_status = build_kernel()
    build_date = datetime.now().isoformat()

    # Get build environment information
    build_environment = get_build_environment()

    # Add the build result to the database
    entry = {
        "branch_name": branch,
        "build_date": build_date,
        "build_status": build_status,
        "build_environment": build_environment
    }
    database.append(entry)
    update_database(database)

    print(f"Branch {branch} build {build_status}")

if __name__ == "__main__":
    main()