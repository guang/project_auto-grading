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
