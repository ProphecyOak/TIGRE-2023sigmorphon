import os, sys, argparse
from properties import*


def main(parsedArgs):
    resultsByForm = {}
    resultsByFeatures = {}
    headers = ["lemma","features","gold"]

    ### Grabs lemmas from split file
    with open(parsedArgs.split, encoding="UTF-8") as s:
        for line in [x.split("\t") for x in s.read().strip().split("\n")]:
            resultsByForm[line[2]] = line
            resultsByFeatures[(line[0],line[1])] = line

    ### Grabs target values from supplied files.
    numRelevantColumns = 3
    for fileI in range(0,len(parsedArgs.files)//(numRelevantColumns+1)+numRelevantColumns,numRelevantColumns+1):
        lemmaColumn, targetColumn, predictedColumn = int(parsedArgs.files[fileI+1]), int(parsedArgs.files[fileI+2]), int(parsedArgs.files[fileI+3])
        headers.append(os.path.basename(parsedArgs.files[fileI]))
        with open(parsedArgs.files[fileI],encoding="UTF-8") as f:
            print(parsedArgs.files[fileI])
            rows = [x.split("\t") for x in f.read().strip().split("\n")]
        for row in rows:
            if row[predictedColumn] == "craqueles": print(row)
            if row[targetColumn] in resultsByForm.keys():
                ### Adds row based on the target form
                resultsByForm[row[targetColumn]].append(row[predictedColumn])
            elif (row[lemmaColumn], row[targetColumn]) in resultsByFeatures.keys():
                ### Adds row based on the features and lemma
                resultsByFeatures[(row[lemmaColumn], row[targetColumn])].append(row[predictedColumn])
            else: print(row)
        
    ### Writes all of the rows to the output file
    with open(parsedArgs.output, "w", encoding="UTF-8")  as w:
        w.write("\t".join([str(x) for x in headers])+"\n")
        for row in resultsByForm.values():
            if len(row) > 3: w.write("\t".join([str(x) for x in row])+"\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser("errorSummation.py")
    parser.add_argument("files",
                        nargs="+",
                        default=[],
                        help="Files to aggregate errors from.")
    parser.add_argument("-s","--split",
                        dest="split",
                        nargs="?",
                        default=os.path.join(SHARED_TASK_DATA_FOLDER,"fra.dev"),
                        help="split to draw rows from.")
    parser.add_argument("-lc","--lemmaColumn",
                        dest="lemmaColumn",
                        type=int,
                        nargs="?",
                        default=0,
                        help="Column in split with lemmas.")
    parser.add_argument("-fc","--featureColumn",
                        dest="featureColumn",
                        type=int,
                        nargs="?",
                        default=1,
                        help="Column in split with features.")
    parser.add_argument("-o","--output",
                        dest="output",
                        nargs="?",
                        default="../CounterSorterOutput/summedErrors.tsv",
                        help="Output file.")
    main(parser.parse_args())