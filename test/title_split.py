"""
    @ Title Split
    @ Author : Ministersky
    @ Date : 2022-07-18    
"""

from sre_parse import SPECIAL_CHARS


TARGET_FILE = "./title.txt"
OUT_FILE = "./result.txt"
splited_title = []
SPECIES_LIST = None


print("Split Start!")

def delete_Duplication(src:list) -> list:
   _set = set(src)
   _result = list(_set) 
   return _result

with open(TARGET_FILE,mode="r", encoding="utf-8") as f:
    lines = f.readlines()
    for i in lines:
        title = i.split(sep=" ")
        splited_title.append(title[0])
    SPECIES_LIST =  delete_Duplication(splited_title)
    
with open(OUT_FILE, "w", encoding="utf-8")as f:
    for i in SPECIES_LIST:
        f.write(i+"\n") 





