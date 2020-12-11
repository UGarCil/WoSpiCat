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

path= r'D:\Garcilazo\Python\00Exercises\World_Spider_Catalogue\WSC_script'
os.chdir(path)
path_file = [x for x in os.listdir(path) if 'output' not in x and '.txt' in x][0]
catalogue_path = jn(path,path_file)

final_string = 'GEN\tSPP\tGEN+SPP\tAUTHOR\tYEAR\tAUTHORITY\tTYPE\tSEX\tDIS\tCONDIS\n'
with open(catalogue_path,'r', encoding='utf-8') as file:
    def pick_aut (aut, yr):
        if '(' in aut:
            return (aut.replace(')','') + ', ' + yr + ')')
        else:
            return (aut + ', ' + yr)
        

    file = file.readlines()
    for i in file:
        if 'Gen. ' in i:
            current_genus = i.split(' ')[1]
            # print(current_genus)
        elif '|' in i:
            species = i.split(' ')[1]
            second_str = i.split(' ',2)[2]
            # print(author)
            third_str = second_str.split(' | ')[0]
            is_bas = False
            if "*" in third_str:
                if '(' in third_str:
                    is_bas = True
                is_type = '*'
                no_par = third_str.replace('(','')
                no_par = no_par.replace(')','')
                year = no_par.replace(' *','')[-4:]
                # print(year)
                author = no_par.replace(' *','')[:-6]
                author = author.replace(',','')
                author = author.strip()
                if is_bas:
                    author = '('+author+')'
                # print(author)
            else:
                if '(' in third_str:
                    is_bas = True
                is_type = ''
                no_par = third_str.replace('(','')
                no_par = no_par.replace(')','')
                year = no_par[-4:]
                author = no_par[:-4]
                author = author.replace(',','')
                # print(author, author.strip())
                author = author.strip()
                if is_bas:
                    author = '('+author+')'
            final_string+=current_genus+'\t'+ \
            species + '\t' + \
            current_genus+' '+species + '\t' + \
            author + "\t" + \
            year +'\t' + \
            pick_aut (author,year) + '\t' + \
            is_type + '\t' + \
            second_str.split(' | ')[1] + '\t' + \
            second_str.split(' | ')[2].split(' [')[0] + '\n'
            
df = pd.DataFrame([final_string])
export = open('output.txt','w',encoding='utf-8')
export.write(final_string)
export.close()