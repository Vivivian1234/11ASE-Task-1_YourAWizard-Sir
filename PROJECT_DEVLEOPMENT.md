# _**11ASE Task 1 2025 - Harry Potter Spell Application**_

### By Vivian Ding
---
---
## **Requirements Definition**

### *Functional Requirements*

* The application should be able to import data
* The application should be able to handle errors and continue without breaking or executing incorrect outputs
* The application should have a clear and consistent user interface
* The application should be able to be installed without errors
* The application should be able to access data without loading a cvs file

### *Non-Functional Requirements*
* The application should load quickly
* The application should be efficient
* The application should be secure and very reliable
* The application should be publicly accessible
* The application should should have an instructions screen that can be viewed at anytime for users
* The application should have a maintained level of data integrity

# *Determining Specifications*
### *Functional Specifications*

\
**User Requirements**\
<u>What does the user need to be able to do? List all specifications here.</u>

The user should be able to understand the main menu and be able to give inputs that are required. They should be to choose what function to do (search spell, add spell, view spellbook, remove spell and exit program), as well as input spell names for those functions to do.

\
**Inputs & Outputs**\
<u>What inputs will the system need to accept and what outputs will it need to display?</u>

The system should accept numbers from 1-5 for the main menu, and should be able to accept any string and display the correct output whether the input is a valid spell or not.

\
**Core Features**\
<u>At its core, what specifically does the program need to be able to do?</u>

The program should be able to search, store, remove spells and view the spellbook where added spells are stored. The system should display the spell and description of the spell for the user to be informed. The program should be able to load quickly and should be able to exit efficiently.

\
**User Interaction**\
<u>How will users interact with the system (e.g. command-line, GUI?) and what information will it need to provide to help users navigate?</u>

The system is text based, so the user will type inputs in command lines and the system will perform accordingly. The instructions will be displayed in the main menu, as well as the README file for extra information.

\
**Error Handling**\
<u>What possible errors could you face that need to be handled by the system?</u>

Possible errors include an invalid input for the main menu and functions. When incorrect inputs are detected for search_spell, it will return "Spell not found." When incorrect inputs are detected for add_spell, it will return "{name} was not found. Could not add to your spellbook." When incorrect inputs are detected for remove_spell, it will return "Spell not found in your spellbook." When incorrect inputs are detected for the main menu screen, it will return "Invalid choice. Please try again." These errors have been detected and handled by the system and direct the user back to the main menu, ensuring there are no crashes and keeps the system running.

<br>   

# *Design*

### **Gantt Chart**
\
hi

### **Harry Potter Structure Chart**

\
![Harry_Potter_Structure_Chart](/images/Harry_Potter_Structure_Chart.png "Harry Potter Structure Chart")


### **Harry Potter Main Algorithm**
\
![Harry_Potter_Algorithms](/images/Harry%20Potter%20Algorithm.png "Harry Potter Algorithms")

<br>   

### **Harry Potter Algorithm Chart Pseudocode**

BEGIN main()\
&ensp; &ensp; choice = 0\
&ensp; &ensp; WHILE choice is not 5\
&ensp; &ensp; &ensp; &ensp; INPUT choice\
&ensp; &ensp; &ensp; &ensp; IF choice is 1 THEN\
&ensp; &ensp; &ensp; &ensp; &ensp; &ensp; Search spell\
&ensp; &ensp; &ensp; &ensp; &ensp; &ensp; &ensp; &ensp; IF API Request Valid THEN\
&ensp; &ensp; &ensp; &ensp; &ensp; &ensp; &ensp; &ensp; &ensp; &ensp; Show spell data\
&ensp; &ensp; &ensp; &ensp; &ensp; &ensp; &ensp; &ensp; ELSE\
&ensp; &ensp; &ensp; &ensp; &ensp; &ensp; &ensp; &ensp; &ensp; &ensp; DISPLAY 'Invalid choice. Please try again.'\
&ensp; &ensp; &ensp; &ensp; &ensp; &ensp; &ensp; &ensp; ENDIF\
&ensp; &ensp; &ensp; &ensp; ELSEIF choice is 2 THEN\
&ensp; &ensp; &ensp; &ensp; &ensp; &ensp; Store spell\
&ensp; &ensp; &ensp; &ensp; ELSEIF choice is 3 THEN\
&ensp; &ensp; &ensp; &ensp; &ensp; &ensp; Cast spell\
&ensp; &ensp; &ensp; &ensp; ELIF choice is 4 THEN\
&ensp; &ensp; &ensp; &ensp; &ensp; &ensp; Remove spell\
&ensp; &ensp; &ensp; &ensp; ELSE\
&ensp; &ensp; &ensp; &ensp; &ensp; &ensp; DISPLAY 'Invalid choice. Please try again.'\
&ensp; &ensp; &ensp; &ensp; ENDIF\
&ensp; &ensp; ENDWHILE\
END main()

### **Harry Potter Sub Algorithm- Add_spell**
\
![Harry Potter Sub Algorithm- Add_spell](/images/Harry%20Potter%20Sub%20Algorithm-%20Add_spell.png "Harry Potter Sub Algorithm- Add_spell")


### **Harry Potter Pseudocode- Add_spell**

BEGIN add_spell(name)\
&ensp; &ensp; CALL search_spell(name)\
&ensp; &ensp; IF spell is found THEN\
&ensp; &ensp; &ensp; &ensp; ADD spell to spellbook\
&ensp; &ensp; &ensp; &ensp; DISPLAY 'Spell added to spellbook.'\
&ensp; &ensp; &ensp; &ensp; DISPLAY 'Spellbook:'\
&ensp; &ensp; &ensp; &ensp; ALL view_spellbook()\
&ensp; &ensp; ELSE\
&ensp; &ensp; &ensp; &ensp; DISPLAY 'Spell not found. Could not add to your spellbook.'\
&ensp; &ensp; ENDIF\
END add_spell


<br>  

### **Harry Potter Sub Algorithm- View_spellbook**
\
![Harry Potter Sub Algorithm- View_spellbook](/images/Harry%20Potter%20Sub%20Algorithm-%20View_spellbook.png "Harry Potter Sub Algorithm- View_spellbook")



### **Harry Potter Sub Algorithm- View_spellbook**

BEGIN view_spellbook\
&ensp; &ensp; IF spellbook is not empty THEN\
&ensp; &ensp; &ensp; &ensp; FOR each spell in spellbook \
&ensp; &ensp; &ensp; &ensp; &ensp; &ensp; DISPLAY spell name and description\
&ensp; &ensp; &ensp; &ensp; ENDFOR\
&ensp; &ensp; ELSE\
&ensp; &ensp; &ensp; &ensp; DISPLAY 'Your spellbook is empty.'\
&ensp; &ensp; ENDIF\
END view_spellbook

<br>  


# *Data dictionary*

| Variable | Data Type | Format for Display | Size in Bytes | Size for Display | Description | Example | Validation |
|----------|-----------|--------------------|---------------|------------------|-------------|---------|------------|
|Spell name|String|Text|50|50|The name of the spell|Obliviate|Must be a non-empty string|
|Description|String|Text|100|100|What the spell does after being cast|Erases the target's memory|Must be a non-empty string|


# *Peer Evaluation*
### **Person 1- Will**
The code works very cleanly although the search function wasn't working yet the code reacted to all errors cleanly and without creating a bug. This project achieves what it aims to do.

### **Person 2- Erin**
The program is able to run and store user inputs successfully and it displays the output. When there is an issue in the input, the program is able to detect the error and request the user to choose an option again. There are many options for users to choose from with many spells however it was inconvenient to browse through the spells which aren't in a readme or a separate file in the project, I would suggest that the spells could be allocated a separate file. Overall, I believe that the program was successful in terms of visibility and accuracy as it allowed for users to effortlessly look through the menu the program provides and choose an option for what they require without having to shuffle through countless amounts of data.

# *Maintenance*

<u>Explain how you would handle issues caused by changes to the API over time.</u>

I would constantly update the system to stay compatible with the API, ensuring all modifications will keep the system secure and functional.

<u>Explain how you would ensure the program remains compatible with new versions of Python and libraries like requests. </u>

I would constantly refresh my code to stay compatible with newer versions of python to ensure that all the code is still functional and efficient.

<u> Describe the steps you would take to fix a bug found in the program after deployment. </u>

Once I find a bug in the program, I would immediately try to fix the code and constantly test it to ensure it is fixed. Once fixed, I would then push it to GitHub to keep it updated.

<u>Outline how you would maintain clear documentation and ensure the program remains easy to update in the future.</u>

I would maintain clear documentation to ensure the program is easy to understand by writing all the things completed in each push and how it impacted and improved the system.

<br>   

# *Final Evaluation*

<u> Evaluate the current functionality of the program in terms of how well it addresses the functional and non-functional requirements. </u>

The program completes the functional requirements of a system which can import data without loading a cvs file and using it to create a user interface for users to access. It can also be installed and handle errors fine. The program also completes non-functional requirements such as its efficiency, accessibility and instructions that all improve user experience.

<u>Discuss areas for improvement or new features that could be added.</u>

I would definitely improve on information displayed for the program. From personal knowledge and peer evaluation, not having the spell names in the program itself makes the whole experience far more troublesome due to the specific inputs needed, and without the API opened to assist users, it may be an unpleasant experience, as misspellings will return the user back to the main menu. I would also fix the search_spell function, as it currently does nothing, but I am unsure how to code the function to return the information due to the function using a different code from others because of the API's specifications. I was unable to find how to do it, but in the future I would most certainly like to improve on it and find a way to get all the information needed.

<u>Evaluate how the project was managed throughout its development and maintenance, including your time management and how challenges were addressed during the software development lifecycle.</u>

The project was managed well through its development, with the main focus on the code. My time management wasn't the best...but I will definitely improve on that in the future. I left the majority of the theory last as I could easily work on them from home with limited time and resources, which may have impacted the consistency of my GitHub pulls. Challenges I faced were mostly the code, but once that was fixed I could work on the theory easily.

<br>   

# *Testing and Debugging*

**Commit 1- 5/3/2025**
---
<u>1. Outline changes made to the code</u>\
This commit was made to add all the subheadings for the documentation such as the functional and non-functional requirements.

<u>2. Assess the impact of these changes.</u>\
This early formatting allowed me to plan early and clearly display the parts completed and finished in order.

<u>3.Outline the next steps.</u>\
The next step for me is to finish all my requirements and specifications.

\
**Commit - 10/3/2025**
---
<u>1. Outline changes made to the code</u>\
I completed the requirements, specifications and all the required charts. I added them to the documentation, which the flowchart screenshots added to a folder called Images.

<u>2. Assess the impact of these changes.</u>\
This step is essential for all this information is the first part of the documentation, so it outlines the purpose and function of this system and provides a detailed structure of it.

<u>3.Outline the next steps.</u>\
The next step is the data dictionary, as it ensures that each data type is identified and the code follows those rules.

\
**Commit - 14/3/2025**
---
<u>1. Outline changes made to the code</u>\
I finished the data dictionary to ensure all the data type information was understood and shown in my documentation.

<u>2. Assess the impact of these changes.</u>\
The data dictionary helped make sure that the data I have and the code I will use it for aligned with the data types in the API and the restrictions of it.

<u>3.Outline the next steps.</u>\
The next step is to work on the code for the API system.

\
**Commit - 19/3/2025**
---
<u>1. Outline changes made to the code</u>\
I started working on the API code, using the pokemon example provided and changing each data type and variable name to work with the API. Unfortunately, the search_spell function would not work and I could not figure out why, which led me to complete the rest of the code and leave it.

<u>2. Assess the impact of these changes.</u>\
This step is important as it is the first prototype of my API code. Working on the code early has given me time to figure out the code and work on the other functions without rushing.

<u>3.Outline the next steps.</u>\
The next step would be to fix the search_spell function and try to improve the rest of the code.

\
**Commit - 24/3/2025**
---
<u>1. Outline changes made to the code</u>\
Mr Scott helped me fix the search_spell function :)\
The problem was due to the API's specific retrieving requirements, as the standard code of requesting data was incompatible with it, leaving an empty output. The function being fixed allowed the rest of the code to work perfectly, leading me to finish the first full prototype of my code.

<u>2. Assess the impact of these changes.</u>\
This was a very significant step as it was the first full prototype of my code, which allowed me to test the basic functions and give me time to improve on other parts.

<u>3.Outline the next steps.</u>\
The next step would be the peer evaluation and the testing and debugging.

\
**Commit - 7/4/2025**
---
<u>1. Outline changes made to the code</u>\
I completed the peer evaluation with Will and Erin, who very kindly provided very insightful feedback on my code, highlighting what was completed and what should be improved on.

<u>2. Assess the impact of these changes.</u>\
This was important as it helped me understand what I could improve on in the future to further enhance the API system.

<u>3.Outline the next steps.</u>\
The next step would be the installation, where I update the requirements and README() files.

\
**Commit - 7/4/2025**
---
<u>1. Outline changes made to the code</u>\
I updated the README() file and the requirements.txt for the full instructions and outline of the API system.

<u>2. Assess the impact of these changes.</u>\
This assists users in installing dependencies and gives users instructions necessary to run the software.

<u>3.Outline the next steps.</u>\
The next step would be the maintenance and final evaluation stages to identify how well my system has completed the requirements.

\
**Commit - 8/4/2025**
---
<u>1. Outline changes made to the code</u>\
I finished the maintenance and the final evaluation stages.

<u>2. Assess the impact of these changes.</u>\
They address my time management and development skills during the project, explaining my steps through this task and what I should work on.

<u>3.Outline the next steps.</u>\
The next step would be the testing and debugging stage, where I use all my GitHub commits to prove my consistent work.

\
**Commit - 8/4/2025**
---
<u>1. Outline changes made to the code</u>\
This is the testing and debugging stage, where I use all my commits and write this section.

<u>2. Assess the impact of these changes.</u>\
The step is important as it is used as my evidence log to prove that I have been working consistently throughout the term and using all my lessons appropriately.

<u>3.Outline the next steps.</u>\
The next step would be to double check all my files are correct, my repository is public and then submit it!!! Yay :D

