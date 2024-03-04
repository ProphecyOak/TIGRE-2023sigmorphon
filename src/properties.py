SEGMENTATIONS_FOLDER = "../SegmentationsSplits"
SHARED_TASK_DATA_FOLDER = "../SharedTaskData"
NEURAL_OUTPUT_FOLDER = "../NeuralTransducerOutput"
NEURAL_ERRORS_FOLDER = "../NeuralTransducerErrors"
COUNTER_SORTER_OUTPUT_FOLDER = "../CounterSorterOutput"

SORT_FUNCTIONS = {
    "field": lambda x,y: x[y],
    "suffix": lambda x,y: x[y][::-1],
    "number": lambda x,y: int(x[y])
}