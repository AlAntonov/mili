# raw data from https://www.microsoft.com/en-us/translator/languages/
import re
from iso639 import Lang

def collect(in_filename, link, exceptions={}):
  rows = []
  
  skip_list = [
    'Arabic (Levantine)',
    'Chinese (Literary)',
    'Chinese Simplified',
    'French (Canada)',
    'Inuktitut (Latin)',
    'Klingon (plqaD)',
    'Mongolian (Cyrillic)',
    'Portuguese (Brazil)',
    'Serbian (Cyrillic)'
    ]
  
  all_languages = []
  with open(in_filename, 'r') as file:
    for line in file:
      name = line.split('	')[0]
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