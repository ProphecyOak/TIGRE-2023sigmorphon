#!/usr/bin/env python

import urllib.request
import io, os, argparse
import re
from tqdm import tqdm

LEMPG_DEFAULT = os.path.join('..', 'lemma_pages')
LANG_DEFAULT = os.path.join('..', 'unimorph_files')

def convert_char(c: str) -> str:
    cord = ord(c)-64
    d = max(0,ord(c)-16**2)//64
    pref = 16*12+3+d*2
    suf = cord-d*2*64
    
    return '%'+hex(pref)[-2:].upper()+'%'+hex(suf)[-2:].upper()

def encode_lemma(lem: str) -> str:
    encoded = ''
    for c in lem:
        if not c.isascii(): encoded += convert_char(c)
        elif c == ' ': encoded += '_'
        else: encoded += c

    return encoded

def get_lemmas(langpath: str = None, lemind: int = 0) -> set[str]:
    if not langpath: langpath = LANG_DEFAULT
    lem_set: set[str] = set()

    with open(langpath) as langfile:
        for line in langfile:
            if line != '\n' and line.strip().split('\t')[1] == 'V,NFIN':
                lem_set.add(line.strip().split('\t')[lemind])
    
    return lem_set

def get_lem_pages(pgpath: str = None) -> list[str]:
    if not pgpath: pgpath = LEMPG_DEFAULT
    return [os.path.splitext(f)[0] for f in os.listdir(pgpath)]

def get_lemma_langs(lem: str, lem_pgs: list[str], pgpath: str = None, target_lang: str = '', open_url: bool = True) -> list[str]:

    if not pgpath: pgpath = LEMPG_DEFAULT

    have_data_flag = True
    if lem not in lem_pgs and open_url:
        have_data_flag = False
        encoded_lem = encode_lemma(lem)

        try:
            lempg: io.BufferedIOBase = urllib.request.urlopen('https://en.wiktionary.org/wiki/'+encoded_lem)
            pgstr = lempg.read().decode('utf8')
            lempg.close()
        except:
            return ['URL Error']
    elif not open_url:
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

def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        'lang-stats',
        description='Run on a unimorph language file to look for incorrectly-scraped lemmas',
    )

    parser.add_argument('lang',
                        help='The name of the language to use, as written in English Wiktionary.')
    parser.add_argument('langfpath',
                        help='The path to the file containing language data')
    
    parser.add_argument('-w', '--wikt-path',
                        default=os.path.join('..','lemma_pages'),
                        help='Path to directory containing extracted wiktionary pages for the language.',
                        dest='wikt')
    parser.add_argument('-u', '--unim-path',
                        default=os.path.join('..', 'unimorph_files'),
                        help='Path to directory containing unimorph data',
                        dest='unim')
    parser.add_argument('-o', '--out-path',
                        default=os.path.join('..','unimorph_files', 'filtered'),
                        help='Path to the directory to write the output file to.',
                        dest='out')
    
    return parser.parse_args()

def main():
    args = get_args()
    LANG, LANGPATH, WIKT, UNIM, OUT = args.lang, args.langfpath, args.wikt, args.unim, args.out

    lemmas = sorted(get_lemmas(langpath=LANGPATH, lemind=0))
    lempgs = get_lem_pages(pgpath=os.path.join(WIKT, LANG))

    langsets: dict[str, set[str]] = {}

    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    
    outfile = open(os.path.join(OUT, f'{os.path.basename(LANGPATH)}.filtered'), 'w')

    for lem in tqdm(lemmas):
        langs = get_lemma_langs(lem, lempgs, pgpath=os.path.join(WIKT, LANG), target_lang=LANG, open_url=True)
        if LANG not in langs:
            for lang in langs:
                if not lang in langsets: langsets[lang] = set()
                langsets[lang].add(lem)
                outfile.write(lem+'\t'+lang+'\n')

    outfile.close()

    for altlang, lemset in langsets.items():
        print(f'{altlang}:\t{len(lemset)/len(lemmas):.1%}')

if __name__ == '__main__':
    main()