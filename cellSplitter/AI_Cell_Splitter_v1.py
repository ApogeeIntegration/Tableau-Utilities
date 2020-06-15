'''
   Copyright [2020] [APOGEE Integration]

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
import pandas as pd

def cellSplitter(df):
    if 'Values' in df:
        df['Values']=df['Values'].str.split(',')
        exploded = df.filter(regex='Values|^Key').explode('Values')
        exploded = exploded[exploded['Values'].str.strip().astype(bool)]
        return exploded
    else:
        return df

def get_output_schema(inputSchema):
    if 'Values' in inputSchema:
        return pd.DataFrame(inputSchema.filter(regex='Values|^Key'))
    else:
        return pd.DataFrame(inputSchema)
    
