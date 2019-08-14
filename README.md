# Logs analysis project

## Project summary
#### It is internal reporting tool that will use information from database to discover:
* What are the most popular three articles of all time?
* Who are the most popular article authors of all time?
* On which days did more than 1% of requests lead to errors?

## Pre-Requisites and Preparation
* Python 2.7
* PSQL database

## Prepare the Vagrant VM
Clone the [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository. There is a catalog folder provided for you, but no files have been included. If a catalog folder does not exist, simply create your own inside of the vagrant folder.

* Launch the Vagrant VM (by typing `vagrant up` in the directory fullstack/vagrant from the terminal).
* Logging into the Linux VM with (by typing `vagrant ssh`from the terminal).

## Download the data
Download [the data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.

To build the reporting tool, you'll need to load the site's data into your local database.

To load the data, cd into the vagrant directory and use the command `psql -d news -f newsdata.sql`.

## Downlaod the project 

#### Fork the starter repo
log into your personal Github acccount, and fork  [GitHub: udacity\_Project\_1](https://github.com/Michsedki/udacity_Project_1)


#### Clone the remote to your local machine
From terminal,run this command(replace `<UserName>` with your GitHub username):
`git clone https://github.com/<UserName>/udacity_Project_1 news_data_analysis`

#### Put this file into the vagrant directory, which is shared with your virtual machine.


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







