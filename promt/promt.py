# this code uses code part from view-source:https://www.translate.ru/перевод
from iso639 import Lang
import re

def collect(in_filename, link, exceptions={}):
  rows = []
  
  with open(in_filename, 'r', encoding="utf-8") as file:
    data = file.read()
    data = data.replace("zhcn", "zh")
  
  from_list = re.findall("value=\"(.+?)\"", data)
  to_list_of_list = re.findall("data-to-values=\"(.+?)\"", data)
  
  for i in range(len(from_list)):
    for to in to_list_of_list[i].split(' '):
      rows.append([link, Lang(from_list[i]).pt3, Lang(to).pt3])
  
  return rows