# README

## Schedule Optimizer

### Overview:
* CIS 422 Project 2
* Web application that outputs a customized hw schedule for the following week.
* Can be accessed here: https://cis422project2.herokuapp.com
* Members: Mason Olsen, Mapuana Maka, Ani Janardhan


### Packages:
* Python - Datetime
* Python - Copy


### Description:
The intended user will give information about upcoming assignments - including % of grade, estimated time to completion, personal priority score and due date - as well as break times and sleep times. Next, the user will select from certain preference options, which will customize the outputted schedule to match their study habits. A schedule will then be generated that fixes study times throughout the week for completing the various assignments. This app aims to bypass the stress of time management by giving the user a schedule to follow that works with their other commitments and puts them on a track to handle their responsibilities on time. 


### Breakdown:

This project is divided into three parts:

### Backend - Structure/Classes    
**Schedule Class:**    
Schedule object which initiates an empty schedule and employs methods for adding breaks, sleep times and assignments. The generate schedule method then populates the schedule with assignments based on functions define from the priority and matrix files (see below). Finally the create calendar method outputs the finalized schedule in html format for the frontend to handle.

**Assignment Class:**   
Standardized class for assignment objects which holds all pertinent data relevant to each assignment, specifically:  
* Name
* % of Grade
* Estimated time 
* Due Date
* User Priority Score

### Backend - Priority/Matrix-Fill
**Priority:**  
In order to prioritize which assignments to do first, certain elements are taken into account. The most obvious factor is due date, which accounts for 50% of a calculated "priority score" in all priority preference options. Different options prioritize the assignments differently, such as long sort, which gives a heavier weighting to longer assignments, or standard sort, which gives percentage of total grade a high weighting. Each of these priority factors are given a weighting and then summed together to create a final priority score for each assignment on a scale of 0-10. The assignments are then sorted in order from highest to lowest priority and passed off to the matrix-fill operation.  

**Matrix-Fill:**  
There are two options for populating the schedule with assignments. The work sessions can group assignments - which schedules assignments contiguously until completion - or split assignments - which schedules an assignment for an hour before switching to a different assignment. This should reflect different styles of working, as some people get bored easily and like to switch between tasks, while others like to work on one task only until its completed.

### Frontend - Web Server/Formatting
The website has step-by-step sequence that leads to the generated schedule output.

**Welcome Page**    
Welcome message with some info about what the application does.

**Add Assignments Page**
Allows the user to add details for as many assignments as they need for the upcoming week.

**Add Breaks Page**  
Allows the user to input breaks during which no assignments will be scheduled.

**Add Sleep Times**
Allows the user to input sleeping and waking times to determine what parts of the calendar week will be represented in the schedule.

**Preferences Page**   
Lets the user select preferences to match their study habits based on the priority and matrix-fill operations defined above. Generate schedule button at the bottom.

**Schedule Page**  
Final output is displayed, showcasing the following week and the times when each assignment has been scheduled.


