#!/bin/sh

#Generate .out files
python formatNeuralErrors.py

python nonneural.py -o
python nonneural.py -o -t

python nonneural.py -o -p ../SegmentationsSplits
python nonneural.py -o -t -p ../SegmentationsSplits

python errorSummation.py ../SharedTaskData/fra.dev.out 1 2 0 \
    ../NeuralTransducerFormatted/fra.neural.dev.tsv 1 0 0 \
    -s ../SharedTaskData/fra.dev
mv ../CounterSorterOutput/summedErrors.tsv \
    ../CounterSorterOutput/summed_Original-Dev.tsv
    
python errorSummation.py ../SharedTaskData/fra.tst.out 1 2 0 \
    ../NeuralTransducerFormatted/fra.neural.test.tsv 1 0 0 \
    -s ../SharedTaskData/fra.tst
mv ../CounterSorterOutput/summedErrors.tsv \
    ../CounterSorterOutput/summed_Original-Tst.tsv

python errorSummation.py ../SegmentationsSplits/fra.dev.out 1 2 0 \
    ../NeuralTransducerFormatted/fra-segmentations.neural.dev.tsv 1 0 0 \
    -s ../SegmentationsSplits/fra.dev
mv ../CounterSorterOutput/summedErrors.tsv \
    ../CounterSorterOutput/summed_Segmentations-Dev.tsv

python errorSummation.py ../SegmentationsSplits/fra.tst.out 1 2 0 \
    ../NeuralTransducerFormatted/fra-segmentations.neural.test.tsv 1 0 0 \
    -s ../SegmentationsSplits/fra.tst
mv ../CounterSorterOutput/summedErrors.tsv \
    ../CounterSorterOutput/summed_Segmentations-Tst.tsv