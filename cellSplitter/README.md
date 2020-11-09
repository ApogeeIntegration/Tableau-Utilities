# Cell Splitter Utility

Scripts for splitting delimiter separated values from single cells into rows

## Tableau Prep Scripts

### CellSplitter.py

This script is a Python script written to be deployed via Tableau's TabPy server.

- connect to the Sample Country Data in Tableau Prep
- add a clean step to the data flow
  - rename the Person ID column to ‘Values’ (cellSplitter splits columns named ‘Values’)
  - add the prefix ‘Key’ to columns to output unchanged  (cellSplitter includes columns unchanged with the prefix ‘Key’) 
- add the cellSplitter script to the flow
  - connect to the Tableau Python (TabPy) server
  - locate the .py file that contains the cellSplitter function
  - enter the function name, ‘cellSplitter’
- hit enter and the results will be returned as an expanded version of the ‘Values’ column
- rename the columns back to the original names (directly in the Script step w/o an additional Clean Step)

### CellSplitter.R

This script is an R script written to be deployed via Tableau's RServe server.

- connect to the Sample Country Data in Tableau Prep
- add a clean step to the data flow
  - rename the Person ID column to ‘Values’ (cellSplitter splits columns named ‘Values’)
  - add the prefix ‘Key’ to columns to output unchanged  (cellSplitter includes columns unchanged with the prefix ‘Key’) 
- add the cellSplitter script to the flow
  - connect to the Tableau R (RServe) server
  - locate the .R file that contains the cellSplitter function
  - enter the function name, ‘cellSplitter’
- hit enter and the results will be returned as an expanded version of the ‘Values’ column
- rename the columns back to the original names (directly in the Script step w/o an additional Clean Step)

## Command Line Script

### CmdLineCellSplitter.py

This is a Python script written to be deployed via the Command Line.

- The command line script takes two required arguments to specify the input data file and the name of the column to split:
  
  $ python CmdLineCellSplitter.py My_Data_File.csv My_Target_Column
  
  - Also, the command line script can take additional optional arguments to specify the delimiter character, a new name for the target column if you would like to rename it, and any additional column names that you would like to be preserved in the output data.
