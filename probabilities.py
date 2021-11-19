from utils import *
from random import *


# Determina si una persona fallece o no
def Die(person):
    U = random()
    option_per_gender = {
        'Male': 0,
        'Female': 1
    }
    for i in range(len(Die_probability_per_interval)):
        interval = Die_probability_per_interval[i]
        if interval[0]*12 < person.age and person.age <= interval[1]*12:
            return U <= Die_probability_per_month[i][option_per_gender[person.sex]]
    return False

# determina si una mujer queda embarazada
def Pregnant(person):
    U = random()
    for i in range(len(Pregnant_probability_per_interval)):
        case = Pregnant_probability_per_interval[i]
        if case[0]*12 < person.age and person.age <= case[1]*12:
            return U <= Pregnant_probability_per_month[i]
    return False

# determina el numero maximo de hijos que quiere tener una mujer
def NumberMaxChildren():
    for i in range(6):
        U = random()
        if U <= NumberMaxChildren_probability[i][1]:
            continue
        return i
    return MAX_CHILD

# Determina si una persona quiere o no una pareja
def WantPartner(person):
    U = random()
    for i in range(len(WantPartner_probability_per_interval)):
        case = WantPartner_probability_per_interval[i]
        if case[0]*12 <= person.age and person.age <= case[1]*12:
            return U <= WantPartner_probability_per_month[i]
    return False

# Determina si dos personas de diferente sexo seran pareja
def WillBePartner(person1, person2):
    U = random()
    age_dif = abs(person1.age-person2.age)
    for case in WillBePartner_probability_per_interval:
        if case[0]*12 <= age_dif and age_dif <= case[1]*12:
            return U <= case[2]
    return False

# Determina el tiempo sin buscar pareja si ocurre una ruptura de una pareja
# se retorna (tiempo_persona1, tiempo_persona2)
def BreakUp(person1, person2):
    time1, time2 = 0, 0
    for case in Time_of_breakup_for_age:
        if case[0]*12 <= person1.age and person1.age <= case[1]*12:
            time1 = case[2]
        if case[0]*12 <= person2.age and person2.age <= case[1]*12:
            time2 = case[2]
    return (time1, time2)

# Determina el numero de hijos que una mujer embarazada tendra en el parto
# [] si pierde el hijo en el parto
def ChildBirth():
    children = []
    for i in range(5):
        U = random()
        if U <= ChildBirth_probability[i][1]:
            children.append(['Male', 'Female'][randint(0,1)])
            continue
        else:
            break
    return children