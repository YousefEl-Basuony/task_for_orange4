import os

for root, dirs, files in os.walk(r"c:\Users\DELL\Desktop"):
    for file in files:
        if file.endswith((".zip", ".rar", ".tar.gz")):
            print(os.path.join(root, file))
