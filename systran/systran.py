# this code uses https://api-translate.systran.net/translation/supportedLanguages from browser->devTools->Network
from iso639 import Lang
import json

def collect(in_filename, link, exceptions={}):
  rows = []
  
  with open(in_filename, 'r') as file:
    data = json.load(file)
      
  for dir in data["languagePairs"]:
    rows.append([link, Lang(dir["source"][:2]).pt3, Lang(dir["target"][:2]).pt3])
    
  return rows