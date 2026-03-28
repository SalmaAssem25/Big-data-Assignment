#!/bin/bash

echo "Creating results folder..."
mkdir -p results

echo "Copying files..."

cp data_preprocessed.csv results/
cp data_clustered.csv results/
cp clusters.txt results/

echo "Done! Check results folder."