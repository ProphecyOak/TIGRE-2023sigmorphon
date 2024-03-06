import os, sys, argparse
from properties import*


def main(parsedArgs):
    resultsByForm = []
    headers = ["lemma","features","gold"]

    ### Grabs lemmas from split file
    with open(parsedArgs.split, encoding="UTF-8") as s:
        for line in [x.split("\t") for x in s.read().strip().split("\n")]:
            resultsByForm.append(line)

    ### Grabs target values from supplied files.
    for fileI in range(0,len(parsedArgs.files)//4+3,4):
        targetColumn, predictedColumn, headerSkip = int(parsedArgs.files[fileI+1]), int(parsedArgs.files[fileI+2]), int(parsedArgs.files[fileI+3])
        headers.append(os.path.basename(parsedArgs.files[fileI]))
        with open(parsedArgs.files[fileI],encoding="UTF-8") as f:
            print(parsedArgs.files[fileI])
            rows = [x.split("\t") for x in f.read().strip().split("\n")][headerSkip:]
        for row,resultRow in zip(rows,resultsByForm):
            resultRow.append(row[predictedColumn] if row[predictedColumn] not in [resultRow[1],resultRow[2]] else "")
        
    ### Writes all of the rows to the output file
    with open(parsedArgs.output, "w", encoding="UTF-8")  as w:
        w.write("\t".join([str(x) for x in headers])+"\n")
        for row in resultsByForm:
            if not parsedArgs.includeCorrect:
                rowCheck = list(filter("".__ne__, row))
                if len(rowCheck) > 3: w.write("\t".join([str(x) for x in row])+"\n")
            else:
                w.write("\t".join([str(x) for x in row])+"\n")

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
    parser.add_argument("-o","--output",
                        dest="output",
                        nargs="?",
                        default="../CounterSorterOutput/summedErrors.tsv",
                        help="Output file.")
    parser.add_argument("-c","--correct",
                        dest="includeCorrect",
                        action="store_true",
                        help="Includes correct rows as well.")
    main(parser.parse_args())