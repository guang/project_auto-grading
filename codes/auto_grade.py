"""     @author:        Guang Yang
        @mktime:        9/25/2014
        @description:   main file to do the semi-automated grading for 203
"""
from write_feedback import *    # NOQA
from db_connect import *        # NOQA


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
    add_section_name_to_file(file_name, 'mc')
    not_done = True
    points_off = 5

    while not_done:
        question_num = input("(multiple choice) Enter question number"
                             " (or type done): ")
        if question_num == 'done':
            not_done = False
            print("Exiting multiple choice section")
            return score
        else:
            error_name = input("(multiple choice) Enter error name: ")
            dict_key = "{0}{1}".format(question_num, error_name)
            try:
                feedback_content = get_mc_feedback(LAB, question_num,
                                                   error_name)
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
    add_section_name_to_file(file_name, 'da')
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


if __name__ == "__main__":
    SECTION = 1
    LAB = 1
    GRADER = "Guang Yang (gy8@berkeley.edu)"
    S_NAME = "Guang Yang"  # input("Student Name: ")
    FILE_NAME = generate_file_name(SECTION, LAB, S_NAME)
    score = 100

    new_file(SECTION, LAB, S_NAME, FILE_NAME)
    score = mult_choice(FILE_NAME, score)
    # score = data_analysis(FILE_NAME, score)
