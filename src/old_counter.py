#!/usr/bin/env python

import os

FILTER_DEFAULT = os.path.join('..', 'SharedTaskData', 'other', 'fr')

def get_historical(fpath: str = FILTER_DEFAULT) -> list[str]:

    with open(fpath) as histfile:
        histlems: set[str] = set()
        for line in histfile:
            splitline = line.strip().split('\t')
            if line != '\n' and splitline[1] != 'URL Error': histlems.add(splitline[0])

    return histlems

def count_file(histlems: set[str], fpath: str, lemind: int = 0) -> tuple[int, int]:
    with open(fpath) as file:
        flines = [line.strip().split('\t') for line in file if line != '\n']

    lems = {line[lemind] for line in flines}

    return [line for line in flines if line[lemind] in histlems], flines, [lem for lem in lems if lem in histlems], lems

def main():
    data_path = os.path.join('..', 'SharedTaskData', 'other')

    histlems = get_historical()

    for dpath, _, fnames in os.walk(data_path):
        for fname in fnames:
            fpath = os.path.join(dpath, fname)
            histform, totform, histlem, totlem = count_file(histlems, fpath, lemind=1)
            print(f'file: {fpath}\nhistorical forms: {len(histform)}\ttotal forms: {len(totform)}\tproportion: {len(histform)/len(totform):.1%}')
            print(f'historical lemmas: {len(histlem)}\ttotal lemmas: {len(totlem)}\tproportion: {len(histlem)/len(totlem):.1%}\n')

if __name__ == '__main__':
    main()