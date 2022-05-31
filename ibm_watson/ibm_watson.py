# this code uses html data from language selector https://www.ibm.com/demos/live/watson-language-translator/self-service/home
import re
from iso639 import Lang

def collect(in_filename, link, exceptions={}):
  rows = []
  
  skip_list = [
    'Detect Language',
    'Chinese (Simplified)',
    'French (Canada)',
    'Basque',
    'Catalan'
    ]
  
  with open(in_filename, 'r') as file:
    str = file.read()
    
  start = [m.end() for m in re.finditer('"option">', str)]
  end = [m.start() for m in re.finditer('<svg', str)]
  
  all_languages = []
  for s, e in zip(start, end):
    name = str[s:e]
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
  
  # Basque and Catalan are supported only for translation to and from Spanish
  restricted_languages = ['eus', 'cat']
  for lang in  restricted_languages:
    rows.append([link, lang, 'spa'])
    rows.append([link, 'spa', lang])
    
  return rows