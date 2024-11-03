#!/usr/bin/python3

import os
import platform
import subprocess
import sys
import json
from datetime import datetime

# 設定資料庫檔案名稱
database_file = "build_results.json"

# 初始化資料庫
if not os.path.exists(database_file):
    with open(database_file, "w") as f:
        json.dump([], f)

# 讀取已編譯的 branch 結果
def load_database():
    with open(database_file, "r") as f:
        return json.load(f)

# 更新資料庫
def update_database(data):
    with open(database_file, "w") as f:
        json.dump(data, f, indent=4)

# 檢查是否已經編譯過該 branch
def is_branch_built(database, branch_name):
    return any(entry["branch_name"] == branch_name for entry in database)

# 檢查 Ubuntu 版本
def check_ubuntu_version():
    try:
        result = subprocess.run(["lsb_release", "-rs"], capture_output=True, text=True, check=True)
        if result.stdout.strip() != "20.04":
            print("This script is designed for Ubuntu 20.04.")
            sys.exit(1)
    except subprocess.CalledProcessError:
        print("Unable to determine Ubuntu version.")
        sys.exit(1)

# 列出可用 branch
def get_available_branches():
    branches = subprocess.run(
        ["git", "ls-remote", "--heads", "https://android.googlesource.com/kernel/common.git"],
        capture_output=True, text=True
    )

    # We need exclud deprecated branches
    deprecated_keywords = ["deprecated", "old", "legacy"]
    branch_names = [
        line.split("/")[-1] for line in branches.stdout.splitlines()
        if line.split("/")[-1].startswith("android") and not any(keyword in line.split("/")[-1] for keyword in deprecated_keywords)
    ]
    branch_names.sort()
    return branch_names

# 驗證 branch 名稱
def validate_branch_name(branch):
    if not branch.startswith("android"):
        print("Branch name should start with android")
        sys.exit(1)

# 安裝必要套件
def install_required_packages():
    subprocess.run(["sudo", "apt", "update", "-y"], check=True)
    subprocess.run([
        "sudo", "apt", "install", "-y", "build-essential", "libncurses-dev", "bison", "flex", "libssl-dev", "bc", "git"
    ], check=True)

# 克隆指定的 branch
def clone_repository(branch):
    if not os.path.isdir("common"):
        subprocess.run(
            ["git", "clone", "--depth", "1", "--branch", branch, "https://android.googlesource.com/kernel/common.git"],
            check=True
        )

# 編譯 kernel
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

# 取得編譯環境資訊
def get_build_environment():
    environment = {
        "os": platform.system(),
        "os_version": platform.release(),
        "architecture": platform.machine(),
        "cpu_cores": os.cpu_count()
    }
    return environment

# 主程式
def main():
    # 載入資料庫
    database = load_database()

    # 檢查 Ubuntu 版本
    check_ubuntu_version()

    # 檢查是否提供了 branch 名稱
    if len(sys.argv) < 2:
        available_branches = get_available_branches()
        print("Available branches:")
        for branch in available_branches:
            print(branch)
        print("Please give a branch to build, for example android12-5.10")
        sys.exit(1)
    
    branch = sys.argv[1]
    
    # 驗證 branch 名稱
    validate_branch_name(branch)
    
    # 檢查是否已經編譯過
    if is_branch_built(database, branch):
        print(f"Branch {branch} 已編譯過，跳過")
        sys.exit(0)

    # 安裝必要的套件
    install_required_packages()
    
    # 克隆儲存庫
    clone_repository(branch)
    
    # 編譯 kernel 並儲存結果
    print(f"正在編譯 branch {branch}...")
    build_status = build_kernel()
    build_date = datetime.now().isoformat()

    # 獲取編譯環境資訊
    build_environment = get_build_environment()

    # 新增編譯結果到資料庫
    entry = {
        "branch_name": branch,
        "build_date": build_date,
        "build_status": build_status,
        "build_environment": build_environment
    }
    database.append(entry)
    update_database(database)

    print(f"Branch {branch} 編譯 {build_status}")

if __name__ == "__main__":
    main()
