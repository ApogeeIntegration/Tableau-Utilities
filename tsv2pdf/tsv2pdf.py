'''
    Copyright [2021] [APOGEE Integration]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

'''

import tableauserverclient as TSC
import argparse
import img2pdf
import os
import pandas as pd
from PIL import Image


def main():

    parser = argparse.ArgumentParser(description='Download pdf file of snapshot(s) of a tableau dashboard.')
    parser.add_argument('--server', '-s', required=True, help='server address')
    parser.add_argument('--token-name', '-tn', required=True,
                        help='user token name')
    parser.add_argument('--token-secret', '-ts', required=True, 
                        help='user token secret')
    parser.add_argument('--view-name', '-v', required=True,
                        help='name of dashboard view')   
    parser.add_argument('--csv', '-csv', required=False,
                        help='csv dataframe of filters/parameters')
    parser.add_argument('--filepath', '-f', required=True,
                        help='filepath to save the pdf file returned')
    
    args = parser.parse_args()
    
    #signs user into server using token access
    tableau_auth = TSC.PersonalAccessTokenAuth(args.token_name, args.token_secret, '')
    server = TSC.Server(args.server, use_server_version=True)
    server.auth.sign_in(tableau_auth)

    #query for the view that we want an image of
    with server.auth.sign_in(tableau_auth):
        req_option = TSC.RequestOptions()
        req_option.filter.add(TSC.Filter(TSC.RequestOptions.Field.Name,
                                         TSC.RequestOptions.Operator.Equals, args.view_name))
        all_views, pagination_item = server.views.get(req_option)
            
        if not all_views:
            raise LookupError("View with the specified name was not found.")
        
        view_item = all_views[0]

        #adds filter/parameters to the view if .csv included in argument
        if args.csv is not None:
            filters = pd.read_csv(args.csv)
            path_names = [0] * filters.shape[0]
            for i, j in filters.iterrows():  
                image_req_option = TSC.ImageRequestOptions(imageresolution=TSC.ImageRequestOptions.Resolution.High)
                for col in filters.columns:
                    image_req_option.vf(col, str(j[col]).replace(', ',','))
                    
                server.views.populate_image(view_item, image_req_option)
                
                #temporarily saves each view as separate .png files
                with open('py_img_%i.png' %i, "wb") as image_file:
                    image_file.write(view_item.image)
                    path_names[i] = ('py_img_%i.png' %i)
                             
        #takes a snapshot of the default view, when .csv not included            
        else:
            image_req_option = TSC.ImageRequestOptions(imageresolution=TSC.ImageRequestOptions.Resolution.High)
            server.views.populate_image(view_item, image_req_option)
            
            #temporarily saves view as .png
            with open('py_img_0.png', "wb") as image_file:
                image_file.write(view_item.image)
                path_names = ['py_img_0.png']
        
        #converts mode to remove alpha channel to allow .pdf conversion
        for path in path_names:
            img = Image.open(path)
            if img.mode == 'RGBA':
                img.convert('RGB').save(path)
               
        #save images as single .pdf     
        with open(args.filepath, "wb") as f:
            f.write(img2pdf.convert(path_names))
            
        #removes temporary .png file(s) from folder    
        for path in path_names:
            os.remove(path)


if __name__ == '__main__':
    main()
    
