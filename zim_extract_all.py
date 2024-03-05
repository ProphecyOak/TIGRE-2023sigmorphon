# -*- coding: utf-8 -*-
import codecs
import re
import os
import argparse
from collections import Counter
from zimply.zimply import ZIMFile

# gather arguments
parser = argparse.ArgumentParser(
    description="Extract per-language lemma list from zim file."
)
parser.add_argument(
    "-zimfile", action="store", dest="zimfile", help="Location of ZIM file."
)
parser.add_argument(
    "-langfile", action="store", dest="langfile", help="List of languages."
)
args = parser.parse_args()


# load the zimfile
zimfile = ZIMFile(args.zimfile, "utf-8")

# load the languages
with codecs.open(args.langfile, "rb", "utf-8") as f:
    languages = [line.strip() for line in f]

# create directories to store results
for language in languages:
    if not os.path.exists("./lemma_pages/" + language):
        os.makedirs("./lemma_pages/" + language)

count = 0
cclust = 0
cblob = 0
OK = True
while OK:
    try:
        data = zimfile._read_blob(cclust, cblob)
        count += 1
        try:
            body = data.decode("utf-8")

            for language in languages:
                if (
                    language + u"</h2>" in body
                    and u"Verb</h3>" in body
                ):
                    lemmatch = re.search('class="Latn headword".*?>(.*?)<', body)
                    if lemmatch:
                        lemma = lemmatch[1]
                        outf = codecs.open(
                            "./lemma_pages/"
                            + language
                            + "/" + lemma + ".html",
                            "wb",
                            encoding="utf-8",
                        )
                    outf.write(body)
                    outf.close()
                    # update id
                count += 1
        except:
            print("BAD DATA", count)
        cblob += 1  # Update blob
    except IOError:
        cblob = 0  # reset blob
        cclust += 1  # update cluster
        if cclust >= zimfile.header_fields["clusterCount"]:  # no such cluster anymore
            OK = False
