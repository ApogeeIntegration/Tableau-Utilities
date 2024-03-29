# Tableau Server View to PDF File

Script for transferring multiple snapshots of different views of a Tableau Dashboard into a multi-page PDF file.

## tsv2pdf script

### *tsv2pdf.py*

This script was created to systematically allow a user to pick multiple filters for multiple snapshots of a view and then paste all images together into a single .pdf file.

Steps required for use:

1.	Create a .csv file with columns named after the filter and cells filled in with parameter and/or filter specifications*
2.  Have the desired dashboard view uploaded to your server
2.	Run the script on terminal or command prompt using the arguments described below.

## Running Utility Script

This is a Python script written to be called via command line, bash, terminal, etc. 

     python tsv2pdf.py [-s --server] [-tn --token-name] [-ts --token-secret] [-v --view-name] [-csv --csv] [-f --filepath]

\* Note this step is optional, if it is ignored the default view will be printed to a pdf
