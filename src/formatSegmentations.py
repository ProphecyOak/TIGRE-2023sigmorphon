import sys
import os

def splitRow(row):
    tabSplitRow = row.split("\t")
    if tabSplitRow[2][-4:] == "NFIN": return None
    return f"{tabSplitRow[0]}\t{tabSplitRow[2].replace("V|V","V").replace("|",";")}\t{tabSplitRow[1]}"

def convertFile(lang="fra"):
    with open(f"../SegmentationsSplits/{lang}.segmentations", encoding="UTF-8") as f:
        segmentations = f.read()
    segmentationRows = segmentations.strip().split("\n")
    splitSegmentationRows = list(map(splitRow, segmentationRows))
    
    with open(f"../SegmentationsSplits/{lang}.total", "w", encoding="UTF-8") as dest:
        for row in splitSegmentationRows:
            if row != None: dest.write(row+"\n")

def generateSplit(lang="fra"):
    with open(f"../SharedTaskData/{lang}.trn", encoding="UTF-8") as trn:
        trnSet = set([y[0] for y in [x.split("\t") for x in trn.read().strip().split("\n")]])
    with open(f"../SharedTaskData/{lang}.dev", encoding="UTF-8") as dev:
        devSet = set([y[0] for y in [x.split("\t") for x in dev.read().strip().split("\n")]])
    with open(f"../SharedTaskData/{lang}.tst", encoding="UTF-8") as tst:
        tstSet = set([y[0] for y in [x.split("\t") for x in tst.read().strip().split("\n")]])

    with open(f"../SegmentationsSplits/{lang}.total", encoding="UTF-8") as tot, open(f"../SegmentationsSplits/{lang}.trn", "w", encoding="UTF-8") as trn, open(f"../SegmentationsSplits/{lang}.dev", "w", encoding="UTF-8") as dev, open(f"../SegmentationsSplits/{lang}.tst", "w", encoding="UTF-8") as tst:
        for x in tot.read().strip().split("\n"):
            lemma = x.split("\t")[0]
            if lemma in trnSet: trn.write(x+"\n")
            if lemma in devSet: dev.write(x+"\n")
            if lemma in tstSet: tst.write(x+"\n")

if __name__ == "__main__":
    convertFile()
    generateSplit()