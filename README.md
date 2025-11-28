# 📊 Directory Disk Usage Reporter v1.0
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen)
![Category](https://img.shields.io/badge/Category-Ops-orange)

A small Python utility that scans a target directory, computes disk usage for top-level subfolders and root files, and outputs a human-readable text report plus a JSON summary for dashboards.

## Features
- Recursively computes folder sizes (bytes and human-readable)
- Produces a ranked text report and a JSON file
- Simple CLI: provide a directory path, get instant insights
- Useful for finding disk hogs and automating cleanup tasks

## Output
- disk_usage_report_YYYY-MM-DD_HH-MM-SS.txt — readable report
- disk_usage_report_YYYY-MM-DD_HH-MM-SS.json — machine-readable summary

## Notes
- May take time on very large directories or network drives.
- Run with appropriate permissions to avoid denied-file errors.

Made by Paradox (shariq818)
