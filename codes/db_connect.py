"""     @author:        Guang Yang
        @mktime:        10/02/2014
        @description:   functions to communicate with database
"""

import sqlite3 as lite


def get_mc_feedback(lab_num, question_num, error_name):
    """ get feedback from database based on lab, question and the error

    Args:
        lab_num (int):          lab number
        question_num (int):     question number
        error_name (str):       error name

    Returns:
        feedback (str):         raw feedback in string (no line breaks)
    """
    con = lite.connect('solutions.db')

    with con:
        cur = con.cursor()
        cur.execute("SELECT feedback FROM MC WHERE lab_num=? AND question_num=?"
                    " AND error_name=?", (lab_num, question_num, error_name))
        feedback = cur.fetchone()
    return feedback[0]


def show_da_feedback(lab_num, question_num, part_name):
    """ show all feedbacks for a part of question on a lab.

    Args:
        lab_num (int):              lab number
        question_num (int):         question number
        part_name (str):            part name (a, b, c, d)

    Returns:
        feedback_list (list):       a list of feedbacks for the question
    """
    con = lite.connect('solutions.db')

    with con:
        cur = con.cursor()
        cur.execute("SELECT error_name, feedback FROM DA WHERE lab_num=? AND "
                    "question_num=? AND part_name=?", (lab_num, question_num,
                                                       part_name))
        feedback_list = cur.fetchall()
    return feedback_list


def pull_da_feedback(lab_num, question_num, part_name, error_name):
    """ pull requested feedback (data analysis) from the database

    Args:
        lab_num (int):              lab number
        question_num (int):         question number
        part_name (str):            part name (a, b, c, d)
        error_name (str):           identifier for the error

    Returns:
        feedback (str):             content of the feedback
        points_off (int):           amount of points taken off
    """
    con = lite.connect('solutions.db')

    with con:
        cur = con.cursor()
        cur.execute("SELECT feedback, points_off FROM DA WHERE lab_num=? AND "
                    "question_num=? AND part_name=? AND error_name=?",
                    (lab_num, question_num, part_name, error_name))
        feedback_and_points = cur.fetchone()

    return feedback_and_points


def add_da_feedback(lab_num, question_num, part_name, error_name, feedback,
                    points_off):
    """ add new feedback into the data base

    Args:
        lab_num (int):              lab number
        question_num (int):         question number
        part_name (str):            part name (a, b, c, d)
        error_name (str):           identifier for the error
        points_off (int):           points to be taken off for the feedback

    Returns:
        feedback (str):             content of the feedback
        points_off (int):           amount of points taken off
    """
    con = lite.connect('solutions.db')

    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO DA VALUES({0}, {1}, '{2}', '{3}', '{4}', {5})"
                    "".format(lab_num, question_num, part_name, error_name,
                              feedback, points_off))
        success_msg = ("Successfully added {0} for question {1}{2} to database"
                       "".format(error_name, question_num, part_name))
    return success_msg
