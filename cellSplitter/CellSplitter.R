"Copyright [2020] [APOGEE Integration]

Licensed under the Apache License, Version 2.0 (the \"License\");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an \"AS IS\" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License."

library(dplyr)
library(splitstackshape)

cellSplitter <- function(df){
  if ('Values' %in% colnames(df)){
    df <- df %>%
      select("Values",starts_with("Key"))
    return(cSplit(df, 'Values', ',', 'long'))
  }
  else{
    return(df)
  }
}

getOutputSchema <- function(inputSchema){
  if ('Values' %in% colnames(inputSchema)){
    return(inputSchema %>% select("Values",starts_with("Key")))
  }
  else{
    return(inputSchema)
  }
}
