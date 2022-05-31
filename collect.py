from iso639 import Lang
import csv
import os
import json
import importlib

def collect_langs(langs, link):
  rows = []
  for i in langs:
    for j in langs:
      if i == j:
        continue
      rows.append([link, i, j])
  return rows
  
def collect_dirs(directions, link, revert_directions):
  rows = []
  for dir in directions:
    rows.append([link, dir["from"], dir["to"]])
    if revert_directions:
      rows.append([link, dir["to"], dir["from"]])
  return rows  
    
if __name__ == '__main__':
  languages = []
  current_directory = os.getcwd()
  tsv_filename = os.path.join(current_directory, 'mili.tsv')
  print(tsv_filename)
  
  exceptions_filename = os.path.join(current_directory, 'exceptions.json')  
  with open(exceptions_filename, 'r', encoding='utf-8') as exceptfile:
    exceptions = json.load(exceptfile)
  
  with open(tsv_filename, 'w', newline='') as tsvfile:
    writer = csv.writer(tsvfile, delimiter='\t')
    
    for x in os.walk(current_directory):
      filenames = (f for f in x[2] if '.json' in f and 'exceptions' not in f)
      for filename in filenames:
        with open(os.path.join(x[0], filename), 'r') as file:
          data = json.load(file)

        system = filename.replace('.json', '')
        print(system)

        if "directions" in data:
          revert_directions = "revert_directions" in data and data["revert_directions"]
          all_dir = collect_dirs(data["directions"], data["link"], revert_directions)
        elif "languages" in data:
          all_dir = collect_langs(data["languages"], data["link"])
        else: # if "custom" in data
          impr = importlib.import_module(system + "." + system)
          raw_filename = system + '.raw'
          all_dir = impr.collect(os.path.join(x[0], raw_filename), data["link"], exceptions)        
        
        for dir in all_dir:
          writer.writerow(dir)
          languages.append(dir[1])
          languages.append(dir[2])
        
  languages = sorted(list(set(languages)))
  print(languages)
  print("Totally %d languages" % len(languages))