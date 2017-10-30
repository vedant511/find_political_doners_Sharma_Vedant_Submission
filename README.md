# Table of Contents
1. [Introduction](README.md#introduction)
2. [Running Instructions](README.md#running-instructions)
3. [Details of Source Code](README.md#details-of-source-code)

# Introduction
##### Programming Language -> python2.7
##### IDE -> PYCHARM
##### Complexity -> O(n)
##### Required Functionality Achieved -> 100%

This repository contains my response for the insight data engineering fellowship coding task. I have written an efficient and scalable code with a run-time complexity of O(n) where n is the number of lines in the input file. My code will work efficiently even with very large input files.

# Running Instructions
To run the code, migrate to the src folder. The code can be run either giving an input text file name as an argument to the python script or even without the argument.
If the user gives the argument, the code will execute and give output text files based on the name of input file given by user.
If the user does not give the argument, the code will execute and give output based on default itcont.txt file in input folder.
! Make sure you copy your text file in the input folder before giving it as an argument while excuting the code.

To run using your file in input folder=>
(Assuming you are in the src folder in terminal)
##### python find_political_donors.py <your_file_name.txt>

To run using default file itcont.txt=>
##### python find_political_donors.py

###### *You can check the output files medianvals_by_zip.txt and medianvals_by_date.txt in the output folder after running the code.

# Details of Source Code

Different methods have been created to achieve the required functionality. These methods with their function are:
1. main - This is the main method which will be called when you will execute the program. It will call other helper methods.
2. load_file - This method loads the input text file into a dataframe and returns it.
3. parse_input - This function does the major job in creating the medianvals_by_zip.txt output file. It takes in the input dataframe returned by above load_file method and two dictionaries which will get filled up by this method according to the constraints. It returns the medianvals_by_zip dataframe.
4. make_date_df - This method takes in the by_date_dict modified by the "parse_input" method, and makes and returns a dataframe from it which contains the fields sorted by recipient ID and date.
5. make_text_files - This method takes in the two final dataframes for medianvals by zip and dict respectively and makes the required output text files from them.
The Flow of the program is as follows (main method handles all this)
###                        INPUT--->LOAD_FILE--->PARSE_INPUT--->MAKE_DATE_DF--->MAKE_TEXT_FILES(OUTPUT)

