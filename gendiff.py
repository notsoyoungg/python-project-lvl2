#!/usr/bin/env python
import argparse
import json
import os.path

parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f', '--format', help='set format of output')
args = parser.parse_args()

readed = json.load(open(os.path.abspath(args.first_file)))
readed2 = json.load(open(os.path.abspath(args.second_file)))
#print(readed['host'])

def sort_dict(dict_):
      sorted_tuple = sorted(dict_.items(), key=lambda x: x[0])
      sorted_dict = dict(sorted_tuple)
      return sorted_dict

def generate_diff(dict1, dict2):
  for key in sort_dict(dict1):
      if key in dict2 and dict1[key] == dict2[key]:
          print(f'  {key}: {dict1[key]}')
      if key not in dict2:
          print(f'- {key}: {dict1[key]}')
      if key in dict2 and dict1[key] != dict2[key]:
          print(f'- {key}: {dict1[key]}')
          print(f'+ {key}: {dict2[key]}')
  for key in sort_dict(dict2):
      if key not in dict1:
         print(f'+ {key}: {dict2[key]}') 

def main():
    generate_diff(readed, readed2)
    print(args.first_file)


if __name__ == '__main__':
    main()