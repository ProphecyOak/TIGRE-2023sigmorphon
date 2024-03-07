#!/bin/sh

#Generate .out files
python formatNeuralErrors.py
python formatSegmentations.py -f

python nonneural.py -o
python nonneural.py -o -t

python nonneural.py -o -p ../SegmentationsSplits
python nonneural.py -o -t -p ../SegmentationsSplits

python errorSummation.py ../SharedTaskData/fra.dev.out 2 0 \
    ../NeuralTransducerFormatted/fra.neural.dev.tsv 0 0 \
    -s ../SharedTaskData/fra.dev \
    -o ../CounterSorterOutput/summed_Original-Dev.tsv \
    -n Original-Dev-Nonneural Original-Dev-Neural
    
python errorSummation.py ../SharedTaskData/fra.tst.out 2 0 \
    ../NeuralTransducerFormatted/fra.neural.test.tsv 0 0 \
    -s ../SharedTaskData/fra.tst \
    -o ../CounterSorterOutput/summed_Original-Tst.tsv \
    -n Original-Tst-Nonneural Original-Tst-Neural

python errorSummation.py ../SegmentationsSplits/fra.dev.out 2 0 \
    ../NeuralTransducerFormatted/fra-segmentations.neural.dev.tsv 0 0 \
    -s ../SegmentationsSplits/fra.dev \
    -o ../CounterSorterOutput/summed_Segmentations-Dev.tsv \
    -n Segmentations-Dev-Nonneural Segmentations-Dev-Neural

python errorSummation.py ../SegmentationsSplits/fra.tst.out 2 0 \
    ../NeuralTransducerFormatted/fra-segmentations.neural.test.tsv 0 0 \
    -s ../SegmentationsSplits/fra.tst \
    -o ../CounterSorterOutput/summed_Segmentations-Tst.tsv \
    -n Segmentations-Tst-Nonneural Segmentations-Tst-Neural

python errorSummation.py ../CounterSorterOutput/summed_Original-Dev.tsv \
    ../CounterSorterOutput/summed_Segmentations-Dev.tsv \
    -o ../CounterSorterOutput/summedDev.tsv -e

python errorSummation.py ../CounterSorterOutput/summed_Original-Tst.tsv \
    ../CounterSorterOutput/summed_Segmentations-Tst.tsv \
    -o ../CounterSorterOutput/summedTst.tsv -e

python errorSummation.py ../CounterSorterOutput/summedDev.tsv \
    ../CounterSorterOutput/summedTst.tsv \
    -o ../CounterSorterOutput/summedAll.tsv -e