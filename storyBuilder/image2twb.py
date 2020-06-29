# Copyright 2020 Apogee Integration, LLC

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import argparse
import subprocess


parser = argparse.ArgumentParser(description = "This script imports images in the order they appear in folder into a Tableau Story.")

# Determine absolute path of images directory that you'd like to transfer onto Tableau dashboards and a Tableau story.
parser.add_argument("images_folder_path", help = "Please provide the absolute path to the folder containing images to be imported into Tableau dashboards/ story")

# Determine tableau file name
parser.add_argument("tableau_path_name", help = "Please provide the name of the tableau output file without an extension")

# Option to overwrite automatic sizing with a fixed size taking in a height and width parameter
parser.add_argument("-f", "--fixed", metavar = ('HEIGHT', 'WIDTH'), help = "Flags whether you want the dashboards and story to be a fixed size. Requires a height and width pixel count for size dimensions desired.", type = int, nargs = 2,
  action = "append")

# Option to open Tableau file immediately with running of Python script
parser.add_argument("-o", "--open", help = "Flag if you want Tableau to open immediately with the script. O/w it will be saved to the current directory without opening.", 
  action = "store_true")

# Option to replace the tableau file if already exists.
parser.add_argument("-r", "--replace", help = "Flag if the Tableau name indicated already exists and you'd like to overwrite it.", 
  action = "store_true")

args = parser.parse_args()

# Directory of images to be fed into Tableau.
image_folder_path = args.images_folder_path

# Determine if Tableau file opens immediately following script or merely provides the .twb file without opening.
open_file_after_creation = args.open

replace_tableau_file = args.replace

# Default to automatic sizing of dashbaords and story
sizing_string = "sizing-mode='automatic'"
story_sizing_string = "sizing-mode='automatic'"

# Create snippet for fixed height and width values given arguments passed in.
height = 0
width = 0

if args.fixed is not None:
  
  image_dims = args.fixed

  height = image_dims[0][0]
  width = image_dims[0][1]
  sizing_string = "maxheight='{height}' maxwidth='{width}' minheight='{height}' minwidth='{width}' sizing-mode='fixed'".format(height = height, width = width)
  story_sizing_string = "maxheight='964' maxwidth='1016' minheight='964' minwidth='1016'"

## Check if tableau file name contains .twb at the end of it. Otherwise, append .twb to the end of it.
tableau_file_path = ""

if ".twb" in args.tableau_path_name:
  tableau_file_path = args.tableau_path_name 
else:
  tableau_file_path = args.tableau_path_name + ".twb"


# Absolute path of directory with images
directory = os.path.abspath(image_folder_path)


# Returns a list of sorted image files within directory ("path") base on their time stamp of creation
def sorted_ls(path):
    mtime = lambda f: os.stat(os.path.join(path, f)).st_mtime
    return list(sorted(os.listdir(path), key=mtime))

list_images = sorted_ls(directory)

if os.path.exists(tableau_file_path) & replace_tableau_file == False:

  print("File already exists. If you wish to overwrite existing file, please rerun with the -r or --replace flag.")

elif os.path.exists(tableau_file_path) & replace_tableau_file: 

  ## Write the Tableau file with the images in directory passed in
  with open(tableau_file_path, 'w') as f:
      
      # Header of the XML document
      f.write(
  """<?xml version='1.0' encoding='utf-8' ?>

  <!-- build 20194.19.1010.1202                               -->
  <workbook original-version='18.1' source-build='2019.4.0 (20194.19.1010.1202)' source-platform='mac' version='18.1' xmlns:user='http://www.tableausoftware.com/xml/user'>
    <document-format-change-manifest>
      <AutoCreateAndUpdateDSDPhoneLayouts ignorable='true' predowngraded='true' />
      <SheetIdentifierTracking ignorable='true' predowngraded='true' />
      <WindowsPersistSimpleIdentifiers />
    </document-format-change-manifest>
    <preferences>
      <preference name='ui.encoding.shelf.height' value='24' />
      <preference name='ui.shelf.height' value='26' />
    </preferences>
    <datasources />

    <dashboards>""")
      
      dashboard_num = 1

      for image_path in list_images:   

        #image_path = directory + "/" + image_path 
        image_path = os.path.join(directory, image_path)  

        if (".jpeg" in image_path.lower()) or (".png" in image_path.lower()) or (".jpg" in image_path.lower()):

          id_unique_end = dashboard_num + 1000

      #for each image in images_path, create a dashboard
          f.write("""
      <dashboard name='Dashboard {slide_num}'>
        <style />
        <size {sizing_string} />
        <zones>
          <zone h='100000' id='4' type='layout-basic' w='100000' x='0' y='0'>
            <zone h='97090' id='3' is-centered='0' is-scaled='1' param='{image_folder_image_path}' type='bitmap' w='98316' x='842' y='1455'>
              <zone-style>
                <format attr='border-color' value='#000000' />
                <format attr='border-style' value='none' />
                <format attr='border-width' value='0' />
                <format attr='margin' value='4' />
              </zone-style>
            </zone>
            <zone-style>
              <format attr='border-color' value='#000000' />
              <format attr='border-style' value='none' />
              <format attr='border-width' value='0' />
              <format attr='margin' value='8' />
            </zone-style>
          </zone>
        </zones>
        <devicelayouts>
          <devicelayout auto-generated='true' name='Phone'>
            <size maxheight='700' minheight='700' sizing-mode='vscroll' />
            <zones>
              <zone h='100000' id='6' type='layout-basic' w='100000' x='0' y='0'>
                <zone h='97090' id='5' param='vert' type='layout-flow' w='98316' x='842' y='1455'>
                  <zone fixed-size='280' h='97090' id='3' is-centered='0' is-fixed='true' is-scaled='1' param='{image_folder_image_path}' type='bitmap' w='98316' x='842' y='1455'>
                    <zone-style>
                      <format attr='border-color' value='#000000' />
                      <format attr='border-style' value='none' />
                      <format attr='border-width' value='0' />
                      <format attr='margin' value='4' />
                      <format attr='padding' value='0' />
                    </zone-style>
                  </zone>
                </zone>
                <zone-style>
                  <format attr='border-color' value='#000000' />
                  <format attr='border-style' value='none' />
                  <format attr='border-width' value='0' />
                  <format attr='margin' value='8' />
                </zone-style>
              </zone>
            </zones>
          </devicelayout>
        </devicelayouts>
        <simple-id uuid='{{4D058E49-AB62-4056-BA04-B1F1036B{end_id}}}' />
      </dashboard>""".format(image_folder_image_path = image_path , slide_num = dashboard_num, end_id = id_unique_end, sizing_string = sizing_string))

        dashboard_num += 1

      # Tableau Story header
      f.write("""
      <dashboard name='Story 1' type='storyboard'>
        <style />
        <size {story_sizing_string}/>
        <zones>
          <zone h='100000' id='2' type='layout-basic' w='100000' x='0' y='0'>
            <zone h='98340' id='1' param='vert' removable='false' type='layout-flow' w='98426' x='787' y='830'>
              <zone h='3423' id='3' type='title' w='98426' x='787' y='830' />
              <zone h='10477' id='4' is-fixed='true' paired-zone-id='5' removable='false' type='flipboard-nav' w='98426' x='787' y='4253' />
              <zone h='84440' id='5' paired-zone-id='4' removable='false' type='flipboard' w='98426' x='787' y='14730'>
                <flipboard active-id='2' nav-type='caption' show-nav-arrows='true'>
                  <story-points>""".format(story_sizing_string = story_sizing_string))
      
      # Tableau Story points created for each Dashboard
      for slide in range(1, len(list_images)):
          
          f.write("""
                    <story-point captured-sheet='Dashboard {slide_num}' id='{slide_num}' />""".format(slide_num = slide))
              
      # Tableau Story bottom code
      f.write("""
                  </story-points>
                </flipboard>
              </zone>
            </zone>
            <zone-style>
              <format attr='border-color' value='#000000' />
              <format attr='border-style' value='none' />
              <format attr='border-width' value='0' />
              <format attr='margin' value='8' />
            </zone-style>
          </zone>
        </zones>
        <simple-id uuid='{503D6677-4C88-47BE-9B70-D9B6504FB60B}' />
      </dashboard>""")
      
      
      # Between dashboard and windows
      f.write("""
    </dashboards>
    <windows>""")
      
      ### Create a unique id for each window created (per dashboard and per slide)
      for slide in range(1, len(list_images)):
          
          id_unique_end = slide + 1000
          
      # Windows XML section, one per dashboard created
          f.write("""
      <window class='dashboard' hidden='true' maximized='true' name='Dashboard {slide_num}'>
        <viewpoints />
        <active id='-1' />
        <simple-id uuid='{{B37FC551-7DBC-47F4-8E07-908C28F9{end_id}}}' />
      </window>""".format(slide_num = slide, end_id = id_unique_end))
      
      # Windows XML section for the story
      f.write("""
      <window class='dashboard' maximized='true' name='Story 1'>
        <viewpoints />
        <active id='-1' />
        <simple-id uuid='{C8E3C7C3-8B64-490D-8564-A7EA63E551AE}' />
      </window>""")
      
      # Tail end of the XML file
      f.write("""
    </windows>
  </workbook>""")

else:
  ## Write the Tableau file with the images in directory passed in
  with open(tableau_file_path, 'w') as f:
      
      # Header of the XML document
      f.write(
  """<?xml version='1.0' encoding='utf-8' ?>

  <!-- build 20194.19.1010.1202                               -->
  <workbook original-version='18.1' source-build='2019.4.0 (20194.19.1010.1202)' source-platform='mac' version='18.1' xmlns:user='http://www.tableausoftware.com/xml/user'>
    <document-format-change-manifest>
      <AutoCreateAndUpdateDSDPhoneLayouts ignorable='true' predowngraded='true' />
      <SheetIdentifierTracking ignorable='true' predowngraded='true' />
      <WindowsPersistSimpleIdentifiers />
    </document-format-change-manifest>
    <preferences>
      <preference name='ui.encoding.shelf.height' value='24' />
      <preference name='ui.shelf.height' value='26' />
    </preferences>
    <datasources />

    <dashboards>""")
      
      dashboard_num = 1

      for image_path in list_images:   

        #image_path = directory + "/" + image_path 
        image_path = os.path.join(directory, image_path)  

        if (".jpeg" in image_path.lower()) or (".png" in image_path.lower()) or (".jpg" in image_path.lower()):

          id_unique_end = dashboard_num + 1000

      #for each image in images_path, create a dashboard
          f.write("""
      <dashboard name='Dashboard {slide_num}'>
        <style />
        <size {sizing_string} />
        <zones>
          <zone h='100000' id='4' type='layout-basic' w='100000' x='0' y='0'>
            <zone h='97090' id='3' is-centered='0' is-scaled='1' param='{image_folder_image_path}' type='bitmap' w='98316' x='842' y='1455'>
              <zone-style>
                <format attr='border-color' value='#000000' />
                <format attr='border-style' value='none' />
                <format attr='border-width' value='0' />
                <format attr='margin' value='4' />
              </zone-style>
            </zone>
            <zone-style>
              <format attr='border-color' value='#000000' />
              <format attr='border-style' value='none' />
              <format attr='border-width' value='0' />
              <format attr='margin' value='8' />
            </zone-style>
          </zone>
        </zones>
        <devicelayouts>
          <devicelayout auto-generated='true' name='Phone'>
            <size maxheight='700' minheight='700' sizing-mode='vscroll' />
            <zones>
              <zone h='100000' id='6' type='layout-basic' w='100000' x='0' y='0'>
                <zone h='97090' id='5' param='vert' type='layout-flow' w='98316' x='842' y='1455'>
                  <zone fixed-size='280' h='97090' id='3' is-centered='0' is-fixed='true' is-scaled='1' param='{image_folder_image_path}' type='bitmap' w='98316' x='842' y='1455'>
                    <zone-style>
                      <format attr='border-color' value='#000000' />
                      <format attr='border-style' value='none' />
                      <format attr='border-width' value='0' />
                      <format attr='margin' value='4' />
                      <format attr='padding' value='0' />
                    </zone-style>
                  </zone>
                </zone>
                <zone-style>
                  <format attr='border-color' value='#000000' />
                  <format attr='border-style' value='none' />
                  <format attr='border-width' value='0' />
                  <format attr='margin' value='8' />
                </zone-style>
              </zone>
            </zones>
          </devicelayout>
        </devicelayouts>
        <simple-id uuid='{{4D058E49-AB62-4056-BA04-B1F1036B{end_id}}}' />
      </dashboard>""".format(image_folder_image_path = image_path , slide_num = dashboard_num, end_id = id_unique_end, sizing_string = sizing_string))

        dashboard_num += 1

      # Tableau Story header
      f.write("""
      <dashboard name='Story 1' type='storyboard'>
        <style />
        <size {story_sizing_string}/>
        <zones>
          <zone h='100000' id='2' type='layout-basic' w='100000' x='0' y='0'>
            <zone h='98340' id='1' param='vert' removable='false' type='layout-flow' w='98426' x='787' y='830'>
              <zone h='3423' id='3' type='title' w='98426' x='787' y='830' />
              <zone h='10477' id='4' is-fixed='true' paired-zone-id='5' removable='false' type='flipboard-nav' w='98426' x='787' y='4253' />
              <zone h='84440' id='5' paired-zone-id='4' removable='false' type='flipboard' w='98426' x='787' y='14730'>
                <flipboard active-id='2' nav-type='caption' show-nav-arrows='true'>
                  <story-points>""".format(story_sizing_string = story_sizing_string))
      
      # Tableau Story points created for each Dashboard
      for slide in range(1, len(list_images)):
          
          f.write("""
                    <story-point captured-sheet='Dashboard {slide_num}' id='{slide_num}' />""".format(slide_num = slide))
              
      # Tableau Story bottom code
      f.write("""
                  </story-points>
                </flipboard>
              </zone>
            </zone>
            <zone-style>
              <format attr='border-color' value='#000000' />
              <format attr='border-style' value='none' />
              <format attr='border-width' value='0' />
              <format attr='margin' value='8' />
            </zone-style>
          </zone>
        </zones>
        <simple-id uuid='{503D6677-4C88-47BE-9B70-D9B6504FB60B}' />
      </dashboard>""")
      
      
      # Between dashboard and windows
      f.write("""
    </dashboards>
    <windows>""")
      
      ### Create a unique id for each window created (per dashboard and per slide)
      for slide in range(1, len(list_images)):
          
          id_unique_end = slide + 1000
          
      # Windows XML section, one per dashboard created
          f.write("""
      <window class='dashboard' hidden='true' maximized='true' name='Dashboard {slide_num}'>
        <viewpoints />
        <active id='-1' />
        <simple-id uuid='{{B37FC551-7DBC-47F4-8E07-908C28F9{end_id}}}' />
      </window>""".format(slide_num = slide, end_id = id_unique_end))
      
      # Windows XML section for the story
      f.write("""
      <window class='dashboard' maximized='true' name='Story 1'>
        <viewpoints />
        <active id='-1' />
        <simple-id uuid='{C8E3C7C3-8B64-490D-8564-A7EA63E551AE}' />
      </window>""")
      
      # Tail end of the XML file
      f.write("""
    </windows>
  </workbook>""")



# If optional argument is true, open the Tableau file immediately, otherwise create the .twb file unopened.
if open_file_after_creation:
  subprocess.call(['open', tableau_file_path])



