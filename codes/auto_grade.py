"""     @author:        Guang Yang
        @mktime:        9/25/2014
        @description:   main file to do the semi-automated grading for 203
"""
from write_feedback import *    # NOQA (this is a pylint bug, please ignore)
from db_connect import *        # NOQA
from write_summary import *     # NOQA


def mult_choice(file_name, score):
    """ automating the process for grading multiple choices

    User is asked to provide a string (no space) of answers from student. We
    then loop through each of the answers, trying to pull the feedback from our
    solutions database (unless answer is correct, in which case we just skip).

    Args:
        file_name (str):        name of the file being edited
        score (int):            current score for the student

    Returns:
        score (int):            score after taking points off for wrong answers
    """
    add_section_name_to_file(file_name, 'mc')
    points_off = 4
    perfect_score = score

    answers_raw = input("(multiple choice) Enter answer sequence: ").lower()
    answers_list = list(answers_raw)
    print("Processing {0} answers".format(len(answers_list)))

    for ind, error_name in enumerate(answers_list):
        question_num = ind + 1
        try:
            feedback_content = get_mc_feedback(LAB, question_num, error_name)
            add_feedback_to_file(file_name, question_num, feedback_content,
                                 points_off)
            dict_key = "{0}{1}".format(question_num, error_name)
            print("Successfully added feedback {0}".format(dict_key))
            score -= points_off
        except TypeError:
            pass
    if score == perfect_score:
        add_goodjob_to_file(file_name)
    return score


def test_selection(file_name, score):
    """ automating the process for grading test selection

    User is asked to provide a string (no space) of answers from student. We
    then loop through each of the answers, trying to pull the feedback from our
    solutions database (unless answer is correct, in which case we just skip).

    Args:
        file_name (str):        name of the file being edited
        score (int):            current score for the student

    Returns:
        score (int):            score after taking points off for wrong answers
    """
    add_section_name_to_file(file_name, 'ts')
    points_off = 5
    perfect_score = score

    answers_raw = input("(test selection) Enter answer sequence: ").lower()
    answers_list = list(answers_raw)
    print("Processing {0} answers".format(len(answers_list)))

    for ind, error_name in enumerate(answers_list):
        question_num = ind + 1
        try:
            feedback_content = get_ts_feedback(LAB, question_num, error_name)
            add_feedback_to_file(file_name, question_num, feedback_content,
                                 points_off)
            dict_key = "{0}{1}".format(question_num, error_name)
            print("Successfully added feedback {0}".format(dict_key))
            score -= points_off
        except TypeError:
            pass
    if score == perfect_score:
        add_goodjob_to_file(file_name)
    return score


def data_analysis(file_name, score):
    """ automating the process for grading data analysis

    Args:
        file_name (str):        name of the file being edited
        score (int):            current score for the student

    Returns:
        score (int):            score after taking points off for wrong answers
    """
    perfect_score = score

    add_section_name_to_file(file_name, 'da')
    not_done = True
    while not_done:
        question_num = input("(data analysis) Enter question number"
                             "(or type 'done'): ")
        if question_num == 'done':
            not_done = False
            if score == perfect_score:
                add_goodjob_to_file(file_name)
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
                while is_save not in ('y', 'n'):
                    mode_new_msg = ("-- recording answer for lab {0} question "
                                    "{1} part {2}: {3} --\n"
                                    "".format(LAB, question_num, part_name,
                                              error_name))
                    feedback_new = input(mode_new_msg)
                    points_off_new = int(input("how many points to be "
                                               "taken off? "))
                    is_save = input("Save the answer to database (y/n/c)? ")
                    if is_save in ('y', 'n'):
                        question_and_part = "{0}{1}".format(question_num,
                                                            part_name)
                        if is_save == 'y':
                            flag = add_da_feedback(LAB, question_num, part_name,
                                                   error_name, feedback_new,
                                                   points_off_new)
                            print(flag)
                        add_feedback_to_file(file_name, question_and_part,
                                             feedback_new, points_off_new)
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
    SECTION = 1
    LAB = 3
    GRADER = "Guang Yang (gy8@berkeley.edu)"
    S_NAME = input("Student Name: ")
    FILE_NAME = generate_file_name(SECTION, LAB, S_NAME)
    score = 100

    new_file(SECTION, LAB, S_NAME, FILE_NAME, GRADER)
    score = mult_choice(FILE_NAME, score)
    score = test_selection(FILE_NAME, score)
    score = data_analysis(FILE_NAME, score)
    additional_comments(FILE_NAME)
    add_final_score(FILE_NAME, score)
    write_summary_score(LAB, SECTION, S_NAME, score)
