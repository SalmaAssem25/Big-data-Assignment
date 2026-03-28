#!/bin/bash

mkdir -p results

docker cp analytics-container:/app/pipeline/data_raw.csv ./results/
docker cp analytics-container:/app/pipeline/data_preprocessed.csv ./results/

docker cp analytics-container:/app/pipeline/insight1.txt ./results/
docker cp analytics-container:/app/pipeline/insight2.txt ./results/
docker cp analytics-container:/app/pipeline/insight3.txt ./results/
docker cp analytics-container:/app/pipeline/clusters.txt ./results/

docker cp analytics-container:/app/pipeline/summary_plot.png ./results/

docker stop analytics-container
docker rm analytics-container

echo "Results copied successfully!"