import sys
import re
import argparse
from properties import *

def sortOutErrors(test, language, outputFolder, dataFolder, errorFolder):
    fileToCheck = "test" if test else "dev"
    with open(f"{outputFolder}/{language}.decode.{fileToCheck}.tsv") as f:
        contents = f.read()

    lines = contents.strip().split("\n")
    columns = []
    for line in lines[1:]:
        columns.append(line.replace(" ","").split("\t"))

    errorColumns = list(filter(lambda x: x[3] != '0', columns))
    if fileToCheck == "test": fileToCheck = "tst"  #Because for whatever reason, neural_transducer doesnt use same extension formatting :/
    with (open(f"{dataFolder}/{language}.{fileToCheck}") as dat,
          open(f"{errorFolder}/errors.{language}.{fileToCheck}.tsv","w") as e,
          open(f"{errorFolder}/unexpectedForms.{language}.{fileToCheck}.tsv","w") as u):
        lemmaDict = {}
        e.write("lemma\t"+lines[0]+"\n")
        u.write(lines[0]+"\n")
        for form in dat.read().strip().split("\n"):
            splitForm = re.split(r"\s+",form)
            lemmaDict[splitForm[2]] = splitForm[0]
        reducedErrorColumns = []
        for line in errorColumns:
            try:
                line.insert(0,lemmaDict[line[1]])
                reducedErrorColumns.append(line)
            except:
                u.write("\t".join(line)+"\n")
        reducedErrorColumns.sort(key=lambda x: x[0])
        for line in reducedErrorColumns:
            if len(line) == 5: e.write("\t".join(line)+"\n")

def main(parsedArgs):
    if parsedArgs.all:
        #Loop through languages like nonneural.py does
        print("This option is not yet implemented")
    else:
        sortOutErrors(parsedArgs.test, parsedArgs.lang, parsedArgs.path, parsedArgs.original, parsedArgs.dest)

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
    parser.add_argument("-o","--original",
                        dest="original",
                        nargs="?",
                        default=SHARED_TASK_DATA_FOLDER,
                        help="Path to folder with original splits to grab lemmas from.")
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
