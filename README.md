
\# Customer Analytics Pipeline



\## Team Members

\- salma sherif

\- haydi mostafa

\- Maryam ali

\- Yassin salah



\---



\## Project Description

This project implements a data processing pipeline using Python and Docker.  

It processes a raw dataset, performs preprocessing, generates insights, visualizes data, and applies clustering.



\---



\## Execution Flow

ingest.py → preprocess.py → analytics.py → visualize.py → cluster.py



\---

\##Docker Commands
build docker image:
    docker build -t customer-analytics

run container 
    docker run -it customer-analytics

\## How to Run 

python ingest.py bank.csv

(The rest of the scripts run automatically as part of the pipeline)



\---



\## Output Files

\- data_raw.csv -> raw dataset copy 

\- data_preprocessed.csv -> cleaned dataset  

\- insight1.txt, insight2.txt, insight3.txt -> generated insights
\-histogram.png -> distribution of selected feature
\-heatmap.png -> correlation between features
\-scatter.png -> relationship between variables
\- summary_plot.png -> visualization plots
\- clusters.txt -> number of samples per cluster



\---



\## Summary Script



The summary.sh script collects all output files into a results folder.



\---





\## Notes

\- K-Means clustering was applied using numerical features.

\- Data preprocessing included cleaning, transformation, and scaling.

