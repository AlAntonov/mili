# this code uses code part from view-source:https://gramtrans.com/
from iso639 import Lang
import re

def collect(in_filename, link, exceptions={}):
  rows = []
  
  with open(in_filename, 'r', encoding="utf-8") as file:
    data = file.read()
  
  dir_list = re.findall("value=\"(.+?)\"", data)
  
  skip_list = [
      'eng2qax'
    ]
    
  for dir in dir_list:
    if dir in skip_list:
      continue
    dir_split = dir.split("2")
    rows.append([link, Lang(dir_split[0]).pt3, Lang(dir_split[1]).pt3])
  
  return rows