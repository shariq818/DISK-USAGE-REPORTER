# disk_usage_reporter.py
# Disk Usage Reporter v1.1 (User Input Version)
# Author: Paradox (shariq818)

import os
import json
from datetime import datetime

def get_size_bytes(path):
    total = 0
    for root, _, files in os.walk(path):
        for f in files:
            try:
                fp = os.path.join(root, f)
                total += os.path.getsize(fp)
            except (FileNotFoundError, PermissionError):
                continue
    return total

def human_readable(num):
    for unit in ("B","KB","MB","GB","TB"):
        if num < 1024.0:
            return f"{num:3.2f} {unit}"
        num /= 1024.0
    return f"{num:.2f} PB"

def build_report(target_dir):
    target_dir = os.path.abspath(target_dir)
    entries = os.listdir(target_dir)

    subdirs = [e for e in entries if os.path.isdir(os.path.join(target_dir, e))]
    root_files_size = 0

    for e in entries:
        full = os.path.join(target_dir, e)
        if os.path.isfile(full):
            try:
                root_files_size += os.path.getsize(full)
            except:
                pass

    usage = {}
    for d in subdirs:
        full = os.path.join(target_dir, d)
        size = get_size_bytes(full)
        usage[d] = size

    sorted_usage = sorted(usage.items(), key=lambda x: x[1], reverse=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    base_name = f"disk_usage_report_{timestamp}"

    text_out = os.path.join(os.getcwd(), base_name + ".txt")
    json_out = os.path.join(os.getcwd(), base_name + ".json")

    # Write text report
    with open(text_out, "w", encoding="utf-8") as f:
        f.write(f"Disk usage report for: {target_dir}\n")
        f.write(f"Generated: {timestamp}\n\n")

        if root_files_size:
            f.write(f"[ROOT FILES] {human_readable(root_files_size)}\n\n")

        f.write("Top-level subfolder usage (largest first):\n")
        f.write("-" * 60 + "\n")
        for name, size in sorted_usage:
            f.write(f"{name:35} {human_readable(size)}\n")

    # Write JSON
    report_json = {
        "target": target_dir,
        "generated_at": timestamp,
        "root_files_size_bytes": root_files_size,
        "subfolders": [
            {"name": name, "size_bytes": size, "size_human": human_readable(size)}
            for name, size in sorted_usage
        ]
    }

    with open(json_out, "w", encoding="utf-8") as jf:
        json.dump(report_json, jf, indent=2)

    return text_out, json_out


if __name__ == "__main__":
    print("=== Disk Usage Reporter ===")
    target = input("Enter the full path of the folder you want to scan: ").strip()

    if not os.path.isdir(target):
        print("Error: That path does not exist or is inaccessible!")
    else:
        print("Scanning... please wait.")
        txt, js = build_report(target)
        print(f"\nReport saved:\n  {txt}\n  {js}")
