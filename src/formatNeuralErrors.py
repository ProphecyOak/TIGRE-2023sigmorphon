import sys
import re
import argparse
from properties import *

def sortOutErrors(test, language, outputFolder, errorFolder):
    fileToCheck = "test" if test else "dev"
    with open(f"{outputFolder}/{language}.decode.{fileToCheck}.tsv") as f:
        contents = f.read()

    lines = contents.strip().split("\n")
    rows = []
    for line in lines[1:]:
        rows.append(line.replace(" ","").split("\t"))

    with open(f"{errorFolder}/errors.{language}.{fileToCheck}.tsv","w") as e:
          for row in rows: e.write("\t".join(row)+"\n")

def main(parsedArgs):
    if parsedArgs.all:
        #Loop through languages like nonneural.py does
        print("This option is not yet implemented")
    else:
        sortOutErrors(parsedArgs.test, parsedArgs.lang, parsedArgs.path, parsedArgs.dest)

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
                        default=NEURAL_ERRORS_FOLDER,
                        help="Path to destination folder for error catalog.")
    parser.add_argument("-t","--test",
                        dest="test",
                        action="store_true",
                        help="Uses the .tst split instead of the .dev split.")
    langGroup = parser.add_mutually_exclusive_group()
    langGroup.add_argument("-l","--lang",
                        dest="lang",
                        nargs="?",
                        default="fra",
                        help="Language to generate splits from.")
    langGroup.add_argument("-a","--all",
                        dest="all",
                        action="store_true",
                        help="Not yet implemented: Runs on all languages found in the segmentations folder.")
    main(parser.parse_args())
