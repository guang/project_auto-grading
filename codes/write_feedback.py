"""     @author:        Guang Yang
        @mktime:        10/02/2014
        @description:   functions used to write the feedback file for students
"""
import os.path
import textwrap


def generate_file_name(section, lab, s_name):
    """ generate file name (string) based on student information """
    s_name = s_name.lower().split(" ")  # [FirstName, LastName]
    return "sec{0}_lab{1}_{2}-{3}.txt".format(section, lab, s_name[0],
                                              s_name[1])


def new_file(section, lab, s_name, file_name, grader):
    """ create new file based on student information (if not already there)
    """
    new_file_boilerplate = ("Name: {0}\nSection: {1}\nLab: {2}\nGrader: {3}\n"
                            "".format(s_name, section, lab, grader))
    if os.path.isfile(file_name):
        return
    else:
        with open(file_name, 'w') as f:
            f.write(new_file_boilerplate)


def add_section_name_to_file(file_name, section_name):
    """ Adds section name to the file based on the section number given:
        'mc' is multiple choice,
        'ts' is test selection,
        'da' is data analysis,
        'ac' is additional comments
    """
    section_dict = {'mc': "\n\nMultiple Choices\n",
                    'ts': "\n\nTest Selection\n",
                    'da': "\n\nData Analysis\n",
                    'ac': "\n\nAdditional Comments\n"}
    with open(file_name, 'a') as f:
        f.write(section_dict[section_name])


def add_feedback_to_file(file_name, question_num, feedback_content, points_off):
    """ open existing file, append feedback and points off, then close it

    Args:
        section (int):              student's section number
        lab (int):                  student's lab number
        s_name (list):              student's first and last name
        question_num (str):         question number and part number
        feedback_content (str):     content of the feedback
        points_off (int):           point to be taken off for the question

    Returns:
        None

    Example:
        >>> add_feedback("sec1_lab1_yang-guang", "1d", "Hahahaha noob", 5)
    """
    feedback_content = textwrap.wrap(feedback_content)
    with open(file_name, 'a') as f:
        f.write("\n-- question {0} (-{1} points) --"
                "\n".format(question_num, points_off))
        for i in feedback_content:
            f.write("{0}\n".format(i))


def add_final_score(file_name, score):
    """ add final score
    """
    with open(file_name, 'a') as f:
        f.write("\nYour final score is {0}".format(score))
