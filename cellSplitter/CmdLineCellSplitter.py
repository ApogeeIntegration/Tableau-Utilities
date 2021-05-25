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
import pandas as pd
import argparse

def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("target_col")
    parser.add_argument("-s", "--sep", default=",")
    parser.add_argument("-n", "--new_col")
    parser.add_argument("argv", nargs="*", default = [])
    return parser.parse_args()

def splitter(input_file, target_col, sep, new_col = None, *argv):
    df = pd.read_csv(input_file)
    df[target_col] = df[target_col].str.split(sep)
    exploded = df[[target_col, *argv]].explode(target_col)
    exploded = exploded[exploded[target_col].str.strip().astype(bool)]
    if new_col == None:
        return pd.DataFrame(exploded[[target_col,*argv]])
    else:
        exploded[new_col] = exploded[target_col]
        return pd.DataFrame(exploded[[new_col,*argv]])

if __name__ == '__main__':
    args = arg_parse()
    result = splitter(
        args.input_file,
        args.target_col,
        args.sep,
        args.new_col,
        *args.argv
    )
    print(result)
