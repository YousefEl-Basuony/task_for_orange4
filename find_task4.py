import os

for root, dirs, files in os.walk(r"c:\Users\DELL\Desktop"):
    for file in files:
        if "task4" in file.lower() or "safety" in file.lower():
            print(os.path.join(root, file))
