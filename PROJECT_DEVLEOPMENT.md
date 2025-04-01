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
### *Functional Requirements*


# *Design*

### **Gantt Chart**
\
hi

### **Harry Potter Structure Chart**
\
![Harry_Potter_Structure_Chart](/images/Harry%20Potter%20Structure%20Chart.png "Harry Potter Structure Chart")

<u>Harry Potter Structure Chart Pseudocode</u>

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
END main()\

### **Algorithms**
\
![Harry_Potter_Algorithms](/images/Harry%20Potter%20Algorithm.png "Harry Potter Algorithms")


# Data dictonary

| Variable | Data Type | Format for Display | Size in Bytes | Size for Display | Description | Example | Validation |
|----------|-----------|--------------------|---------------|------------------|-------------|---------|------------|
|Spell name|String|Text|50|50|The name of the spell|Obliviate|Must be a non-empty string|
|Description|String|Text|100|100|What the spell does after being cast|Erases the target's memory|Must be a non-empty string|


# *Development*
----
---
---
---
---