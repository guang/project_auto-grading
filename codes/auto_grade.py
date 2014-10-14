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
    points_off = 4

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
            feedback_content = get_mc_feedback(LAB, question_num,
                                               error_name)
            add_feedback_to_file(file_name, question_num,
                                 feedback_content, points_off)
            print("Successfully added feedback {0}".format(dict_key))
            score = score - 5


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
    while not_done:
        question_num = input("(data analysis) Enter question number"
                             "(or type 'done'): ")
        if question_num == 'done':
            not_done = False
            print("Exiting data analysis section")
            return score
        else:
            part_name = input("Enter part number: ")
            feedback_list = show_da_feedback(LAB, question_num, part_name)
            if feedback_list:
                for i in feedback_list:
                    print("\nerror_name: {0}\nfeedback: {1}".format(i[0], i[1]))
            else:
                print("no feedbacks currently exist for this question/part")
            error_name = input("what's the error name? ")
            user_mode = input("(pull) from existing or write (new) entry: ")
            if user_mode == 'pull':
                feedback_and_points = pull_da_feedback(LAB, question_num,
                                                       part_name, error_name)
                feedback = feedback_and_points[0]
                points_off = feedback_and_points[1]
                question_and_part = "{0}{1}".format(question_num, part_name)
                add_feedback_to_file(file_name, question_and_part, feedback,
                                     points_off)
                score = score - points_off
                print("Successfully added feedback for question {0}{1}"
                      "".format(question_num, part_name))
            elif user_mode == 'new':
                is_save = False
                while is_save != 'yes':
                    mode_new_msg = ("-- recording answer for lab {0} question "
                                    "{1} part {2}: {3} --\n"
                                    "".format(LAB, question_num, part_name,
                                              error_name))
                    feedback_new = input(mode_new_msg)
                    points_off_new = int(input("how many points to be "
                                               "taken off? "))
                    is_save = input("Save the answer to database (yes)? ")
                    if is_save == "yes":
                        question_and_part = "{0}{1}".format(question_num,
                                                            part_name)
                        flag = add_da_feedback(LAB, question_num, part_name,
                                               error_name, feedback_new,
                                               points_off_new)
                        add_feedback_to_file(file_name, question_and_part,
                                             feedback_new, points_off_new)
                        print(flag)
                        score = score - points_off_new
            else:
                print("action was not specified, exiting")


def additional_comments(file_name):
    """ automating the process for adding additional comments

    Args:
        file_name (str):        name of the file being edited
    """
    add_section_name_to_file(file_name, 'ac')
    is_save = False
    while is_save != 'yes':
        feedback = input("-- recording additional comments --\n")
        is_save = input("Save the answer (yes)? ")
        if is_save == 'yes':
            add_feedback_to_file(file_name, 'feedback', feedback, 0)


if __name__ == "__main__":
    SECTION = 5
    LAB = 1
    GRADER = "Guang Yang (gy8@berkeley.edu)"
    S_NAME = input("Student Name: ")
    FILE_NAME = generate_file_name(SECTION, LAB, S_NAME)
    score = 100

    new_file(SECTION, LAB, S_NAME, FILE_NAME, GRADER)
    score = mult_choice(FILE_NAME, score)
    score = data_analysis(FILE_NAME, score)
    additional_comments(FILE_NAME)
    add_final_score(FILE_NAME, score)
