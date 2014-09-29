"""     @author:        Guang Yang
        @mktime:        9/27/2014
        @description:   solution keys for the multiple choice section for
                        different labs
"""


def solution_mult_choice(lab):
    """ solution bank for all 4 labs """
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
