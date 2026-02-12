import os

repo_path = "."

files = [f for f in os.listdir(repo_path) if f.endswith(('.java', '.py', '.cpp', '.js'))]

files.sort()

content = "# 📘 DSA Daily Progress\n\n"
content += f"Total Problems Solved: {len(files)}\n\n"
content += "## 📂 Solved Problems List\n\n"

for file in files:
    content += f"- {file}\n"

with open("README.md", "w", encoding="utf-8") as readme:
    readme.write(content)

print("README updated successfully!")
