# Error Analysis of French Morphological Inflection Generators

This project uses scripts designed to inflect lemmas based on morphosyntactic descriptions and aims to uncover patterns behind errors made my the various scripts made, in this case, when run on the French langauge. Our goal is to emphasize the role of high-quality training data, as well as recommend improved practices for scraping and collecting training data to be used for these tasks.

## Directories

The following are the folders found within the repository:

- **NeuralTransducerErrors**
Contains error files for neural transducer outputs. Example files include `errors.fra.dev.tsv.counted.tsv` for tracking counted errors. These files were created using scripts we authored independantly from the shared task files.

- **NeuralTransducerOutput**
Stores the output from the neural transducer. This includes files like `fra.decode.dev.tsv` and `fra.decode.test.tsv`. (LINK TO neural transducer repo and say it is the default output for the French after 800 epochs)

- **SegmentationsSplits**
Holds segmentation splits, such as `fra.segmentations`, as well as generates splits from '.segmentations' files. (LINK TO UNIMORPH REPO) 

- **SharedTaskData**
Includes data used for shared tasks, like development (`fra.dev`), training (`fra.trn`), and testing (`fra.tst`) splits.

- **src**
Source code directory containing scripts for various operations such as error analysis, data formatting, error counting, etc.

## Scripts Description

Below is a brief overview of the scripts located in the `src` directory:

### counterSorter.py: 

A script for counting and sorting errors. (MORE INFO NEEDED)

### formalNeuralErrors.py:

Analyzes formal errors in neural outputs. (MORE INFO NEEDED)

### formatSegmentations.py: 

Processes `.segmentations` files from UniMorph, matching them with original shared task splits. Supports `-l` for specific languages and `-a` for all languages. This script converts segmentation files into a `.total` format, aligning with morphosyntactic features and original data formats, and creates new train, dev, and test splits according to the shared task data.

### nonneural.py:

 Borrowed from the SIGMORPHON 2020 shared task, with tweaks in argument handling using the argparse module.

### nonneuralErrorFinder.py:

 Dedicated to finding errors in non-neural system outputs. (MORE INFO NEEDED)

### properties.py:

 Contains default paths and settings for the project. Note: comments might be helpful in describing contents.

## Using this repository

Instructions on how to run the scripts, options in terms of data manipulation, and the sequences of running the data, then sorting, then counting.

### Necessary Libraries and Tools

Libraries: sys, os, argparse, re, getopt, 
Other libraries/tools that are helpful in viewing/manipulating this data: ... (MORE INFO NEEDED)

```bash
# Example command to install prerequisites
pip install -r requirements.txt
