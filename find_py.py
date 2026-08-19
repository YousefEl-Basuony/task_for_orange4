import os

for root, dirs, files in os.walk(r"c:\Users\DELL\Desktop"):
    for file in files:
        if file in ["config.py", "ingest.py"]:
            print(os.path.join(root, file))
