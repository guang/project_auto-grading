Guang's Semi-automated Grader
====================

Semi-automated grading for UC Berkeley iSchool Data Science 203 in Fall 2014.

Comments and feedbacks are welcome at gy [AT] berkeley [DOT] edu

## Table of Contents
- [Overview](#overview)
  - [Dependencies](#dependencies)
  - [Usage](#usage)
- [Putting Solutions into Database](#putting-solutions-into-database)
- [Running the Grader Program](#modifying-assignment-metadata)
- [Postmortem Batch Editing](#postmortem-batch-editing)



## Overview
This semi-automated grading program aims to

- give students personalized feedbacks depending on the type of error they made for
  different questions on the assignment.

- save grader's time from having to repeat writing similar feedbacks for different students
  with similar kinds of errors.

- make feedbacks look more professional and be less error-prone by automating scorekeeping
  and typesetting the feedback file.


It is designed to handle two types
of homework questions with different methods of storing feedbacks:

- multiple choice - here the feedbacks have to be seeded to the database before grading starts.
  New feedbacks cannot be added during grading.

- free response - here the feedbacks do not have to be seeded into the database before
  grading. New feedbacks are added to the database as the grader find new errors while grading.

(Currently it is designed to handle 2 multiple choice sections (MC and TS) and 1 free
response section (DA). However this can be easily modified to handle more sections of each
case.

As you run the program, it communicates with the SQLite database (add or pull
feedbacks based on lab number, section name, question number, and the name of the error),
the program then writes the individualized feedbacks and calculated
final score to a .txt file with general information about the student and assignment.

After grading, if something needs to be changed (the feedback in the database was poorly
worded or just wrong), `batch_fix.py` enables you to make postmortem changes to every
student's individual feedback .txt file using regex to search and replace :trollface:.

### Dependencies
- [Python](https://www.python.org): 3.x

  This program is developed in Python 3.4 and does not provide backward compatibility to
  Python 2. (time to start using Python 3 :sunglasses:)

- SQLite

  I chose to implent the data I/O in SQL (easier to manipulate than python dictionaries,
  stricter schema requirements than JSON). Since data stores for feedbacks would be
  quite small, SQLite is the obvious choice here.

#### Required Python Modules
- sqlite3

  provides nice interfacing with sqlite database

- textwrap

  provides nice text wrapping when writing long feedbacks to file in nicely wrapped
  paragraphs.

### Getting Started

Once the solution database is seeded (see instructions below) and saved as `solutions.db`,
you should check and make sure the general information (expressed in global vars) is correct
in `auto_grade.py`. If everything looks like you can just run

```
python3 auto_grade.py
```

and start grading away :ghost:




