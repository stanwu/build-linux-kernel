#!/bin/env python3

import json

# 讀取 build_results.json
database_file = "build_results.json"
markdown_file = "build_results.md"

with open(database_file, "r") as f:
    build_results = json.load(f)

# 建立 Markdown 表格的表頭
markdown_content = "| Branch Name | Build Date | Build Status | Build Environment |\n"
markdown_content += "|-------------|------------|--------------|-------------------|\n"

# 轉換每筆紀錄為 Markdown 表格列
for entry in build_results:
    branch_name = entry["branch_name"]
    build_date = entry["build_date"]
    
    # 狀態顯示顏色
    if entry["build_status"] == "success":
        build_status = "<span style='color:green'>success</span>"
    else:
        build_status = "<span style='color:red'>failed</span>"

    # 編譯環境顯示
    build_environment = f"OS: {entry['build_environment']['os']} {entry['build_environment']['os_version']}, "
    build_environment += f"Arch: {entry['build_environment']['architecture']}, "
    build_environment += f"CPU Cores: {entry['build_environment']['cpu_cores']}"

    # 組成表格列
    markdown_content += f"| {branch_name} | {build_date} | {build_status} | {build_environment} |\n"

# 將結果寫入 build_results.md
with open(markdown_file, "w") as f:
    f.write(markdown_content)

print(f"Markdown 表格已儲存至 {markdown_file}")
