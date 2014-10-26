"""     @author:        Guang Yang
        @mktime:        10/25/2014
        @description:   writes name and grade in a separate summary text file
                        named "summary_labX_secX.txt" for each section
"""


def write_summary_score(lab, section, s_name, score):
    summary_file = "summary_lab{0}_sec{1}.txt".format(lab, section)
    with open(summary_file, 'a') as f:
        f.write("{0}, {1}\n".format(s_name, score))
