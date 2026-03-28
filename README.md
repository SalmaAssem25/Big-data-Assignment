
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



\## How to Run (Locally)



1\. Run preprocessing:

python preprocess.py bank.csv



2\. Run clustering:

python cluster.py



\---



\## Output Files



\- data\_preprocessed.csv → cleaned dataset  

\- data\_clustered.csv → dataset with clusters  

\- clusters.txt → number of samples per cluster  



\---



\## Summary Script



The summary.sh script collects all output files into a results folder.



\---



\## Notes

\- K-Means clustering was applied using numerical features.

\- Data preprocessing included cleaning, transformation, and scaling.

