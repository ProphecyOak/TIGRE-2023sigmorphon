import sys, os
import re
import argparse
from properties import *

def sortOutErrors(filepath, errorFolder):
    with open(filepath) as f:
        contents = f.read()

    lines = contents.strip().split("\n")
    rows = []
    for line in lines[1:]:
        rows.append(line.replace(" ","").split("\t"))

    with open(f"{errorFolder}/{os.path.basename(filepath)}","w") as e:
          for row in rows: e.write("\t".join(row)+"\n")

def main(parsedArgs):
    for file in os.listdir(parsedArgs.path):
        sortOutErrors(os.path.join(parsedArgs.path,file), parsedArgs.dest)

if __name__ == "__main__":
    parser = argparse.ArgumentParser("catalogNeuralErrors.py")
    parser.add_argument("-p","--path",
                        dest="path",
                        nargs="?",
                        default=NEURAL_OUTPUT_FOLDER,
                        help="Path to folder with the neuraltransducer output files.")
    parser.add_argument("-d","--dest",
                        dest="dest",
                        nargs="?",
                        default=NEURAL_FORMATTED_FOLDER,
                        help="Path to destination folder for error catalog.")
    main(parser.parse_args())
