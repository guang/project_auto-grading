Guang's Semi-automated Grader
====================

Semi-automated grading for UC Berkeley iSchool Data Science 203 in Fall 2014.
Comments and feedbacks are welcome at gy8@berkeley.edu

## Table of Contents
- [Overview](#overview)
  - [Dependencies](#dependencies)
  - [Usage](#usage)
- [Putting Solutions into Database](#putting-solutions-into-database)
- [Running the Grader Program](#modifying-assignment-metadata)
- [Postmortem Batch Editing](#postmortem-batch-editing)



## Overview
This grader program aims to give students personalized feedbacks depending on the type of
errors they made for different question on the assignment. It is designed for two types
of homework questions with different methods of storing feedbacks:

- multiple choice - here the feedbacks are seeded to the database before grading starts
- free response - here feedbacks for new errors are added to the database as the user
  find them while grading.

As you run the program, it communicates with the SQLite database (add or pull
feedbacks based on question
and error type), the program then writes the individualized feedbacks and calculated
final score to a .txt file with general information about the student and assignment.

After grading, if something need to be changed (the feedback in the database was poorly
worded or wrong), this grader program enables you to make postmortem changes to every
student's individual feedback .txt file using regex to search and replace.

### Dependencies
This program is developed in Python 3.4 and does not provide compatibility to Python 2.
(time to start using Python 3 :sunglasses:)

[Python](https://www.python.org): 3.x

### Usage

Once the solution database is seeded (see instructions below) and saved as `solutions.db`,
you should check and make sure the general information (expressed in global vars) is correct
in `auto_grade.py`. If everything looks like you can just run

```
python3 auto_grade.py
```

and start grading away "ghost:




