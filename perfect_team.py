"""
The School of Languages and Science teaches five sujbects: Physics, Chemistary, Math, Batany and Zoology.
Each student is skilled in one subject. The skills of students are described by string of name 'skills'
that consists of letters 'p', 'c', 'm', 'b' and 'z' only. Each character describes the skill of a student.

Given a list of students' skills, determine the total number of different teams satisfying the following constraints:

- A team consists of a group of exactly five students.
- Each student is skilled in different subject.
- A student may only b on one team.

Example 1:
skills = pcmbzpcmbz => output: 2
"""


def perfectTeam(skills):
    if len(skills) < 5: return 0

    skills_count = {'m': 0, 'p': 0, 'c': 0, 'b': 0, 'z': 0}

    for skill in skills:
        if skill in skills_count.keys():
            skills_count[skill] += 1

    return min(skills_count.values())


if __name__ == '__main__':
    print(perfectTeam('pcmbzpcmbz'))
    print(perfectTeam('mppzbmbpzcbmpbmczcz'))
    print(perfectTeam('pcm'))
