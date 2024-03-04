import sys, os, argparse
from properties import*

def writeLineTSV(w,l):
    w.write("\t".join(l)+"\n")

def handleFile(sort, fileToSort, fileDest, column=0, sortFunction=lambda x,y: x[0], reverse=False):
    with open(fileToSort, encoding="UTF-8") as f:
        lines = [x.split("\t") for x in f.read().strip().split("\n")]
    lines.sort(key=lambda row: sortFunction(row,column),reverse=reverse)
    with open(fileDest, "w") as w:
        if sort:
            for x in lines: writeLineTSV(w,x)
            return
        lineCounts = []
        curTotal = 0
        curStat = None
        for x in lines:
            if x[column] == curStat:
                curTotal += 1
            else:
                writeLineTSV(w,[x[0],str(curTotal)])
                curTotal = 1
                curStat = x[column]
        writeLineTSV(w,[x[0],str(curTotal)])

def main(parsedArgs):
    counted = parsedArgs.operation in ["c","count"]
    handleFile(not counted,
               parsedArgs.file,
               parsedArgs.dest if parsedArgs.dest != None else parsedArgs.file+f'.{["sorted","counted"][counted]}.tsv',
               parsedArgs.column,
               SORT_FUNCTIONS[parsedArgs.method],
               parsedArgs.reverse)

if __name__ == "__main__":
    parser = argparse.ArgumentParser("errorCounter")
    parser.add_argument("file",
                        help="File you wish to sort or count.")
    parser.add_argument("operation",
                        choices=["s","sort","c","count"],
                        help="Operation to carry out on the file.")
    parser.add_argument("column",
                        type=int,
                        help="Column to count or sort by.")
    parser.add_argument("-d", "--dest",
                        dest="dest",
                        nargs="?",
                        default=None,
                        help="File to write output to.")
    parser.add_argument("-m", "--method",
                        dest="method",
                        nargs="?",
                        choices=list(SORT_FUNCTIONS.keys()),
                        default="field",
                        help="Method of sorting.")
    parser.add_argument("-r", "--reverse",
                        dest="reverse",
                        action="store_true",
                        help="Reverse the method of sorting.")

    main(parser.parse_args())