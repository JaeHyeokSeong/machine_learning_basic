# import glob
#
# folders = glob.glob("/Users/jaehyeokseong/Desktop/*")
# for folder in folders:
#     print(folder)

# import os

# print(os.getcwd())
#
# folder = "sampel_dir"
#
# if os.path.exists(folder):
#     print("already exist")
#     os.rmdir(folder)
#     print(f"deleted {folder}")
# else:
#     os.makedirs(folder)
#     print(f"created {folder} folder")

# print(os.listdir())

import time

print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))
