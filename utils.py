import numpy as np

#=================================================================================================
# Variables globales
#-------------------------------------------------------------------------------------------------
MAX_CHILD = 12
Pregnant_probability_per_interval,\
Pregnant_probability_per_month = [
    [12, 15, 0.2],
    [15, 21, 0.45],
    [21, 35, 0.8],
    [35, 45, 0.4],
    [45, 60, 0.2],
    [60, 125, 0.05]
], []
Die_probability_per_interval,\
Die_probability_per_month = [
    [0, 12, 0.25, 0.25],
    [12, 45, 0.1, 0.15],
    [45, 76, 0.3, 0.35],
    [76, 125, 0.7, 0.65],
    [125, 125+1/12, 1.0, 1.0]
], []
NumberMaxChildren_probability = [
    [1, 0.6],
    [2, 0.75],
    [3, 0.35],
    [4, 0.2],
    [5, 0.1],
    [MAX_CHILD, 0.05]
]
WantPartner_probability_per_interval,\
WantPartner_probability_per_month = [
    [12, 15, 0.6],
    [15, 21, 0.65],
    [21, 35, 0.8],
    [35, 45, 0.6],
    [45, 60, 0.5],
    [60, 125, 0.2]
], []
WillBePartner_probability_per_interval = [
    [0, 5, 0.45],
    [5, 10, 0.4],
    [10, 15, 0.35],
    [15, 20, 0.25],
    [20, 125, 0.15]
]
Time_of_breakup_for_age = [
    [12, 15, 3],
    [15, 21, 6],
    [21, 35, 6],
    [35, 45, 12],
    [45, 60, 24],
    [60, 125, 48]
]
ChildBirth_probability = [
    [1, 0.7],
    [2, 0.18],
    [3, 0.08],
    [4, 0.04],
    [5, 0.02]
]
Breakup_probability = 0.2
#=================================================================================================


#=================================================================================================
# Utiles
#-------------------------------------------------------------------------------------------------
def C(n, k):
    ans = 1
    for i in range(n-k+1, n+1):
        ans *= i / (i-n+k)
    return int(ans)

def initialize():
    # Die
    for case in Die_probability_per_interval:
        n = case[1]*12-case[0]*12
        Die_probability_per_month.append([case[2]/n, case[3]/n])

    # Pregnant
    for case in Pregnant_probability_per_interval:
        n = case[1]*12-case[0]*12
        polynomial = [C(n-8*i, i+1)*(-1)**i for i in range(int(np.ceil((n-8)/9)))][::-1]+[-case[2]]
        roots, root = np.roots(polynomial), 1
        for r in roots:
            if r.imag == 0 and 0 <= r.real and r.real <= root:
                root = r.real
                break
        Pregnant_probability_per_month.append(root)

    # WantPartner
    for case in WantPartner_probability_per_interval:
        n = case[1]*12 - case[0]*12
        #root = 1-((1-case[2])/(-1)**n)**(1/n)
        WantPartner_probability_per_month.append(case[2]/n)

def want_partner_group(person):
    for i in range(len(WantPartner_probability_per_interval)):
        group = WantPartner_probability_per_interval[i]
        if group[0]*12 <= person.age and person.age <= group[1]*12:
            return i+1
    return -1
#=================================================================================================

