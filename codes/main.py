"""     @author:        Guang Yang
        @mktime:        9/25/2014
        @description:   main file to do the semi-automated grading for 203
"""
from solution_mult_choice import *  # NOQA
import os.path

GRADER = "Guang Yang (gy8@berkeley.edu)"


def mult_choice():
    """ automating the process for grading multiple choices """
    not_done = True
    solution = solution_mult_choice(LAB)
    while not_done:
        prompt = ("Enter question number and wrong answer for multiple choice"
                  "(i.e. 1c or 5a) \n")
        if prompt == 'done':
            return
        else:
            feedback_num = input(prompt)
            try:
                feedback_content = solution[feedback_num]
                add_feedback_to_file(SECTION, LAB, S_NAME, feedback_num,
                                     feedback_content)
            except KeyError:
                print("Not a valid key")


def add_feedback_to_file(section, lab, s_name, feedback_num, feedback_content):
    """ open existing file, append feedback, then close it

    Args:
        section (int):              student's section number
        lab (int):                  student's lab number
        s_name (list):              student's first and last name
        feedback_num (str):         question number and wrong answer choice
        feedback_content (str):     content of the feedback

    Returns:
        None

    Example:
        >>> add_feedback(3, 1, "Guang Yang", "1d", "Hahahaha noob")
    """


def new_file(section, lab, s_name):
    """ create new file based on student information if not already there """
    new_file_boilerplate = "Name: {0}\nSection: {1}\nLab: {2}\n".format(s_name,
                                                                        lab,
                                                                        section)
    file_name = generate_file_name(section, lab, s_name)
    if os.path.isfile(file_name):
        return
    else:
        with open(file_name, 'w') as f:
            f.write(new_file_boilerplate)


def generate_file_name(section, lab, s_name):
    """ generate file name (string) based on student information """
    s_name = s_name.lower().split(" ")  # [FirstName, LastName]
    return "sec{0}_lab{1}_{2}-{3}.txt".format(section, lab, s_name[1],
                                              s_name[0])


if __name__ == "__main__":
    SECTION = 1
    LAB = 1
    S_NAME = "Guang Yang"  # input("Student Name: ")
    new_file(SECTION, LAB, S_NAME)
    # mult_choice()
