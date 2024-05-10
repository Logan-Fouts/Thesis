#!/bin/bash

# Define the directory containing the .txt files
DIRECTORY="./outputs/california-experiment-size=701"

# Header for the output
echo "filename | Data size | TP | FP | FN | Precision | Recall | F1-Score | Accuracy | Elapsed Time (s)"

# Loop through all .txt files in the directory
for file in "$DIRECTORY"/*.txt; do
    # Extract the filename
    filename=$(basename "$file")

    # Extract relevant data using grep and awk
    num_images=$(grep "Num Images:" "$file" | awk '{print $NF}')
    tp=$(grep "TP:" "$file" | awk '{print $NF}')
    fp=$(grep "FP:" "$file" | awk '{print $NF}')
    fn=$(grep "FN:" "$file" | awk '{print $NF}')
    precision=$(grep "Precision:" "$file" | awk '{print $NF}')
    recall=$(grep "Recall:" "$file" | awk '{print $NF}')
    f1_score=$(grep "F1-Score:" "$file" | awk '{print $NF}')
    accuracy=$(grep "Accuracy:" "$file" | awk '{print $NF}')
    elapsed_time=$(grep "Elapsed Time:" "$file" | awk '{print $NF}')

    # Print out the data in a tab-separated line
    echo "$filename | $num_images | $tp | $fp | $fn | $precision | $recall | $f1_score | $accuracy | $elapsed_time"
done
