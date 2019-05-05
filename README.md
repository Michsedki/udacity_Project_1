#Logs analysis project

## Project summary
####It is internal reporting tool that will use information from database to discover:
* What are the most popular three articles of all time?
* Who are the most popular article authors of all time?
* On which days did more than 1% of requests lead to errors?

## Pre-Requisites and Preparation
* Python 2.7
* PSQL database


## Downlaod the project 

#### Fork the starter repo
log into your personal Github acccount, and fork  [GitHub: udacity\_Project\_1](https://github.com/Michsedki/udacity_Project_1)


#### Clone the remote to your local machine
From terminal,run this command(replace `<UserName>` with your GitHub username):
`git clone https://github.com/<UserName>/udacity_Project_1 news_data_analysis`

#### Copy this file news\_data\_analysis.py to your database directory.


## How to Use
* Open new terminal, and move to your database directory.
* Run the project file using python: write this command in your terminal `python news_data_analysis.py`

#### the project will print the reults in the terminal like that: 
```
First report: What are the most popular three articles of all time?
"Candidate is jerk, alleges rival" - 338647 Views
"Bears love berries, alleges bear" - 253801 Views
"Bad things gone, say good people" - 170098 Views

Second report: Who are the most popular article authors of all time?
Ursula La Multa - 507594 Views

Third report: On which days did more than 1% of requests lead to errors?
Jul 17, 2016  -  2.26 % errors
```

## Code Design
#### The Project contains 3 files :

1. news\_data\_analysis.py (Source Code)
2. README.MD (This File)
3. result (Sample Output) 







