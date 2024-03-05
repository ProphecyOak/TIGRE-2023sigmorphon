# Error Analysis of French Morphological Inflection Generators

This project uses scripts designed to inflect lemmas based on morphosyntactic descriptions and aims to uncover patterns behind errors made my the various scripts made, in this case, when run on the French langauge. Our goal is to emphasize the role of high-quality training data, as well as recommend improved practices for scraping and collecting training data to be used for these tasks.

## Data and scripts

The following are the folders found within the repository:

### NeuralTransducerErrors
Contains error files for neural transducer outputs. Example files include `errors.fra.dev.tsv.counted.tsv` for tracking counted errors.

### NeuralTransducerOutput
Stores the output from the neural transducer. This includes files like `fra.decode.dev.tsv` and `fra.decode.test.tsv`. Note: maybe renaming "test" to "tst" for consistency.

### SegmentationsSplits
Holds segmentation splits, such as `fra.segmentations`.

### SharedTaskData
Includes data used for shared tasks, like development (`fra.dev`), training (`fra.trn`), and testing (`fra.tst`) splits.

### src
Source code directory containing scripts for various operations such as error analysis, data formatting, error counting, etc.

#### Scripts Description

Below is a brief overview of the scripts located in the `src` directory:

- **counterSorter.py**: A script for counting and sorting errors. (more info needed)
- **formalNeuralErrors.py**: Analyzes formal errors in neural outputs. (more info needed)
- **formatSegmentations.py**: Processes `.segmentations` files from UniMorph, matching them with original shared task splits. Supports `-l` for specific languages and `-a` for all languages. This script converts segmentation files into a `.total` format, aligning with morphosyntactic features and original data formats, and creates new train, dev, and test splits according to the shared task data.
- **nonneural.py**: Borrowed from the SIGMORPHON 2020 shared task, with tweaks in argument handling using the argparse module.
- **nonneuralErrorFinder.py**: Dedicated to finding errors in non-neural system outputs. (more info needed)
- **properties.py**: Contains default paths and settings for the project. Note: comments might be helpful in describing contents.

## Using this repository

Instructions on how to run the scripts, options in terms of data manipulation, and the sequences of running the data, then sorting, then counting.

### Necessary Libraries and Tools

Libraries: sys, os, argparse, re, getopt, 
Other libraries/tools that are helpful in viewing/manipulating this data: ...

```bash
# Example command to install prerequisites
pip install -r requirements.txt
