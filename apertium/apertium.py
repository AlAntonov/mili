# this code uses the part of the code from https://apertium.org/index.js?1621298492300

from iso639 import Lang
import json
from collections import defaultdict

def collect(in_filename, link, exceptions={}):
  dir_list = []
  with open(in_filename, 'r') as file:
    dir_list = json.load(file)  

  rows = []
  double = defaultdict(list)
  for dir in dir_list:
    srcLang = dir['sourceLanguage'][:3]
    tgtLang = dir['targetLanguage'][:3]
    # check for doubles after affix [:3] removement
    if (srcLang == tgtLang) or (srcLang in double and tgtLang in double[srcLang]):
      continue
    else:
      double[srcLang].append(tgtLang)
    rows.append([link, Lang(srcLang).pt3, Lang(tgtLang).pt3])
  return rows