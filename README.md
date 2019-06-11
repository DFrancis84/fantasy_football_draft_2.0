# Draft.py
---
## To install:
`git clone git@github.com:DFrancis84/fantasy_football_draft.git`
## Required imports:
1. sqlite3
2. pyfiglet `pip install pyfiglet`
3. prettytable `pip install prettytable`
---
### What is draft.py?
Draft.py is an open source program that I created for my fantasy football league.  We prefer to do live drafts and instead of having to write all the data down on a piece of paper, I decicded to write this program. It is very simple to use! 

### How to use draft.py?
To use draft.py:
1. Clone draft.py onto your local machine
2. CD into directory
3. enter `python3 draft.py`
4. Screen will first prompt you to enter your league name
    * This is used to create the `.db` file for the designated league name
5. The next prompt will ask for the amount of teams in the league followed by a prompt to ask for number of rounds in the league.
    * This is used for the base functionality of draft.py.  It will take number of teams and multiply by number of rounds and output how many picks will take place in total for the draft.
    * It also utilizes the number teams input by outputing a table every round completion based on number of teams entered.
6. Go through the entire draft entering the prompts as they appear.  With each entry, draft.py will store that data to a sqlite database for you to use to enter the results into your desired fantasy football host.
7. After the final pick has been selected, it will output a table with every pick made for the draft, while finalizing the created database for easy querying.
---
### Schema for sqlite database:
- pick - _INTEGER_ ***Primary Key, AutoIncrement***
- team - _TEXT_
- player Name - _TEXT_
- position - _TEXT_
---
### What's next?
With the base of the program live, there are a few more things that I want to add to the program.  They are as follows:
1. Would like to query against the database and prevent user from being able to enter the same name twice
2. To piggyback off of #2, Would like to be able to have the list of ALL players loaded to where you can ensure that you have the right names, and possibly even be able to select from said list
