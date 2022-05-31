# this code uses raw data from selector view-source:http://87.75.107.242/

from iso639 import Lang

def collect(in_filename, link, exceptions={}):
  rows = []
  with open(in_filename, 'r') as file:
    for line in file:
      dir = line.split("\"")[1].split("-")
      rows.append([link, Lang(dir[0]).pt3, Lang(dir[1]).pt3])
  return rows