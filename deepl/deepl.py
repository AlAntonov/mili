# this code uses the list from the language selector at https://www.deepl.com/translator
from iso639 import Lang

def collect(in_filename, link, exceptions={}):
  rows = []
  
  all_languages = []
  with open(in_filename, 'r') as file:
    for line in file:
      name = line.strip()
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