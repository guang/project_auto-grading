"""     @author:        Guang Yang
        @mktime:        9/27/2014
        @description:   solution bank for multiple choice and data analysis
"""


def solution_mult_choice(lab):
    """ solution bank multiple choice section for all 4 labs """
    # lab 1
    lab1_sol = {
        "1a": "The correct answer is E.\nThis is explanation for 1a",
        "1b": "The correct answer is E.\nThis is explanation for 1b",
        "1c": "The correct answer is E.\nThis is explanation for 1c",
        "1d": "The correct answer is E.\nThis is explanation for 1d",
    }

    # lab 2
    lab2_sol = {
    }

    # lab 3
    lab3_sol = {
    }

    # lab 4
    lab4_sol = {
    }

    solution_dict = (lab1_sol, lab2_sol, lab3_sol, lab4_sol)

    return solution_dict[lab-1]


def solution_data_analysis(lab):
    """ solution bank for data analysis section for all 4 labs

    Many layers: 1) lab number (lab1_sol), 2) question_key (2a),
    3) error_key (wrong_date), 4) actual content and points off in a tuple
    """
    # lab 1
    lab1_sol = {
        '2a': {
            'wrong_date': (
                "The date is incorrect, check again", 2
            ),
            'wrong_blah': (
                "The blah is wrong, maybe consider doing the assignment again"
                "blah blah blah lololz", 1
            ),
        },
        '3a': {
        }
    }

    # lab 2
    lab2_sol = {
    }

    # lab 3
    lab3_sol = {
    }

    # lab 4
    lab4_sol = {
    }

    solution_dict = (lab1_sol, lab2_sol, lab3_sol, lab4_sol)

    return solution_dict[lab-1]
