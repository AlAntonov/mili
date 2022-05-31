# this code uses list from https://yandex.com/support/translate/supported-langs.html
import re
from iso639 import Lang

def collect(in_filename, link, exceptions={}):
  rows = []
  
  skip_list = [
      'Emoji'
    ]
  
  all_languages = []
  with open(in_filename, 'r') as file:
    for line in file:
      name = line.strip()
      if len(name) == 0:
        continue
      if name in skip_list:
        continue
      if not name in exceptions:
        iso = Lang(name).pt3
      else:
        iso = Lang(exceptions[name]).pt3
      all_languages.append(iso)
      
  for i in all_languages:
    for j in all_languages:
      if i == j:
        continue
      rows.append([link, i, j])
    
  return rows