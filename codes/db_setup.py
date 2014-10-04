"""     @author:        Guang Yang
        @mktime:        9/27/2014
        @description:   solution bank for multiple choice and data analysis
"""


import sqlite3 as lite


def new_solutions_db():
    """ initializes a sqlite database called 'solutions.db', where solutions
    for all 4 labs are to be stored in 3 tables: mc, ts and da.
    - documentation only, executed in commandline sqlite -

    Schema:
        MC (multiple choice):
            lab number (int):           1,2,3,4
            question number (int):      1,2,3,4,5,...
            error_name (text):           'a','e',...
            feedback (text):             "The correct answer is A Teehee"

        TS (test selection):
            lab number (int):           1,2,3,4
            question number (int):      1,2,3,4,5,...
            error_name (text):           'a','e',...
            feedback (text):             "The correct answer is A Teehee"

        DA (data analysis):
            lab number (int):           1,2,3,4
            question number (int):      1,2,3,4,5,...
            part_name (text):            'a','c',...
            error_name (text):           'no_preprocess','wrong_test',...
            feedback (text)              "The correct answer should Teehee"
    """
    pass


def new_grades_db():
    """ initializes a sqlite database called 'grades.db', where grades for each
    student is stored
    - documentation only, executed in commandline sqlite -

    Schema:
        Grades:
            section number (int)
            lab number (int)
            student name (str)
            student score (int)
    """
    pass


def solution_mult_choice_lab1():
    """ solution bank for multiple choices (lab 1)- data are stored in a
    tuple where the format is (lab_num, question_num, error_name, feedback)

    Returns:
        mc_col (list):          list of tuples to be fed into sqlite database

    """
    mc_sol = []
    # lab1 q1
    mc_sol.append((1, 1, 'a', "The correct answer is E. The variable is "
                   "discrete, so it can'tbe interval"))
    mc_sol.append((1, 1, "b", "The correct answer is E. Dichotomous variables "
                   "are nomial with only categories or levels, which is not "
                   "the case here"))
    mc_sol.append((1, 1, "c", "The correct answer is E. Nominal variables "
                   "do not impose order, however here there is indeed order "
                   "from less to more"))
    mc_sol.append((1, 1, "1d", "The correct answer is E. Since ratio "
                   "variables are also continuous, it can't be the case here"))

    # lab1 q2
    mc_sol.append((1, 2, "b", "The correct answer is A. Dichotomous is binary"
                   ", not an interval variable"))
    mc_sol.append((1, 2, "c", "The correct answer is A. This is not clear "
                   "from just using a binary variable"))
    mc_sol.append((1, 2, "d", "The correct answer is A. This is not clear "
                   "from just using a binary variable"))
    mc_sol.append((1, 2, "e", "The correct answer is A. It's not clear what's "
                   "conceptual vs operational"))

    # lab1 q3
    mc_sol.append((1, 3, "a", "The correct answer is D. Not true - std "
                   "indeed gets 'stretched' by outliers"))
    mc_sol.append((1, 3, "b", "The correct answer is D. This was a little "
                   "tricky - the problem here is the use of 'any population'. "
                   "Let's demonstrate this by a counterexample. Say we have "
                   "two distributions, X which is normal distribution with "
                   "mean mu and standard deviation sigma, and Y which is a "
                   "constant distribution over the support of a singleton 5. "
                   "For X, it's clear that sampling a point from a normal "
                   "distribution has about 68%% chance of falling within one "
                   "standard deviation of the mean. However, since Y is a "
                   "singleton, the mean is 5 and variance is 0. As a result, "
                   "The chance of your sample falling within one standard "
                   "deviation of the mean is 100%%."))
    mc_sol.append((1, 3, "c", "The correct answer is D. Take the constant "
                   "to be 0 and it's very clear this is wrong"))

    # lab1 q4
    mc_sol.append((1, 4, "a", "The correct answer is B. This answer doesn't "
                   "make sense as there is no quota"))
    mc_sol.append((1, 4, "c", "The correct answer is B. Where is the social "
                   "network?"))
    mc_sol.append((1, 4, "d", "The correct answer is B. You need "
                   "probabilities to select clusters"))
    mc_sol.append((1, 4, "e", "The correct answer is B. But the prompt said "
                   "random"))
    mc_sol.append((1, 4, "f", "The correct answer is B. What's systematic "
                   "about it?"))

    # lab1 q5
    mc_sol.append((1, 5, "a", "The correct answer is C. "
                   "If we let X ~ N(50,sigma^2), we see that P(X>70) can be "
                   "expressed using Z = (X-50)/sigma. So P(X>70) is the same a"
                   "s P((X-50)/sigma > (70-50)/sigma), which is P(Z>(20/sigma)"
                   " which is then 1 - phi(20/sigma), where phi is the cdf of "
                   "the standard normal."
                   "Similarly if we let Y be 1/100 sum(X_j), j from 1 to 100 "
                   "we have then Y ~ N(50,sigma^2/100 and follow the above "
                   "calculations we arrive at the same answer"))
    mc_sol.append((1, 5, "b", "The correct answer is C. "
                   "If we let X ~ N(50,sigma^2), we see that P(X>70) can be "
                   "expressed using Z = (X-50)/sigma. So P(X>70) is the same a"
                   "s P((X-50)/sigma > (70-50)/sigma), which is P(Z>(20/sigma)"
                   " which is then 1 - phi(20/sigma), where phi is the cdf of "
                   "the standard normal."
                   "Similarly if we let Y be 1/100 sum(X_j), j from 1 to 100 "
                   "we have then Y ~ N(50,sigma^2/100 and follow the above "
                   "calculations we arrive at the same answer"))
    mc_sol.append((1, 5, "d", "The correct answer is C. "
                   "If we let X ~ N(50,sigma^2), we see that P(X>70) can be "
                   "expressed using Z = (X-50)/sigma. So P(X>70) is the same a"
                   "s P((X-50)/sigma > (70-50)/sigma), which is P(Z>(20/sigma)"
                   " which is then 1 - phi(20/sigma), where phi is the cdf of "
                   "the standard normal."
                   "Similarly if we let Y be 1/100 sum(X_j), j from 1 to 100 "
                   "we have then Y ~ N(50,sigma^2/100 and follow the above "
                   "calculations we arrive at the same answer"))

    # lab1 q6
    mc_sol.append((1, 6, "a", "The correct answer is B. "
                   "This is law of large numbers"))
    mc_sol.append((1, 6, "c", "The correct answer is B. "
                   "Well this is kind of obvious you don't need a theorem to "
                   "know this"))
    mc_sol.append((1, 6, "d", "The correct answer is B. "
                   "Not the central limit theorem"))

    # q7
    mc_sol.append((1, 7, "7b", "The correct answer is A. "
                   "Standard error of the mean is defined as s/sqrt(n) where n "
                   "is the sample size. So it will get smaller"))
    mc_sol.append((1, 7, "7c", "The correct answer is A. "
                   "It should actually be larger"))
    mc_sol.append((1, 7, "7d", "The correct answer is A. "
                   "Sampling doesn't alter inherent population distribution"))
    mc_sol.append((1, 7, "7e", "The correct answer is A. "
                   "That's not what central limit theorem tells us"))
    mc_sol.append((1, 7, "7f", "The correct answer is A. "
                   ""))

    # q8
    mc_sol.append((1, 8, "a", "The correct answer is D. "
                   "All three statistics are 30"))
    mc_sol.append((1, 8, "b", "The correct answer is D. "
                   "Yup it's a constant distribution, which is unimodal"))
    mc_sol.append((1, 8, "c", "The correct answer is D. "
                   "Yup constant distributions have 0 variance/std"))
    mc_sol.append((1, 8, "e", "The correct answer is D. "
                   "There's no errors so sure it's 0"))

    # q9
    mc_sol.append((1, 9, "a", "The correct answer is B. "
                   "Using Bayes theorem we can write P(H|A) = P(H) * P(A|H)/"
                   "P(A) Now we know that P(H)=0.01 (given), P(A|H)=1 (trick "
                   "coin has two heads so it always flips head), P(A)=0.51 "
                   "(trick coin has 2 heads)."))
    mc_sol.append((1, 9, "c", "The correct answer is B. "
                   "Using Bayes theorem we can write P(H|A) = P(H) * P(A|H)/"
                   "P(A) Now we know that P(H)=0.01 (given), P(A|H)=1 (trick "
                   "coin has two heads so it always flips head), P(A)=0.51 "
                   "(trick coin has 2 heads)."))
    mc_sol.append((1, 9, "d", "The correct answer is B. "
                   "Using Bayes theorem we can write P(H|A) = P(H) * P(A|H)/"
                   "P(A) Now we know that P(H)=0.01 (given), P(A|H)=1 (trick "
                   "coin has two heads so it always flips head), P(A)=0.51 "
                   "(trick coin has 2 heads)."))
    mc_sol.append((1, 9, "e", "The correct answer is B. "
                   "Using Bayes theorem we can write P(H|A) = P(H) * P(A|H)/"
                   "P(A) Now we know that P(H)=0.01 (given), P(A|H)=1 (trick "
                   "coin has two heads so it always flips head), P(A)=0.51 "
                   "(trick coin has 2 heads)."))

    return mc_sol


def solution_mult_choice_lab2():
    """ solution bank for multiple choices - data are stored in a tuple where
    the format is (lab_num, question_num, error_name, feedback)

    Returns:
        mc_col (list):          list of tuples to be fed into sqlite database

    """
    mc_sol = []
    # lab1 q1
    mc_sol.append((1, 1, 'a', "The correct answer is E. The variable is "
                   "discrete, so it can'tbe interval"))
    mc_sol.append((1, 1, "b", "The correct answer is E. Dichotomous variables "
                   "are nomial with only categories or levels, which is not "
                   "the case here"))
    mc_sol.append((1, 1, "c", "The correct answer is E. Nominal variables "
                   "do not impose order, however here there is indeed order "
                   "from less to more"))
    mc_sol.append((1, 1, "1d", "The correct answer is E. Since ratio "
                   "variables are also continuous, it can't be the case here"))

    # lab1 q2
    mc_sol.append((1, 2, "b", "The correct answer is A. Dichotomous is binary"
                   ", not an interval variable"))
    mc_sol.append((1, 2, "c", "The correct answer is A. This is not clear "
                   "from just using a binary variable"))
    mc_sol.append((1, 2, "d", "The correct answer is A. This is not clear "
                   "from just using a binary variable"))
    mc_sol.append((1, 2, "e", "The correct answer is A. It's not clear what's "
                   "conceptual vs operational"))

    # lab1 q3
    mc_sol.append((1, 3, "a", "The correct answer is D. Not true - std "
                   "indeed gets 'stretched' by outliers"))
    mc_sol.append((1, 3, "b", "The correct answer is D. This was a little "
                   "tricky - the problem here is the use of 'any population'. "
                   "Let's demonstrate this by a counterexample. Say we have "
                   "two distributions, X which is normal distribution with "
                   "mean mu and standard deviation sigma, and Y which is a "
                   "constant distribution over the support of a singleton 5. "
                   "For X, it's clear that sampling a point from a normal "
                   "distribution has about 68%% chance of falling within one "
                   "standard deviation of the mean. However, since Y is a "
                   "singleton, the mean is 5 and variance is 0. As a result, "
                   "The chance of your sample falling within one standard "
                   "deviation of the mean is 100%%."))
    mc_sol.append((1, 3, "c", "The correct answer is D. Take the constant "
                   "to be 0 and it's very clear this is wrong"))

    # lab1 q4
    mc_sol.append((1, 4, "a", "The correct answer is B. This answer doesn't "
                   "make sense as there is no quota"))
    mc_sol.append((1, 4, "c", "The correct answer is B. Where is the social "
                   "network?"))
    mc_sol.append((1, 4, "d", "The correct answer is B. You need "
                   "probabilities to select clusters"))
    mc_sol.append((1, 4, "e", "The correct answer is B. But the prompt said "
                   "random"))
    mc_sol.append((1, 4, "f", "The correct answer is B. What's systematic "
                   "about it?"))

    # lab1 q5
    mc_sol.append((1, 5, "a", "The correct answer is C. "
                   "If we let X ~ N(50,sigma^2), we see that P(X>70) can be "
                   "expressed using Z = (X-50)/sigma. So P(X>70) is the same a"
                   "s P((X-50)/sigma > (70-50)/sigma), which is P(Z>(20/sigma)"
                   " which is then 1 - phi(20/sigma), where phi is the cdf of "
                   "the standard normal."
                   "Similarly if we let Y be 1/100 sum(X_j), j from 1 to 100 "
                   "we have then Y ~ N(50,sigma^2/100 and follow the above "
                   "calculations we arrive at the same answer"))
    mc_sol.append((1, 5, "b", "The correct answer is C. "
                   "If we let X ~ N(50,sigma^2), we see that P(X>70) can be "
                   "expressed using Z = (X-50)/sigma. So P(X>70) is the same a"
                   "s P((X-50)/sigma > (70-50)/sigma), which is P(Z>(20/sigma)"
                   " which is then 1 - phi(20/sigma), where phi is the cdf of "
                   "the standard normal."
                   "Similarly if we let Y be 1/100 sum(X_j), j from 1 to 100 "
                   "we have then Y ~ N(50,sigma^2/100 and follow the above "
                   "calculations we arrive at the same answer"))
    mc_sol.append((1, 5, "d", "The correct answer is C. "
                   "If we let X ~ N(50,sigma^2), we see that P(X>70) can be "
                   "expressed using Z = (X-50)/sigma. So P(X>70) is the same a"
                   "s P((X-50)/sigma > (70-50)/sigma), which is P(Z>(20/sigma)"
                   " which is then 1 - phi(20/sigma), where phi is the cdf of "
                   "the standard normal."
                   "Similarly if we let Y be 1/100 sum(X_j), j from 1 to 100 "
                   "we have then Y ~ N(50,sigma^2/100 and follow the above "
                   "calculations we arrive at the same answer"))

    # lab1 q6
    mc_sol.append((1, 6, "a", "The correct answer is B. "
                   "This is law of large numbers"))
    mc_sol.append((1, 6, "c", "The correct answer is B. "
                   "Well this is kind of obvious you don't need a theorem to "
                   "know this"))
    mc_sol.append((1, 6, "d", "The correct answer is B. "
                   "Not the central limit theorem"))

    # q7
    mc_sol.append((1, 7, "7b", "The correct answer is A. "
                   "Standard error of the mean is defined as s/sqrt(n) where n "
                   "is the sample size. So it will get smaller"))
    mc_sol.append((1, 7, "7c", "The correct answer is A. "
                   "It should actually be larger"))
    mc_sol.append((1, 7, "7d", "The correct answer is A. "
                   "Sampling doesn't alter inherent population distribution"))
    mc_sol.append((1, 7, "7e", "The correct answer is A. "
                   "That's not what central limit theorem tells us"))
    mc_sol.append((1, 7, "7f", "The correct answer is A. "
                   ""))

    # q8
    mc_sol.append((1, 8, "a", "The correct answer is D. "
                   "All three statistics are 30"))
    mc_sol.append((1, 8, "b", "The correct answer is D. "
                   "Yup it's a constant distribution, which is unimodal"))
    mc_sol.append((1, 8, "c", "The correct answer is D. "
                   "Yup constant distributions have 0 variance/std"))
    mc_sol.append((1, 8, "e", "The correct answer is D. "
                   "There's no errors so sure it's 0"))

    # q9
    mc_sol.append((1, 9, "a", "The correct answer is B. "
                   "Using Bayes theorem we can write P(H|A) = P(H) * P(A|H)/"
                   "P(A) Now we know that P(H)=0.01 (given), P(A|H)=1 (trick "
                   "coin has two heads so it always flips head), P(A)=0.51 "
                   "(trick coin has 2 heads)."))
    mc_sol.append((1, 9, "c", "The correct answer is B. "
                   "Using Bayes theorem we can write P(H|A) = P(H) * P(A|H)/"
                   "P(A) Now we know that P(H)=0.01 (given), P(A|H)=1 (trick "
                   "coin has two heads so it always flips head), P(A)=0.51 "
                   "(trick coin has 2 heads)."))
    mc_sol.append((1, 9, "d", "The correct answer is B. "
                   "Using Bayes theorem we can write P(H|A) = P(H) * P(A|H)/"
                   "P(A) Now we know that P(H)=0.01 (given), P(A|H)=1 (trick "
                   "coin has two heads so it always flips head), P(A)=0.51 "
                   "(trick coin has 2 heads)."))
    mc_sol.append((1, 9, "e", "The correct answer is B. "
                   "Using Bayes theorem we can write P(H|A) = P(H) * P(A|H)/"
                   "P(A) Now we know that P(H)=0.01 (given), P(A|H)=1 (trick "
                   "coin has two heads so it always flips head), P(A)=0.51 "
                   "(trick coin has 2 heads)."))

    return mc_sol


def solution_mult_choice_lab3():
    """ solution bank for multiple choices - data are stored in a tuple where
    the format is (lab_num, question_num, error_name, feedback)

    Returns:
        mc_col (list):          list of tuples to be fed into sqlite database

    """
    mc_sol = []
    # lab1 q1
    mc_sol.append((1, 1, 'a', "The correct answer is E. The variable is "
                   "discrete, so it can'tbe interval"))
    mc_sol.append((1, 1, "b", "The correct answer is E. Dichotomous variables "
                   "are nomial with only categories or levels, which is not "
                   "the case here"))
    mc_sol.append((1, 1, "c", "The correct answer is E. Nominal variables "
                   "do not impose order, however here there is indeed order "
                   "from less to more"))
    mc_sol.append((1, 1, "1d", "The correct answer is E. Since ratio "
                   "variables are also continuous, it can't be the case here"))

    # lab1 q2
    mc_sol.append((1, 2, "b", "The correct answer is A. Dichotomous is binary"
                   ", not an interval variable"))
    mc_sol.append((1, 2, "c", "The correct answer is A. This is not clear "
                   "from just using a binary variable"))
    mc_sol.append((1, 2, "d", "The correct answer is A. This is not clear "
                   "from just using a binary variable"))
    mc_sol.append((1, 2, "e", "The correct answer is A. It's not clear what's "
                   "conceptual vs operational"))

    # lab1 q3
    mc_sol.append((1, 3, "a", "The correct answer is D. Not true - std "
                   "indeed gets 'stretched' by outliers"))
    mc_sol.append((1, 3, "b", "The correct answer is D. This was a little "
                   "tricky - the problem here is the use of 'any population'. "
                   "Let's demonstrate this by a counterexample. Say we have "
                   "two distributions, X which is normal distribution with "
                   "mean mu and standard deviation sigma, and Y which is a "
                   "constant distribution over the support of a singleton 5. "
                   "For X, it's clear that sampling a point from a normal "
                   "distribution has about 68%% chance of falling within one "
                   "standard deviation of the mean. However, since Y is a "
                   "singleton, the mean is 5 and variance is 0. As a result, "
                   "The chance of your sample falling within one standard "
                   "deviation of the mean is 100%%."))
    mc_sol.append((1, 3, "c", "The correct answer is D. Take the constant "
                   "to be 0 and it's very clear this is wrong"))

    # lab1 q4
    mc_sol.append((1, 4, "a", "The correct answer is B. This answer doesn't "
                   "make sense as there is no quota"))
    mc_sol.append((1, 4, "c", "The correct answer is B. Where is the social "
                   "network?"))
    mc_sol.append((1, 4, "d", "The correct answer is B. You need "
                   "probabilities to select clusters"))
    mc_sol.append((1, 4, "e", "The correct answer is B. But the prompt said "
                   "random"))
    mc_sol.append((1, 4, "f", "The correct answer is B. What's systematic "
                   "about it?"))

    # lab1 q5
    mc_sol.append((1, 5, "a", "The correct answer is C. "
                   "If we let X ~ N(50,sigma^2), we see that P(X>70) can be "
                   "expressed using Z = (X-50)/sigma. So P(X>70) is the same a"
                   "s P((X-50)/sigma > (70-50)/sigma), which is P(Z>(20/sigma)"
                   " which is then 1 - phi(20/sigma), where phi is the cdf of "
                   "the standard normal."
                   "Similarly if we let Y be 1/100 sum(X_j), j from 1 to 100 "
                   "we have then Y ~ N(50,sigma^2/100 and follow the above "
                   "calculations we arrive at the same answer"))
    mc_sol.append((1, 5, "b", "The correct answer is C. "
                   "If we let X ~ N(50,sigma^2), we see that P(X>70) can be "
                   "expressed using Z = (X-50)/sigma. So P(X>70) is the same a"
                   "s P((X-50)/sigma > (70-50)/sigma), which is P(Z>(20/sigma)"
                   " which is then 1 - phi(20/sigma), where phi is the cdf of "
                   "the standard normal."
                   "Similarly if we let Y be 1/100 sum(X_j), j from 1 to 100 "
                   "we have then Y ~ N(50,sigma^2/100 and follow the above "
                   "calculations we arrive at the same answer"))
    mc_sol.append((1, 5, "d", "The correct answer is C. "
                   "If we let X ~ N(50,sigma^2), we see that P(X>70) can be "
                   "expressed using Z = (X-50)/sigma. So P(X>70) is the same a"
                   "s P((X-50)/sigma > (70-50)/sigma), which is P(Z>(20/sigma)"
                   " which is then 1 - phi(20/sigma), where phi is the cdf of "
                   "the standard normal."
                   "Similarly if we let Y be 1/100 sum(X_j), j from 1 to 100 "
                   "we have then Y ~ N(50,sigma^2/100 and follow the above "
                   "calculations we arrive at the same answer"))

    # lab1 q6
    mc_sol.append((1, 6, "a", "The correct answer is B. "
                   "This is law of large numbers"))
    mc_sol.append((1, 6, "c", "The correct answer is B. "
                   "Well this is kind of obvious you don't need a theorem to "
                   "know this"))
    mc_sol.append((1, 6, "d", "The correct answer is B. "
                   "Not the central limit theorem"))

    # q7
    mc_sol.append((1, 7, "7b", "The correct answer is A. "
                   "Standard error of the mean is defined as s/sqrt(n) where n "
                   "is the sample size. So it will get smaller"))
    mc_sol.append((1, 7, "7c", "The correct answer is A. "
                   "It should actually be larger"))
    mc_sol.append((1, 7, "7d", "The correct answer is A. "
                   "Sampling doesn't alter inherent population distribution"))
    mc_sol.append((1, 7, "7e", "The correct answer is A. "
                   "That's not what central limit theorem tells us"))
    mc_sol.append((1, 7, "7f", "The correct answer is A. "
                   ""))

    # q8
    mc_sol.append((1, 8, "a", "The correct answer is D. "
                   "All three statistics are 30"))
    mc_sol.append((1, 8, "b", "The correct answer is D. "
                   "Yup it's a constant distribution, which is unimodal"))
    mc_sol.append((1, 8, "c", "The correct answer is D. "
                   "Yup constant distributions have 0 variance/std"))
    mc_sol.append((1, 8, "e", "The correct answer is D. "
                   "There's no errors so sure it's 0"))

    # q9
    mc_sol.append((1, 9, "a", "The correct answer is B. "
                   "Using Bayes theorem we can write P(H|A) = P(H) * P(A|H)/"
                   "P(A) Now we know that P(H)=0.01 (given), P(A|H)=1 (trick "
                   "coin has two heads so it always flips head), P(A)=0.51 "
                   "(trick coin has 2 heads)."))
    mc_sol.append((1, 9, "c", "The correct answer is B. "
                   "Using Bayes theorem we can write P(H|A) = P(H) * P(A|H)/"
                   "P(A) Now we know that P(H)=0.01 (given), P(A|H)=1 (trick "
                   "coin has two heads so it always flips head), P(A)=0.51 "
                   "(trick coin has 2 heads)."))
    mc_sol.append((1, 9, "d", "The correct answer is B. "
                   "Using Bayes theorem we can write P(H|A) = P(H) * P(A|H)/"
                   "P(A) Now we know that P(H)=0.01 (given), P(A|H)=1 (trick "
                   "coin has two heads so it always flips head), P(A)=0.51 "
                   "(trick coin has 2 heads)."))
    mc_sol.append((1, 9, "e", "The correct answer is B. "
                   "Using Bayes theorem we can write P(H|A) = P(H) * P(A|H)/"
                   "P(A) Now we know that P(H)=0.01 (given), P(A|H)=1 (trick "
                   "coin has two heads so it always flips head), P(A)=0.51 "
                   "(trick coin has 2 heads)."))

    return mc_sol


def solution_mult_choice_lab4():
    """ solution bank for multiple choices - data are stored in a tuple where
    the format is (lab_num, question_num, error_name, feedback)

    Returns:
        mc_col (list):          list of tuples to be fed into sqlite database

    """
    mc_sol = []
    # lab1 q1
    mc_sol.append((1, 1, 'a', "The correct answer is E. The variable is "
                   "discrete, so it can'tbe interval"))
    mc_sol.append((1, 1, "b", "The correct answer is E. Dichotomous variables "
                   "are nomial with only categories or levels, which is not "
                   "the case here"))
    mc_sol.append((1, 1, "c", "The correct answer is E. Nominal variables "
                   "do not impose order, however here there is indeed order "
                   "from less to more"))
    mc_sol.append((1, 1, "1d", "The correct answer is E. Since ratio "
                   "variables are also continuous, it can't be the case here"))

    # lab1 q2
    mc_sol.append((1, 2, "b", "The correct answer is A. Dichotomous is binary"
                   ", not an interval variable"))
    mc_sol.append((1, 2, "c", "The correct answer is A. This is not clear "
                   "from just using a binary variable"))
    mc_sol.append((1, 2, "d", "The correct answer is A. This is not clear "
                   "from just using a binary variable"))
    mc_sol.append((1, 2, "e", "The correct answer is A. It's not clear what's "
                   "conceptual vs operational"))

    # lab1 q3
    mc_sol.append((1, 3, "a", "The correct answer is D. Not true - std "
                   "indeed gets 'stretched' by outliers"))
    mc_sol.append((1, 3, "b", "The correct answer is D. This was a little "
                   "tricky - the problem here is the use of 'any population'. "
                   "Let's demonstrate this by a counterexample. Say we have "
                   "two distributions, X which is normal distribution with "
                   "mean mu and standard deviation sigma, and Y which is a "
                   "constant distribution over the support of a singleton 5. "
                   "For X, it's clear that sampling a point from a normal "
                   "distribution has about 68%% chance of falling within one "
                   "standard deviation of the mean. However, since Y is a "
                   "singleton, the mean is 5 and variance is 0. As a result, "
                   "The chance of your sample falling within one standard "
                   "deviation of the mean is 100%%."))
    mc_sol.append((1, 3, "c", "The correct answer is D. Take the constant "
                   "to be 0 and it's very clear this is wrong"))

    # lab1 q4
    mc_sol.append((1, 4, "a", "The correct answer is B. This answer doesn't "
                   "make sense as there is no quota"))
    mc_sol.append((1, 4, "c", "The correct answer is B. Where is the social "
                   "network?"))
    mc_sol.append((1, 4, "d", "The correct answer is B. You need "
                   "probabilities to select clusters"))
    mc_sol.append((1, 4, "e", "The correct answer is B. But the prompt said "
                   "random"))
    mc_sol.append((1, 4, "f", "The correct answer is B. What's systematic "
                   "about it?"))

    # lab1 q5
    mc_sol.append((1, 5, "a", "The correct answer is C. "
                   "If we let X ~ N(50,sigma^2), we see that P(X>70) can be "
                   "expressed using Z = (X-50)/sigma. So P(X>70) is the same a"
                   "s P((X-50)/sigma > (70-50)/sigma), which is P(Z>(20/sigma)"
                   " which is then 1 - phi(20/sigma), where phi is the cdf of "
                   "the standard normal."
                   "Similarly if we let Y be 1/100 sum(X_j), j from 1 to 100 "
                   "we have then Y ~ N(50,sigma^2/100 and follow the above "
                   "calculations we arrive at the same answer"))
    mc_sol.append((1, 5, "b", "The correct answer is C. "
                   "If we let X ~ N(50,sigma^2), we see that P(X>70) can be "
                   "expressed using Z = (X-50)/sigma. So P(X>70) is the same a"
                   "s P((X-50)/sigma > (70-50)/sigma), which is P(Z>(20/sigma)"
                   " which is then 1 - phi(20/sigma), where phi is the cdf of "
                   "the standard normal."
                   "Similarly if we let Y be 1/100 sum(X_j), j from 1 to 100 "
                   "we have then Y ~ N(50,sigma^2/100 and follow the above "
                   "calculations we arrive at the same answer"))
    mc_sol.append((1, 5, "d", "The correct answer is C. "
                   "If we let X ~ N(50,sigma^2), we see that P(X>70) can be "
                   "expressed using Z = (X-50)/sigma. So P(X>70) is the same a"
                   "s P((X-50)/sigma > (70-50)/sigma), which is P(Z>(20/sigma)"
                   " which is then 1 - phi(20/sigma), where phi is the cdf of "
                   "the standard normal."
                   "Similarly if we let Y be 1/100 sum(X_j), j from 1 to 100 "
                   "we have then Y ~ N(50,sigma^2/100 and follow the above "
                   "calculations we arrive at the same answer"))

    # lab1 q6
    mc_sol.append((1, 6, "a", "The correct answer is B. "
                   "This is law of large numbers"))
    mc_sol.append((1, 6, "c", "The correct answer is B. "
                   "Well this is kind of obvious you don't need a theorem to "
                   "know this"))
    mc_sol.append((1, 6, "d", "The correct answer is B. "
                   "Not the central limit theorem"))

    # q7
    mc_sol.append((1, 7, "7b", "The correct answer is A. "
                   "Standard error of the mean is defined as s/sqrt(n) where n "
                   "is the sample size. So it will get smaller"))
    mc_sol.append((1, 7, "7c", "The correct answer is A. "
                   "It should actually be larger"))
    mc_sol.append((1, 7, "7d", "The correct answer is A. "
                   "Sampling doesn't alter inherent population distribution"))
    mc_sol.append((1, 7, "7e", "The correct answer is A. "
                   "That's not what central limit theorem tells us"))
    mc_sol.append((1, 7, "7f", "The correct answer is A. "
                   ""))

    # q8
    mc_sol.append((1, 8, "a", "The correct answer is D. "
                   "All three statistics are 30"))
    mc_sol.append((1, 8, "b", "The correct answer is D. "
                   "Yup it's a constant distribution, which is unimodal"))
    mc_sol.append((1, 8, "c", "The correct answer is D. "
                   "Yup constant distributions have 0 variance/std"))
    mc_sol.append((1, 8, "e", "The correct answer is D. "
                   "There's no errors so sure it's 0"))

    # q9
    mc_sol.append((1, 9, "a", "The correct answer is B. "
                   "Using Bayes theorem we can write P(H|A) = P(H) * P(A|H)/"
                   "P(A) Now we know that P(H)=0.01 (given), P(A|H)=1 (trick "
                   "coin has two heads so it always flips head), P(A)=0.51 "
                   "(trick coin has 2 heads)."))
    mc_sol.append((1, 9, "c", "The correct answer is B. "
                   "Using Bayes theorem we can write P(H|A) = P(H) * P(A|H)/"
                   "P(A) Now we know that P(H)=0.01 (given), P(A|H)=1 (trick "
                   "coin has two heads so it always flips head), P(A)=0.51 "
                   "(trick coin has 2 heads)."))
    mc_sol.append((1, 9, "d", "The correct answer is B. "
                   "Using Bayes theorem we can write P(H|A) = P(H) * P(A|H)/"
                   "P(A) Now we know that P(H)=0.01 (given), P(A|H)=1 (trick "
                   "coin has two heads so it always flips head), P(A)=0.51 "
                   "(trick coin has 2 heads)."))
    mc_sol.append((1, 9, "e", "The correct answer is B. "
                   "Using Bayes theorem we can write P(H|A) = P(H) * P(A|H)/"
                   "P(A) Now we know that P(H)=0.01 (given), P(A|H)=1 (trick "
                   "coin has two heads so it always flips head), P(A)=0.51 "
                   "(trick coin has 2 heads)."))

    return mc_sol


def solution_mult(lab):
    if lab == 1:
        mc_sol = solution_mult_choice_lab1()
    elif lab == 2:
        mc_sol = solution_mult_choice_lab2()
    elif lab == 3:
        mc_sol = solution_mult_choice_lab3()
    elif lab == 4:
        mc_sol = solution_mult_choice_lab4()
    else:
        print("Invalid input for lab number (1-4)")
        mc_sol = []
    return mc_sol


def solution_data_analysis(lab):
    """ solution bank for data analysis section for all 4 labs

    Many layers: 1) lab number (lab1_sol), 2) question_key (2a),
    3) error_key (wrong_date), 4) actual content and points off in a tuple
    """
    pass


def write_mc_to_db(lab):
    """ writes mc_sol to database "solutions.db"
    Args:
        lab:            lab number for which the solution is to be written
    """
    con = lite.connect('solutions.db')
    mc_sol = solution_mult(lab)

    with con:
        con.row_factory = lite.Row      # dictionary cursor
        cur = con.cursor()
        for i in range(len(mc_sol)):
            cur.execute("INSERT INTO MC VALUES{0}".format(mc_sol[i]))


if __name__ == "__main__":
    write_mc_to_db(1)
