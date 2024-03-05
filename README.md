# Error Analysis of French Morphological Inflection Generators

One Paragraph of project description goes here. This should give a quick overview of what the project does and its target audience.

## The Zip

Briefly describe the main components of your project and how they interact. Below is an outline based on the information you've provided:

### NeuralTransducerErrors
Contains error files for neural transducer outputs. Example files include `errors.fra.dev.tsv.counted.tsv` for tracking counted errors.

### NeuralTransducerOutput
Stores the output from the neural transducer. This includes files like `fra.decode.dev.tsv` and `fra.decode.test.tsv`. Note: maybe renaming "test" to "tst" for consistency.

### SegmentationsSplits
Holds segmentation splits, such as `fra.segmentations`, indicating how data is segmented.

### SharedTaskData
Includes data used for shared tasks, like development (`fra.dev`), training (`fra.trn`), and testing (`fra.tst`) splits.

### src
Source code directory containing scripts for various operations such as error analysis, data formatting, error counting, etc.

#### Scripts Description

Here’s a brief overview of the scripts located in the `src` directory:

- **counterSorter.py**: A script for counting and sorting errors. Further details needed.
- **formalNeuralErrors.py**: Analyzes formal errors in neural outputs. More information required.
- **formatSegmentations.py**: Processes `.segmentations` files from UniMorph, matching them with original shared task splits. Supports `-l` for specific languages and `-a` for all languages. This script converts segmentation files into a `.total` format, aligning with morphosyntactic features and original data formats, and creates new train, dev, and test splits according to the shared task data.
- **nonneural.py**: Borrowed from the SIGMORPHON 2020 shared task, with tweaks in argument handling using the argparse module. It's used for non-neural processing tasks.
- **nonneuralErrorFinder.py**: Dedicated to finding errors in non-neural system outputs. Further explanation needed.
- **properties.py**: Contains default paths and settings for the project. It's advisable to add comments for better clarity on folder usage.

## Using this repository

Include instructions here on how to set up and run your project, including installing any prerequisites, setting up a virtual environment, and running the scripts. Be as detailed as possible to ensure a smooth setup process for new users.

### Necessary Libraries and Tools

Libraries: sys, os, argparse, re, getopt, 
List any required libraries, tools, or frameworks that need to be installed before running the project.

```bash
# Example command to install prerequisites
pip install -r requirements.txt
