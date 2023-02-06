
# EasyA 2.0
Here in the `README.md` file, you'll find information on the repository, and instructions on how to setup and use EasyA.<br>
**Table of Contents**
 - Description
 - How to Install
 - How to Use EasyA
 - Files
 - Contributors

## Description
EasyA is a program that allows college students to search which classes and instructors give the most As and/or Ds & Fs. This tool is designed to give the user more information about the statistics of the class.

There are two ways to use EasyA<br>

 - Student view *(Viewing data)*
 - Administrator view *(Inputting data)*

Data from: https://emeraldmediagroup.github.io/grade-data







## How to Install

### Software Dependencies
This program uses Python3 & a python library matplotlib.<br>

***Both Python3 & matplotlib must be downloaded & installed on your device in order for EasyA to function properly.***<br>

1) Download the [latest version of Python](https://www.python.org/downloads/) for your device<br>
2) Open the command prompt (or terminal on Mac), and type in this command:
			`pip3 install matplotlib`<br>

For Administators only:

1) A couple more libraries are needed to use the scraper: `requests` & `bs4`:<br>
           `pip3 install requests`<br>
           `pip3 install bs4`<br>

*(If you aren't using python 3 and have an older version of python, try typing the same command using `pip` instead of `pip3`)*<br>


### EasyA Installation
1)  **Download.** Click on the green "<> Code" button above the repo, then select the "Download ZIP" option. This will download the contents of the repo onto your local machine <br>
<img src="Instruction_Images/Step1_Download_Zip.pdf" width="300" align="center" ><br><br>

2)  **Unzip.** Open up to your Downloads in File Explorer/Finder and right-click on the zip folder you just downloaded. Then select the "Extract All" option, then press confirm by pressing "Extract". <br>
<img src="Instruction_Images/Step2_Extract_Zip.pdf" width="600"><br><br>
This will decompress the contents of the file, and allow you to now view and execute the files.<br><br>

At this point, EasyA is installed and ready to be run!





## How to Use EasyA


1) **Run EasyA.py.** Open up your command prompt (or terminal if on Mac), and navigate to your EasyA file you just unzipped.<br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`cd Downloads/EasyA-master/EasyA-master`<br><br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If you moved the EasyA folder out of of the Downloads folder, you'll need to find and type the correct path to the folder:<br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`cd insert/your/path/to/folder/EasyA-master`<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Once you're in the correct folder, *(can check folder's contents by using `dir` (Windows) or `ls` (Mac))*, execute the `EasyA.py` file by typing the following command:<br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`python3 EasyA.py`<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*(If you aren't using python 3 and have an older version of python, try typing the same command using `python` instead of `python3`)*<br>
This will use python to execute the EasyA program. <br><br>


2) **Provide Input.** Now that the program is running, a window will pop up with a few options. Here's what each option does:<br>

<img src="Instruction_Images/Step3_User_Interface.pdf" width=600><br>

#### UI Buttons<br>
Subject Code &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-- Select the department of class<br>
Course Number &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-- Select level of class<br>
All Courses at Level -- Look at all classes at x00 level<br>
Show Instructors &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-- Option to have all instructors (including GEs) or, you just school Faculty<br>
Grade Type &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-- EasyA (look at %As) vs JustPass (look at %D/Fs)<br>
Show # of Classes &nbsp;&nbsp;&nbsp;-- Show number of classes that instructor has taught<br>

#### Selecting Your Graph
1.  Select the subject code (department)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Press the Drop down menu to open the list of subject codes. Then scroll to & click your desire subject code.
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*(If the desired subject is AA, you may skip this step and go to Task 2.)*

2. Select course number
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If you would like to see a graph on a certain class, input a number for the course. Example: "110"
Not inputting a course level will not show a graph for a specific course within the department)

3. Select course level
&nbsp;&nbsp;&nbsp;&nbsp;If you would like to see a graph for all classes at a certain x00 level range, press the drop down menu and select a x00 level.
*Not selecting a course level will not display all the classes at the x00 level by class*

4. Select Faculty Filter
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If you would like to see classes from all instructors (including GEs), select `All Instructors` &nbsp;&nbsp;&nbsp;&nbsp;*(default)*
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If you would like to see classes from only faculty/professors, select `Faculty Only`

5. Select Graph Type
If you would like to see an EasyA graph (%As given), select `EasyA` &nbsp;&nbsp;&nbsp;*(default)*
If you would like to see a JustPass graph (%D/Fs given), select `JustPass`

6. Show class count
If you would like to see how many times a class was taught, or instructor taught, check the `Show # of classes`
If this is unchecked, it will not display the number of times a class was taught &nbsp;&nbsp;&nbsp;*(default)*


3) **View Graph.** After you have inputted the specifics of what you would like to see, the EasyA program has saved the graph as a .PDF in the "pdfs" folder. Find the EasyA folder on your local device via file explorer/finder, and open the desired<br>

Here is an example of a finished EasyA graph

<img src="Instruction_Images/Step4_Graph_Example.pdf" width=600><br>




### Administrator Use<br>
To input data, use the `-f` flag while running the file.<br>
              `python3 EasyA.py -f <filename>`<br>
            **The inputted file *must* be a .json file**
This will run the program ready to input data, and not prompt the user to select any department or course levels.
Now this scraper works for all schools, and not just a certain department. # FIXME<br>





## Files
**Main Files**<br>
`EasyA.py`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-- Main executable to run the program<br>
`Course_Class.py` -- Declaration of python class, "Course"<br>
`Graph_class.py` &nbsp;-- Declaration of python class, "Graph"<br>
`User_Input.py` &nbsp;&nbsp;&nbsp;-- Functions for getting input from user<br>
`Fetch_Data.py`	&nbsp;&nbsp;&nbsp;-- Various functions to process data<br>
`Draw_Graph.py`&nbsp;&nbsp;&nbsp;&nbsp;	-- Contains functions to create and initialize the graph so it's ready for plotting<br>

**Parsing & Data Files**<br>
`GradeData.txt` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-- All data<br>
`GradeData.py`   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-- `GradeData.txt` but in a python dictionary<br>
`Regular_Faculty.txt` -- List of Faculty members<br>
`Faculty_Parser.py` &nbsp;&nbsp;&nbsp;&nbsp;-- Functions to parse<br>
`Scrapper.py`	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-- Web scraper to parse through a specified url<br>


**Testing Files**<br>

`GradeData_SmallTest.py` &nbsp;&nbsp;-- Test file for testing <br>
`GradeData_SmallTest.txt` -- Small version of GradeData for testing<br>
`TestCases.py` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-- Various Test cases for functions<br>
`tkinter_test.py` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-- File for testing Tkinter<br>

**Folders**<br>
`images`&nbsp;&nbsp;&nbsp;-- Folder for holding image assets for README file<br>
`EasyA_pdfs`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-- Folder for holding saved .PDF files onces downloaded onto a local machine<br>




## Contributors
**Authors:** Ethan Aasheim, Melodie Collins, Linnea Gilius, Timothy Nadeau, Angela Pelky<br>
**Created:** 1/16/23 by Angela Pelky<br>
