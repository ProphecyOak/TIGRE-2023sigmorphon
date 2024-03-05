#!/usr/bin/env python

import urllib.request
import io, re, os
from tqdm import tqdm

LEMPG_DEFAULT = os.path.join('..', 'lemma_pages', 'French')
LANG_DEFAULT = os.path.join('..', 'SharedTaskData', 'fra.all')

def encode_lemma(lem: str) -> str:
    encodings = {
        'â': '%C3%A2', 'æ': '%C3%A6',
        'è': '%C3%A8', 'é': '%C3%A9', 'ê': '%C3%AA', 'ë': '%C3%AB',
        'ï': '%C3%AF', 'î': '%C3%AE',
        'ô': '%C3%B4', 'œ': '%C5%93',
        'û': '%C3%BB', 'ü': '%C3%BC',
        'ç': '%C3%A7'
    }

    encoded = ''
    for c in lem:
        if c in encodings: encoded += encodings[c]
        else: encoded += c

    return encoded

def get_lemmas(langpath: str = None) -> set[str]:
    if not langpath: langpath = LANG_DEFAULT
    lem_set: set[str] = set()

    with open(langpath) as langfile:
        for line in langfile:
            if line != '\n':
                lem_set.add(line.strip().split('\t')[0])
    
    return lem_set

def get_lem_pages(pgpath: str = None) -> list[str]:
    if not pgpath: pgpath = LEMPG_DEFAULT
    return [os.path.splitext(f)[0] for f in os.listdir(pgpath)]

def get_lemma_langs(lem: str, lem_pgs: list[str], pgpath: str = None, target_lang: str = '') -> list[str]:

    if not pgpath: pgpath = LEMPG_DEFAULT

    have_data_flag = True
    if lem not in lem_pgs:
        have_data_flag = False
        encoded_lem = encode_lemma(lem)

        try:
            lempg: io.BufferedIOBase = urllib.request.urlopen('https://en.wiktionary.org/wiki/'+encoded_lem)
            pgstr = lempg.read().decode('utf8')
            lempg.close()
        except:
            return ['URL Error']
    else:
        with open(os.path.join(pgpath, lem+'.html')) as lempg:
            pgstr = lempg.read()

    langs: list[str] = []
    headers = re.findall('<h2.*?>(.*?)</h2>', pgstr)
    for head in headers:
        if not have_data_flag:
            lang = re.search('>(.+?)<', head)
            if not lang: continue
            else: lang = lang[1]
        else:
            lang = head

        if target_lang in lang: langs.append(lang)

    return langs

def main():
    lemmas = sorted(get_lemmas())
    lempgs = get_lem_pages()

    midset, oldset, errset = set(), set(), set()

    oldfile, midfile, errfile = open('fra.old', 'w'), open('fra.mid', 'w'), open('fra.err', 'w')

    for lem in tqdm(lemmas):
        langs = get_lemma_langs(lem, lempgs, target_lang='French')
        if 'Middle French' in langs:
            midset.add(lem)
            midfile.write(lem+'\n')
        if 'Old French' in langs:
            oldset.add(lem)
            oldfile.write(lem+'\n')
        if 'URL Error' in langs:
            errset.add(lem)
            errfile.write(lem+'\n')
    
    oldfile.close()
    midfile.close()
    errfile.close()

    histportion = len(midset.union(oldset))/len(lemmas)
    mportion, oportion = len(midset)/len(lemmas), len(oldset)/len(lemmas)

    errs = len(errset)
    print(f'fra stats:\nportion historical: {histportion:.1%}\nportion middle: {mportion:.1%}\nportion old: {oportion:.1%}\nmissing pages: {errs}')

if __name__ == '__main__':
    main()