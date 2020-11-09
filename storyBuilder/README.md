# Story Builder Utility

Script for transferring images exported from PowerPoint slides or otherwise into a Tableau Story presentation.

## Images to Tableau Python Script

### *image2twb.py*

This script was created to systematically insert images exported from PowerPoint, or other sources, into Tableau Dashboards, contained in a Tableau Story for presentation. The script is a huge timesaver when dealing with a large number of PPT slides to be converted into Tableau. The conversion is desired for better storytelling, and ultimately a path towards confident decision making, utilizing the wide range of features in Tableau. Script runs with '.jpeg', '.jpg', '.bmp' or '.png' image files. Ensure that .twb files are set to open with Tableau Desktop if you want to use the -o switch to automatically open the generated workbook. The -o switch relies on the open() command functioning well in your environment, which is not always the case.

Steps required for use:

1.	Export the slides you wish to include as images in either .jpeg, .jpg, .bmp or .png format. Remember the path to the directory with these images.
2.	Run the script on terminal or command prompt using the arguments described below.

## Running Utility Script

This is a Python script written to be called via command line, bash, terminal, etc. 

                python3 image2twb.py slides_path tableau_file_name [-f --fixed height width] [-o --open] [-r --replace]
                
The script also works with python2, aka python

* Positional Arguments:

  * *slides_path*: Path to the directory with the images exported from PPT.
  * *tableau_file_name*: Name for the Tableau workbook file created by the script. The .twb extension is optional and will be appended if absent.

* Optional Arguments:
  * *[-f, --fixed height width]*: Flags whether you want the dashboards and story to be a fixed size. If so, input height and width following tag. Otherwise, defaults to creating the Story and Dashboards an automatic size.
  * *[-o, --open]*: If provided, launches Tableau with the generated workbook. 
  * *[-r, --replace]*: If provided, will overwrite an existing Tableau workbook; otherwise, will stop if the workbook file already exists.
