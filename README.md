# Error Analysis of French Morphological Inflection Generators

This project uses scripts designed to inflect lemmas based on morphosyntactic descriptions and aims to uncover patterns behind errors made my the various scripts made, in this case, when run on the French langauge. Our goal is to emphasize the role of high-quality training data, as well as recommend improved practices for scraping and collecting training data to be used for these tasks.

## Directories

The following are the folders found within the repository:

- `NeuralTransducerErrors`
Contains error files for neural transducer outputs. Example files include `errors.fra.dev.tsv.counted.tsv` for tracking counted errors. These files were created using scripts we authored independantly from the shared task files.

- `NeuralTransducerOutput`
Stores the output from the neural transducer. This includes files like `fra.decode.dev.tsv` and `fra.decode.test.tsv`. (LINK TO neural transducer repo and say it is the default output for the French after 800 epochs)

- `SegmentationsSplits`
Holds segmentation splits, such as `fra.segmentations`, as well as generates splits from '.segmentations' files. (LINK TO UNIMORPH REPO) 

- `SharedTaskData`
Includes data used for shared tasks, like development (`fra.dev`), training (`fra.trn`), and testing (`fra.tst`) splits.

- `src`
Source code directory containing scripts for various operations such as error analysis, data formatting, error counting, etc.

## Scripts Description

Below is an overview of the scripts located in the `src` directory:
- [counterSorter.py](#counterSorter)
- [formatNeuralErrors.py](#formatNeuralErrors)

<a name="counterSorter"></a>
<details><summary>counterSorter.py</summary>
 
 >For a given file, either counts or sorts it and places the output in `CounterSorterOutput` by default.
 >- If you are sorting, include an `s` or the word `sort` after the specified file.
 >- If you are counting, include a `c` or the word `count` after the specified file.
 >
 >For either option, you may:
 >- Specify a designated output file using the `-d` or `--dest` flag.
 >- Specify a sorting function using the `-m` or `--method` flag and a key from the `SORT_FUNCTIONS` dictionary in `properties.py`.
 >- Invert the sort direction using the `-r` or `--reverse` flag.
 >- Ignore the header of the file using the `-s` or `--skip` flag and a number of lines to skip.

</details>

<a name="formatNeuralErrors"></a>
<details><summary>formatNeuralErrors.py</summary>
 
 > Analyzes formal errors in neural outputs. (MORE INFO NEEDED)
</details>


<a name="formatSegmentations"></a>
<details><summary>formatSegmentations.py</summary>
 
 > Processes `.segmentations` files from UniMorph, matching them with original shared task splits. Supports `-l` for specific languages and `-a` for all languages. This script converts segmentation files into a `.total` format, aligning with morphosyntactic features and original data formats, and creates new train, dev, and test splits according to the shared task data.
</details>

<a name="nonneural"></a>
<details><summary>nonneural.py</summary>
 
 > Borrowed from the SIGMORPHON 2020 shared task, with tweaks in argument handling using the argparse module.
</details>

<a name="nonneuralErrorFinder"></a>
<details><summary>nonneuralErrorFinder.py</summary>
 
 > Dedicated to finding errors in non-neural system outputs. (MORE INFO NEEDED)
</details>

<a name="properties"></a>
<details><summary>properties.py</summary>
 
 > Contains default paths and settings for the project. Note: comments might be helpful in describing contents.
</details>

## Using this repository

Instructions on how to run the scripts, options in terms of data manipulation, and the sequences of running the data, then sorting, then counting.

### Necessary Libraries and Tools

Libraries: sys, os, argparse, re, getopt, 
Other libraries/tools that are helpful in viewing/manipulating this data: (MORE INFO NEEDED)

```bash
# Example command to install prerequisites
pip install -r requirements.txt
