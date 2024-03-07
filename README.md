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

<details><summary><code>errorSummation.py</code></summary>
 
 >Takes a set of output files and merges them together by form. Make sure that both files have all the same forms in the same order. You must list a number for the index for the column with the predicted form and the number of lines to skip for a header following each file. You may:
 >- Specify the split to check your words against using the `-s` or `--split` flag.
 >- Specify the output file using the `-o` or `--output` flag.
 >- Include the universally correct forms in the results using the `-c` or `--correct` flag.
</details>

<details><summary><code>formatNeuralErrors.py</code></summary>
 
 >Takes the output files placed in `NeuralTransducerOutput` and converts them to a format that is more human readable and is usable for `errorSummation.py` and places the new file into the `NeuralTransducerFormatted` folder. You may:
 >- Specify a designated input directory using the `-p` or `--path` flag.
 >- Specify a designated output directory using the `-d` or `--dest` flag.
 >- Specify whether the outputs from the `.tst` splits instead of the `.dev` splits using the `-t` or `--test` flag.
 >
 >And either: 
 >- Specify a language to convert using the `-l` or `--lang` flag with the UniMorph abbreviation.
 >- ~~Run all files using the `-a` or `--all` flag.~~ \[Not Yet Implemented\]
</details>

<details><summary><code>formatSegmentations.py</code></summary>
 
 >Takes the `.segmentations` files placed in `SegmentationsSplits` and converts them to match the shared task data format. It then uses the splits in `SharedTaskData` to create new splits in the same directory that have similar demographics but only include words in the `.segmentations` files. You may:
 >- Specify a designated input directory for the `.segmentations` files using the `-p` or `--path` flag.
 >- Specify a designated input directory for the original shared task splits using the `-o` or `--original` flag.
 >- Force the recreation of the `.total` file using the `-f` or `--force` flag (Normally, if the `.total` file is present, it will skip that step).
 >
 >And either: 
 >- Specify a language to convert using the `-l` or `--lang` flag with the UniMorph abbreviation.
 >- ~~Run all files using the `-a` or `--all` flag.~~ \[Not Yet Implemented\]
</details>

<details><summary><code>nonneural.py</code></summary>
 
 >This is the baseline `nonneural.py` taken from the [Sigmorphon 2023 Shared Task Repo](https://github.com/sigmorphon/2023InflectionST). It has been modified to use the argparse module. You may:
 >- Specify a designated input directory using the `-p` or `--path` flag.
 >- Run it on the test split using the `-t` or `--test` flag.
 >- Turn on output file generation using the `-o` or `--out` flag (The output is placed in the input directory).
</details>

<details><summary><code>properties.py</code></summary>
 
 >Contains default paths and settings for the project. The following properties are defined:
 >- `SEGMENTATIONS_FOLDER = "../SegmentationsSplits"`
 >- `SHARED_TASK_DATA_FOLDER = "../SharedTaskData"`
 >- `NEURAL_OUTPUT_FOLDER = "../NeuralTransducerOutput"`
 >- `NEURAL_ERRORS_FOLDER = "../NeuralTransducerFormatted"`
 >- `COUNTER_SORTER_OUTPUT_FOLDER = "../CounterSorterOutput"`
 >
 >The following sort methods are defined for use with `counterSorter.py`:
 >- `field` which sorts alphabetically.
 >- `suffix` which sorts alphabetically from the end of the string.
 >- `number` which sorts based on the number value of a column.
</details>

<details><summary><code>counterSorter.py</code></summary>
 
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

## Using this repository

Instructions on how to run the scripts, options in terms of data manipulation, and the sequences of running the data, then sorting, then counting.

### Necessary Libraries and Tools

Libraries: sys, os, argparse, re, getopt, 
Other libraries/tools that are helpful in viewing/manipulating this data: (MORE INFO NEEDED)

```bash
# Example command to install prerequisites
pip install -r requirements.txt
