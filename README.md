# WoSpiCat
Parsing the World Spider Catalogue (WSCA) from https://wsc.nmbe.ch/
You can find a quick tutorial here: https://youtu.be/FVFAU0lHsic

File created on December 12th 2020 by Uriel Garcilazo Cruz. The script takes a .txt file containing a page from a family copied from the WSCA and return an output.txt file
with the relationship of species for each genera for each family.

To run the program:

Make sure to have anaconda installed and the pandas module is installed in your environment.

- Go to https://wsc.nmbe.ch/
- Pick a family and enter it's catalog page
- Copy the page into a .txt editor. MAKE SURE YOUR ENCODING FORMAT IS UTF-8. Often not all characters used in the catalogue can be read by ASCII because they are not english words. 
- Save your file. The name is not important as long as it's not named 'output.txt'. It might be a good idea to name it with the family name just to be consistent.
- double click on main.py. An output.txt file should appear. Open it, copy it and paste it into excel.

Now you can make pivot tables to extract information on the distribution, No. species, etc. for the taxa within the family.

