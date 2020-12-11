#!usr/bin/env/python
'''
The script was created on NOV 11 2020.
It is intended to produce a suite of tools
to navigate the World Spider Catalogue:
    https://wsc.nmbe.ch/

'''

import os
from os.path import join as jn
import pandas as pd

path= r'D:\Garcilazo\Python\00Exercises\World_Spider_Catalogue'
os.chdir(path)
path_file = jn(path,"WSC_Salticidae_2020.txt")

final_list = []
with open(path_file,'r', encoding='utf-8') as file:
    file= file.readlines()
    for i in file:
        if 'Gen. ' in i:
            final_list.append(i.split('[')[0].replace('Gen. ',''))
    finalstring_name = ''
    finalstring_author = ''
    for i in final_list:
        gen_name =i.split(' ')[0]
        gen_author =i.split(' ',1)[1]
        finalstring_name +=gen_name +'\n'
        finalstring_author +=gen_author +'\n'

# print(finalstring_author)
# print(finalstring_name)
Maddison_class = 'Classification.xlsx'

df = pd.read_excel(jn(path,Maddison_class))
df = df.fillna('')
df = df.astype(str)

name_group = 'Hasariini'
for i,j in df.iterrows():
    for key in j.keys():
        # print(j[key])
        if name_group in j[key]:
            print('<li class="listen">'+j['Genus']+'</li>')
        # if name_group in j[key]:
        #     print(j['Genus'])


# ________________________________________________________________________________________________
# This function makes folders following a recursion and following Maddison_2005 classification
'''
In order to work the function needs
   - root path
   - an excel file with the structure of the folders
   - the categories to look into (can be taken from the excel columns, for example using df.keys()[5]),
'''

path_folders = r"D:\Garcilazo\Udemy\Notes_on_papers\Maddison_2015\Clades"
categories = df.keys()[:7] #choosing 7 instead of 6 adds the genus category

def recursive (df, categories,pos,path):
    original_path = path
    if pos<=len(categories)-1:
        local_list = df[categories[pos]].unique()
        for i in local_list:
            # os.mkdir(jn(path,i))
            if i!='':
                os.mkdir(jn(path,i))
                path+='\\'+i
                print(path)
                # print(path)
                new_df = df[df[categories[pos]]==i]
                recursive(new_df,categories, pos+1,path)
            else:
                new_df = df[df[categories[pos]]==i]
                recursive(new_df,categories, pos+1,path)
            path= original_path
    else:
        # path=path_folders
        return(None)

recursive (df,categories,0,path_folders)

# ________________________________________________________________________________________________
# This function takes the name of a genus and returns a string with the path where it's located and opens the file
'''
In order to work the function needs
   - root path
   - an excel file with the structure of the folders
   - the categories to look into (can be taken from the excel columns, for example using df.keys()[5]),
'''

path_folders = r"D:\Garcilazo\Udemy\Notes_on_papers\Maddison_2015\Clades"

taxon = 'Saltafresia'
for root, folder, file in os.walk(path_folders):
    for each_fold in folder:
        if taxon in each_fold:
            path_where_found = jn(root,each_fold)
            os.startfile(path_where_found)