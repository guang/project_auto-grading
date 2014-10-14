"""     @author:        Guang Yang
        @mktime:        10/12/2014
        @description:   Fix stuff/comments in batch after already grades are
                        already made
"""
import os
import re


# open and close file in all files in the specified lab directory
# def read_file(file_name):
#     """ read in the text files and make the changes
#     """
dummy1 = ('/Users/guangyang/Work/project_auto-grading/lab1/'
          'sec1_lab1_mak-arthur.txt')
dummy2 = ('/Users/guangyang/Work/project_auto-grading/lab1/'
          'sec1_lab1_kleemann-gunnar.txt')
dummy = dummy1


def mc_scoring(content):
    points_back = len(re.findall(r'(-- question [1-9]) \(', content))
    if points_back > 0:
        # change MC scores from 5 to 4
        content = re.sub(r'(-- question [1-9]) \(-5 points\)',
                         r'\1 (-4 points)',
                         content)
        # change final score
        current_score_raw = re.search(r'Your final score is ([0-9]{2,3})',
                                      content)
        current_score = int(current_score_raw.group(1))
        new_score = current_score + points_back
        content = re.sub(r'(Your final score is) [0-9]{2,3}',
                         r'\1 {0}'.format(new_score),
                         content)
    return(content)


def q6c(content):
    content = re.sub(r'(The correct answer is B.) Well this is.* need a',
                     r'\1 This is a known fact, CLT is more specific.',
                     content)
    content = re.sub(r'theorem to know this',
                     r'',
                     content)
    return(content)


def q7c(content):
    content = re.sub(r'(The correct answer is F.) It should.*they are',
                     r'\1 Notice that this is the distribution of the variable',
                     content)
    content = re.sub(r'talking about the sampling distribution.*rather',
                     (r', not the statistic. Therefore, we expect the standard '
                      r'deviation to stay '),
                     content)
    content = re.sub(r'than the sampling distribution of the mean',
                     r'roughly constant with sample size, not decrease to zero',
                     content)
    return(content)


def q7a(content):
    content = re.sub(r'(The correct answer is F.) This is very subtle.*andard',
                     r'\1 Variance should actually stay constant ',
                     content)
    content = re.sub(r'deviation is actually not an.*of the population',
                     r'with sample size',
                     content)
    content = re.sub(r'that the sample standard.*could move up or down in',
                     r'',
                     content)
    content = re.sub(r'expectation with increasing sample size\.',
                     r'',
                     content)
    return(content)


def q1a(content):
    content = re.sub(r'(The correct answer is E.) The variable is.*tbe',
                     r'\1 Remember that intervals have different lengths',
                     content)
    content = re.sub(r'^interval$',
                     r'',
                     content)
    return(content)


if __name__ == "__main__":
    pass
    LAB = 1
    sections = [1, 2, 3, 4, 5]

    for i_sec in sections:
        path_name = ("/Users/guangyang/Work/project_auto-grading/"
                     "lab{0}/lab{0}_sec{1}".format(LAB, i_sec))
        files = os.listdir(path_name)
        if '.DS_Store' in files:
            files.remove('.DS_Store')

        for i_file in files:
            i_file_name = "{0}/{1}".format(path_name, i_file)
            with open(i_file_name, 'r') as f:
                content = f.read()
            content = mc_scoring(content)
            content = q6c(content)
            content = q7c(content)
            content = q7a(content)
            content = q1a(content)
            with open(i_file_name, 'w') as f:
                f.write(content)
                print(i_file_name)
