import sys, os, argparse
from properties import*

def compareFile(file, test):
    with (open(file+".out", encoding="UTF-8") as f,
          open(file+f'.{["dev","tst"][test]}', encoding="UTF-8") as s,
          open(file+".errors", "w", encoding="UTF-8") as e):
        for x,y in zip(f.read().strip().split("\n"), s.read().strip().split("\n")):
            if x != y: e.write(x+"\n")

def main(parsedArgs):
    if parsedArgs.all:
        #Loop through languages like nonneural.py does
        print("This option is not yet implemented")
    else:
        compareFile(os.path.join(parsedArgs.path,parsedArgs.lang), parsedArgs.test)

if __name__ == "__main__":
    parser = argparse.ArgumentParser("nonneuralErrorFinder.py")
    parser.add_argument("-p","--path",
                        dest="path",
                        nargs="?",
                        default=SHARED_TASK_DATA_FOLDER,
                        help="Path to the .out file.")
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