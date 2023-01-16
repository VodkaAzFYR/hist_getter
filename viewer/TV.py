import os
from pprint import pprint
from colorama import Fore

for file in os.listdir("Drop-here"):
    with open(rf".\Drop-here\{file}", "r", encoding="utf8") as f:
        file_str = f.read()
        file_list = eval(file_str)
    print(f"{file}:")
    for i in file_list:
        pprint(f"{i[1]} ==> {i[2]}")
    print("===============================================================================================================")
    print(Fore.RED + "===============================================================================================================")
    print(Fore.RESET + "===============================================================================================================")
    input()

