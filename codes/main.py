"""     @author:        Guang Yang
        @mktime:        9/25/2014
        @description:   main file to do the semi-automated grading for 203
"""
from solution import *  # NOQA
import os.path


def mult_choice(file_name, score):
    """ automating the process for grading multiple choices

    while the user input is not "done", we ask user for 1) question number and
    2) error number. We combine these two strings into a dictionary key to pull
    data from the solutions

    Args:
        file_name (str):        name of the file being edited
        score (int):            current score for the student

    Returns:
        score (int):            score after taking points off for wrong answers
    """
    add_section_name_to_file(file_name, 1)
    not_done = True
    solution = solution_mult_choice(LAB)
    points_off = 5

    while not_done:
        question_num = input("(multiple choice) Enter question number"
                             " (or type done): ")
        if question_num == 'done':
            not_done = False
            print("Exiting multiple choice section")
            return score
        else:
            error_num = input("(multiple choice) Enter error number: ")
            dict_key = "{0}{1}".format(question_num, error_num)
            try:
                feedback_content = solution[dict_key]
                add_feedback_to_file(file_name, question_num,
                                     feedback_content, points_off)
                print("Successfully added feedback {0}".format(dict_key))
                score = score - 5
            except KeyError:
                print("Not a valid dictionary key")


def data_analysis(file_name, score):
    """ automating the process for grading data analysis

    Args:
        file_name (str):        name of the file being edited
        score (int):            current score for the student

    Returns:
        score (int):            score after taking points off for wrong answers
    """
    add_section_name_to_file(file_name, 2)
    not_done = True
    solution_lab = solution_data_analysis(LAB)
    while not_done:
        question_num = input("(data analysis) Enter question number"
                             "(or type 'done'): ")
        if question_num == 'done':
            not_done = False
            print("Exiting data analysis section")
            return score
        else:
            solution_question = solution_lab[question_num]
            error_key = input("Enter error key (or type 'show'): ")
            if error_key == 'show':
                # ToDo: pretty print this
                print(solution_question)
            user_mode = input("please choose edit mode"
                              " ('pull' or 'edit'): ")
            if user_mode == 'pull':
                feedback_content = solution_question[error_key][0]
                points_off = solution_question[error_key][1]
                add_feedback_to_file(file_name, question_num,
                                     feedback_content, points_off)
                score = score - points_off
            # ToDo: implement branch for editing and saving feedback
            else:
                pass


def add_feedback_to_file(file_name, question_num, feedback_content, points_off):
    """ open existing file, append feedback and points off, then close it

    Args:
        section (int):              student's section number
        lab (int):                  student's lab number
        s_name (list):              student's first and last name
        question_num (str):         question number and wrong answer choice
        feedback_content (str):     content of the feedback
        points_off (int):           point to be taken off for the question

    Returns:
        None

    Example:
        >>> add_feedback("sec1_lab1_yang-guang", "1d", "Hahahaha noob", 5)
    """
    with open(file_name, 'a') as f:
        f.write("\n-- question {0} ({2} points) --"
                "\n{1}\n".format(question_num, feedback_content, points_off))


def add_section_name_to_file(file_name, section_num):
    """ Adds section name to the file based on the section number given:
        1 is multiple choice,
        2 is data analysis,
        3 is general questions
    """
    section_dict = {1: "\n\nMultiple Choices",
                    2: "\n\nData Analysis",
                    3: "\n\nAdditional Comments"}
    with open(file_name, 'a') as f:
        f.write(section_dict[section_num])


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
    GRADER = "Guang Yang (gy8@berkeley.edu)"
    S_NAME = "Guang Yang"  # input("Student Name: ")
    FILE_NAME = generate_file_name(SECTION, LAB, S_NAME)
    score = 100

    new_file(SECTION, LAB, S_NAME, FILE_NAME)
    # score = mult_choice(FILE_NAME, score)
    score = data_analysis(FILE_NAME, score)
