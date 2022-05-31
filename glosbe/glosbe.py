# this code uses language selector source code from view-source:https://translate.glosbe.com/en modified to json list manually
from iso639 import Lang
import json

def collect(in_filename, link, exceptions={}):
  rows = []
  
  with open(in_filename, 'r') as file:
    data = json.load(file)

  all_languages = [Lang(d["code"]).pt3 for d in data]
      
  for i in all_languages:
    for j in all_languages:
      if i == j:
        continue
      rows.append([link, i, j])
    
  return rows