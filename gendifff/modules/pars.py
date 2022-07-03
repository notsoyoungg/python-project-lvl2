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
