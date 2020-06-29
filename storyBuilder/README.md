# Story Builder Utility

Script for transferring images exported from PowerPoint slides or otherwise into a Tableau Story presentation.

## Images to Tableau Python Script

### *image2twb.py*

This script was created to systematically insert images exported from PowerPoint, or other sources, into Tableau Dashboards, contained in a Tableau Story for presentation. The script is a huge timesaver when dealing with a large number of PPT slides to be converted into Tableau. The conversion is desired for better storytelling, and ultimately a path towards confident decision making, utilizing the wide range of features in Tableau. Script runs with '.jpeg', '.jpg', or '.png' image files. Please also ensure that .twb and .twbx files are all defaulted to open up with Tableau Desktop on your machine, as Tableau Public will not work with this script.

Steps required for use:

1.	Export the PPT slide deck of interest as images in either .jpeg, .jpg, or .png format. Save the path to the directory with these images.
2.	Run the script on terminal or command prompt using the arguments described below.

## Running Utility Script

This is a Python script written to be called via command line, bash, terminal, etc. 

                python3 image2twb.py slides_path tableau_file_name [-f --fixed height width] [-o --open] [-r --replace]

* Positional Arguments:

  * *slides_path*: Path to the directory with the images exported from PPT.
  * *tableau_file_name*: Name for the Tableau file created by the script. Tableau name input may or may not include the .twb extension, either way will work.

* Optional Arguments:
  * *[-f, --fixed height width]*: Flags whether you want the dashboards and story to be a fixed size. If so, input height and width following tag. Otherwise, defaults to creating the Story and Dashboards an automatic size.
  * *[-o, --open]*: Flags if you want the Tableau Workbook with the Story to open immediately with the script. Defaults to saving the Tableau .twb file in the current directory without opening. 
  * *[-r, --replace]*: Flags if the Tableau name indicated already exists and you'd like to overwrite it/ replace it with the script.
