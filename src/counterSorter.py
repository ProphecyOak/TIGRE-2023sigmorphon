import sys, os, argparse
from properties import*

def writeLineTSV(w,l):
    #print(l)
    w.write("\t".join(l)+"\n")

def handleFile(sort, fileToSort, fileDest, column=0, sortFunction=lambda x,y: x[0], reverse=False, skip=0):
    with open(fileToSort, encoding="UTF-8") as f:
        lines = [x.split("\t") for x in f.read().strip().split("\n")[skip:]]
    lines.sort(key=lambda row: sortFunction(row,column),reverse=reverse)
    with open(fileDest, "w", encoding="UTF-8") as w:
        if sort:
            for x in lines: writeLineTSV(w,x)
            return
        curTotal = 0
        curStat = lines[0][column]
        for x in lines:
            if x[column] == curStat:
                curTotal += 1
            else:
                writeLineTSV(w,[curStat,str(curTotal)])
                curTotal = 1
                curStat = x[column]
        writeLineTSV(w,[curStat,str(curTotal)])

def main(parsedArgs):
    counted = parsedArgs.operation in ["c","count"]
    handleFile(not counted,
               parsedArgs.file,
               parsedArgs.dest if parsedArgs.dest != None else os.path.join(COUNTER_SORTER_OUTPUT_FOLDER,os.path.basename(parsedArgs.file)).replace(".tsv","")+f'.{["sorted","counted"][counted]}.tsv',
               parsedArgs.column,
               SORT_FUNCTIONS[parsedArgs.method],
               parsedArgs.reverse,
               parsedArgs.skip)

if __name__ == "__main__":
    parser = argparse.ArgumentParser("errorCounter")
    parser.add_argument("file",
                        help="File you wish to sort or count.")
    parser.add_argument("operation",
                        choices=["s","sort","c","count"],
                        help="Operation to carry out on the file.")
    parser.add_argument("-c","--column",
                        dest="column",
                        type=int,
                        default=0,
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
    parser.add_argument("-s", "--skip",
                        dest="skip",
                        type=int,
                        nargs="?",
                        default=0,
                        help="Skip first n lines of file")

    main(parser.parse_args())