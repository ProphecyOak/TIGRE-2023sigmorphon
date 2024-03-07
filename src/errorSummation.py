import os, sys, argparse
from properties import*


def main(parsedArgs):
    headers = ["lemma","features","gold"] + parsedArgs.headerNames
    if not parsedArgs.addingsSums:
        resultsByForm = []
        ### Grabs lemmas from split file
        with open(parsedArgs.split, encoding="UTF-8") as s:
            for line in [x.split("\t") for x in s.read().strip().split("\n")]:
                resultsByForm.append(line)

        ### Grabs target values from supplied files.
        for fileI in range(0,len(parsedArgs.files)//3+2,3):
            print(parsedArgs.files[fileI])
            predictedColumn, headerSkip = int(parsedArgs.files[fileI+1]), int(parsedArgs.files[fileI+2])
            if len(headers) <= 3 + fileI//3:
                headers.append(os.path.basename(parsedArgs.files[fileI]))
            with open(parsedArgs.files[fileI],encoding="UTF-8") as f:
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
    else:
        resultsByForm = {}
        filesPassed = 0
        for file in parsedArgs.files:
            with open(file) as f:
                rows = [x.split("\t") for x in f.read().strip().split("\n")]
            headers += rows[0][3:]
            for row in rows[1:]:
                form = tuple(row[:3])
                if form in resultsByForm.keys(): resultsByForm[form] = resultsByForm[form] + row[3:]
                else: resultsByForm[form] = ["" for x in range(filesPassed)] + row[3:]
            filesPassed += len(headers[3:])
        with open(parsedArgs.output, "w", encoding="UTF-8") as w:
            w.write("\t".join([str(x) for x in headers])+"\n")
            for form, line in resultsByForm.items():
                w.write("\t".join(list(form)+line)+"\n")

if __name__ == "__main__":
    print("Summing:")
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
    parser.add_argument("-e","--errors",
                        dest="addingsSums",
                        action="store_true",
                        help="Adds summedErrors together.")
    parser.add_argument("-n","--names",
                        dest="headerNames",
                        nargs="+",
                        default=[],
                        help="Header Names associated with the files.")
    main(parser.parse_args())
    print()