# Story Builder Utility

Script for transferring PowerPoint slides into a Tableau Story presentation.

## Images to Tableau Python Script

### *images_to_tableau.py*

This script was created to systematically insert JPEG images exported from PowerPoint to Tableau Dashboards, contained in a Tableau Story for presentation. The script is a huge timesaver when dealing with a large number of PPT slides to be converted into Tableau. The conversion is desired for better storytelling, and ultimately a path towards confident decision making, utilizing the wide range of features in Tableau. 

Steps required for use:

1.	Export the PPT slide deck of interest as images in JPEG format. It must be in JPEG. Save the path to the directory with these images.
2.	Ensure that .twb and .twbx files are all defaulted to open up with Tableau Desktop, as Tableau Public will not work with this script. 
3.	Run the script on terminal or command prompt. It takes 2 positional arguments and 2 optional arguments. 

## Running Utility Script

This is a Python script written to be called via command line, bash, terminal, etc. 

For MacOS or unix-based systems:

   *python3 images_to_tableau.py slides_path tableau_file_name [-f ?fixed height width] [-o ?open]*

* Positional Arguments:

  * *slides_path*: Path to the directory with the images exported from PPT.
  * *tableau_file_name*: Name for the Tableau file created by the script.

* Optional Arguments:
  * *[-f, --fixed height width]*: Flags whether you want the dashboards and story to be a fixed size. If so, input height and width following tag. Otherwise, defaults to creating the Story and Dashboards an automatic size.
  * *[-o, --open]*: Flags if you want the Tableau Workbook with the Story to open immediately with the script. Defaults to saving the Tableau .twb file in the current directory without opening. 

For Windows OS:

   *python3 images_to_tableau.exe slides_path tableau_file_name [-f ?fixed height width] [-o ?open]*

* Positional Arguments:

  * *slides_path*: Path to the directory with the images exported from PPT.
  * *tableau_file_name*: Name for the Tableau file created by the script.

* Optional Arguments:
  * *[-f, --fixed height width]*: Flags whether you want the dashboards and story to be a fixed size. If so, input height and width following tag. Otherwise, defaults to creating the Story and Dashboards an automatic size.
  * *[-o, --open]*: Flags if you want the Tableau Workbook with the Story to open immediately with the script. Defaults to saving the Tableau .twb file in the current directory without opening. 
