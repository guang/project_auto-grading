"""     @author:        Guang Yang
        @mktime:        9/27/2014
        @description:   solution bank for multiple choice and data analysis
"""


def solution_mult_choice(lab):
    """ solution bank multiple choice section for all 4 labs """
    # lab 1
    lab1_sol = {
        # q1
        "1a": ("The correct answer is E.\nThe variable is discrete, so it can't"
               "be interval"),
        "1b": ("The correct answer is E.\nDichotomous variables are nomial "
               "with only categories or levels, which is not the case here"),
        "1c": ("The correct answer is E.\nNominal variables do not impose order"
               ", however here there is indeed order from less to more"),
        "1d": ("The correct answer is E.\nSince ratio variables are also "
               "continuous, it can't be the case here"),

        # q2
        "2b": ("The correct answer is A.\n"
               "Dichotomous is binary, not an interval variable"),
        "2c": ("The correct answer is A.\n"
               "This is not clear from just using a binary variable"),
        "2d": ("The correct answer is A.\n"
               "This is not clear from just using a binary variable"),
        "2e": ("The correct answer is A.\n"
               "It's not clear what's conceptual vs operational"),

        # q3
        "3a": ("The correct answer is D.\n"
               "Not true - std indeed gets 'stretched' by outliers"),
        "3b": ("The correct answer is D.\n"
               "This was a little tricky - the problem here is the use of\n"
               "'any population'. Let's demonstrate this by a counterexample.\n"
               "Say we have two distributions, X which is normal distribution\n"
               "with mean mu and standard deviation sigma, and Y which is a\n"
               "constant distribution over the support of a singleton 5. For\n"
               "X, it's clear that sampling a point from a normal\n"
               "distribution has about 68%% chance of falling within one\n"
               "standard deviation of the mean. However, since Y is a\n"
               "singleton, the mean is 5 and variance is 0. As a result,\n"
               "The chance of your sample falling within one standard\n"
               "deviation of the mean is 100%%."),
        "3c": ("The correct answer is D.\n"
               "Take the constant to be 0 and it's very clear this is wrong"),

        # q4
        "4a": ("The correct answer is B.\n"
               "This answer doesn't make sense as there is no quota"),
        "4c": ("The correct answer is B.\n"
               "Where is the social network?"),
        "4d": ("The correct answer is B.\n"
               "You need probabilities to select clusters"),
        "4e": ("The correct answer is B.\n"
               "But the prompt said random"),
        "4f": ("The correct answer is B.\n"
               "What's systematic about it?"),

        # q5
        "5a": ("The correct answer is C.\n"
               "If we let X ~ N(50,sigma^2), we see that P(X>70) can be\n"
               "expressed using Z = (X-50)/sigma. So P(X>70) is the same as\n"
               "P((X-50)/sigma > (70-50)/sigma), which is P(Z>(20/sigma)\n"
               "which is then 1 - phi(20/sigma), where phi is the cdf of\n"
               "the standard normal."
               "Similarly if we let Y be 1/100 sum(X_j), j from 1 to 100\n"
               "we have then Y ~ N(50,sigma^2/100 and follow the above\n"
               "calculations we arrive at the same answer"),
        "5b": ("The correct answer is C.\n"
               "If we let X ~ N(50,sigma^2), we see that P(X>70) can be\n"
               "expressed using Z = (X-50)/sigma. So P(X>70) is the same as\n"
               "P((X-50)/sigma > (70-50)/sigma), which is P(Z>(20/sigma)\n"
               "which is then 1 - phi(20/sigma), where phi is the cdf of\n"
               "the standard normal."
               "Similarly if we let Y be 1/100 sum(X_j), j from 1 to 100\n"
               "we have then Y ~ N(50,sigma^2/100 and follow the above\n"
               "calculations we arrive at the same answer"),
        "5d": ("The correct answer is C.\n"
               "If we let X ~ N(50,sigma^2), we see that P(X>70) can be\n"
               "expressed using Z = (X-50)/sigma. So P(X>70) is the same as\n"
               "P((X-50)/sigma > (70-50)/sigma), which is P(Z>(20/sigma)\n"
               "which is then 1 - phi(20/sigma), where phi is the cdf of\n"
               "the standard normal."
               "Similarly if we let Y be 1/100 sum(X_j), j from 1 to 100\n"
               "we have then Y ~ N(50,sigma^2/100 and follow the above\n"
               "calculations we arrive at the same answer"),

        # q6
        "6a": ("The correct answer is B.\n"
               "This is law of large numbers"),
        "6c": ("The correct answer is B.\n"
               "Well this is kind of obvious you don't need a theorem to know"
               "this"),
        "6d": ("The correct answer is B.\n"
               "Not the central limit theorem"),

        # q7
        "7b": ("The correct answer is A.\n"
               "Standard error of the mean is defined as s/sqrt(n) where n\n"
               "is the sample size. So it will get smaller"),
        "7c": ("The correct answer is A.\n"
               "It should actually be larger"),
        "7d": ("The correct answer is A.\n"
               "Sampling doesn't alter the inherent population distribution"),
        "7e": ("The correct answer is A.\n"
               "That's not what central limit theorem tells us"),
        "7f": ("The correct answer is A.\n"
               ""),

        # q8
        "8a": ("The correct answer is D.\n"
               "All three statistics are 30"),
        "8b": ("The correct answer is D.\n"
               "Yup it's a constant distribution, which is unimodal"),
        "8c": ("The correct answer is D.\n"
               "Yup constant distributions have 0 variance/std"),
        "8e": ("The correct answer is D.\n"
               "There's no errors so sure it's 0"),

        # q9
        "9a": ("The correct answer is B.\n"
               "Using Bayes theorem we can write P(H|A) = P(H) * P(A|H)/P(A)\n"
               "Now we know that P(H)=0.01 (given), P(A|H)=1 (trick coin has\n"
               "two heads so it always flips head), P(A)=0.51 (trick coin\n"
               "has 2 heads)."),
        "9c": ("The correct answer is B.\n"
               "Using Bayes theorem we can write P(H|A) = P(H) * P(A|H)/P(A)\n"
               "Now we know that P(H)=0.01 (given), P(A|H)=1 (trick coin has\n"
               "two heads so it always flips head), P(A)=0.51 (trick coin\n"
               "has 2 heads)."),
        "9d": ("The correct answer is B.\n"
               "Using Bayes theorem we can write P(H|A) = P(H) * P(A|H)/P(A)\n"
               "Now we know that P(H)=0.01 (given), P(A|H)=1 (trick coin has\n"
               "two heads so it always flips head), P(A)=0.51 (trick coin\n"
               "has 2 heads)."),
        "9e": ("The correct answer is B.\n"
               "Using Bayes theorem we can write P(H|A) = P(H) * P(A|H)/P(A)\n"
               "Now we know that P(H)=0.01 (given), P(A|H)=1 (trick coin has\n"
               "two heads so it always flips head), P(A)=0.51 (trick coin\n"
               "has 2 heads)."),
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


def solution_data_analysis(lab):
    """ solution bank for data analysis section for all 4 labs

    Many layers: 1) lab number (lab1_sol), 2) question_key (2a),
    3) error_key (wrong_date), 4) actual content and points off in a tuple
    """
    # lab 1
    lab1_sol = {
        '2a': {
            'wrong_date': (
                "The date is incorrect, check again", 2
            ),
            'wrong_blah': (
                "The blah is wrong, maybe consider doing the assignment again"
                "blah blah blah lololz", 1
            ),
        },
        '3a': {
        }
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
