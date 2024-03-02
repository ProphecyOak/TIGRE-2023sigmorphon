import sys
import os
import argparse
from properties import *

def splitRow(row):
    tabSplitRow = row.split("\t")
    if tabSplitRow[2][-4:] == "NFIN": return None
    return f"{tabSplitRow[0]}\t{tabSplitRow[2].replace("V|V","V").replace("|",";")}\t{tabSplitRow[1]}"

def convertFile(lang,segmentationsFolder):
    if f"{lang}.total" not in os.listdir(SEGMENTATIONS_FOLDER):
        print("Generating {lang}.total")
        with open(f"{segmentationsFolder}/{lang}.segmentations", encoding="UTF-8") as f:
            segmentations = f.read()
        segmentationRows = segmentations.strip().split("\n")
        splitSegmentationRows = list(map(splitRow, segmentationRows))
        
        with open(f"{segmentationsFolder}/{lang}.total", "w", encoding="UTF-8") as dest:
            for row in splitSegmentationRows:
                if row != None: dest.write(row+"\n")

def generateSplit(lang, segmentationsFolder, splitsFolder):
    print(f"Generating {lang}.trn, {lang}.dev, and {lang}.tst")
    with open(f"{splitsFolder}/{lang}.trn", encoding="UTF-8") as trn:
        trnSet = set([y[0] for y in [x.split("\t") for x in trn.read().strip().split("\n")]])
    with open(f"{splitsFolder}/{lang}.dev", encoding="UTF-8") as dev:
        devSet = set([y[0] for y in [x.split("\t") for x in dev.read().strip().split("\n")]])
    with open(f"{splitsFolder}/{lang}.tst", encoding="UTF-8") as tst:
        tstSet = set([y[0] for y in [x.split("\t") for x in tst.read().strip().split("\n")]])

    with open(f"{segmentationsFolder}/{lang}.total", encoding="UTF-8") as tot, open(f"{segmentationsFolder}/{lang}.trn", "w", encoding="UTF-8") as trn, open(f"{segmentationsFolder}/{lang}.dev", "w", encoding="UTF-8") as dev, open(f"{segmentationsFolder}/{lang}.tst", "w", encoding="UTF-8") as tst:
        for x in tot.read().strip().split("\n"):
            lemma = x.split("\t")[0]
            if lemma in trnSet: trn.write(x+"\n")
            if lemma in devSet: dev.write(x+"\n")
            if lemma in tstSet: tst.write(x+"\n")

def main(parsedArgs):
    if parsedArgs.all:
        #Loop through languages like nonneural.py does
        print("This option is not yet implemented")
    else:
        convertFile(parsedArgs.lang, parsedArgs.path)
        generateSplit(parsedArgs.lang, parsedArgs.path, parsedArgs.original)

if __name__ == "__main__":
    parser = argparse.ArgumentParser("formatSegmentations.py")
    parser.add_argument("-p","--path",
                        dest="path",
                        nargs="?",
                        default=SEGMENTATIONS_FOLDER,
                        help="Path to folder with the .segmentations file.")
    parser.add_argument("-o","--original",
                        dest="original",
                        nargs="?",
                        default=SHARED_TASK_DATA_FOLDER,
                        help="Path to folder with original splits to model off of.")
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