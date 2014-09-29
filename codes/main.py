"""     @author:        Guang Yang
        @mktime:        9/25/2014
        @description:   main file to do the semi-automated grading for 203
"""
from solution_mult_choice import *  # NOQA
import os.path

GRADER = "Guang Yang (gy8@berkeley.edu)"


def mult_choice(file_name):
    """ automating the process for grading multiple choices

    while the user input is not "done", we ask user for 1) question number and
    2) error number. We combine these two strings into a dictionary key to pull
    data from the solutions
    """
    not_done = True
    solution = solution_mult_choice(LAB)

    while not_done:
        question_num = input("(multiple choice) Enter question number"
                             "(or type done): ")
        if question_num == 'done':
            not_done = False
            print("Exiting multiple choice section")
        else:
            error_num = input("(multiple choice) Enter error number: ")
            dict_key = "{0}{1}".format(question_num, error_num)
            try:
                feedback_content = solution[dict_key]
                add_feedback_to_file(file_name, question_num,
                                     feedback_content)
                print("Successfully added feedback {0}".format(dict_key))
            except KeyError:
                print("Not a valid key")


def data_analysis():
    """ automating the process for grading data analysis """


def add_feedback_to_file(file_name, question_num, feedback_content):
    """ open existing file, append feedback, then close it

    Args:
        section (int):              student's section number
        lab (int):                  student's lab number
        s_name (list):              student's first and last name
        question_num (str):         question number and wrong answer choice
        feedback_content (str):     content of the feedback

    Returns:
        None

    Example:
        >>> add_feedback(3, 1, "Guang Yang", "1d", "Hahahaha noob")
    """
    with open(file_name, 'a') as f:
        f.write("\n-- {0} --\n{1}".format(question_num, feedback_content))


def add_section_name_to_file(section_name):
    pass


def new_file(section, lab, s_name, file_name):
    """ create new file based on student information if not already there """
    new_file_boilerplate = "Name: {0}\nSection: {1}\nLab: {2}\n".format(s_name,
                                                                        lab,
                                                                        section)
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
    FILE_NAME = generate_file_name(SECTION, LAB, S_NAME)
    new_file(SECTION, LAB, S_NAME, FILE_NAME)
    mult_choice(FILE_NAME)
