import os
for root, dirs, files in os.walk(r"c:\Users\DELL\Desktop\medical-system"):
    for file in files:
        if file.endswith(".ipynb"):
            print(os.path.join(root, file))
