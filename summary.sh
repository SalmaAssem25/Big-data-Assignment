#!/bin/bash

echo "Creating results folder..."
mkdir -p results

echo "Copying files..."
cp /app/pipeline/data_raw.csv ./results/
cp data_preprocessed.csv results/
cp :/app/pipeline/insight1.txt ./results/
cp :/app/pipeline/insight2.txt ./results/
cp :/app/pipeline/insight3.txt ./results/
cp :/app/pipeline/summary_plot.png ./results/
cp data_clustered.csv results/
cp clusters.txt results/

echo "Done! Check results folder."