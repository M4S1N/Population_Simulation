from probabilities import *
import sys

class Person:
    def __init__(self, sex, age=0):
        self.sex = sex
        # Edad en meses
        self.age = age
        self.time_pregnant = None
        self.total_children_want = 0
        self.total_children = 0
        self.timefrombreakup = None
        self.breakup = None

        self.want_partner_group = want_partner_group(self)
        self.want_partner = False
        self.partner = None
        self.single = True


class Simulation:

    def __init__(self, Male=50, Female=50, T=100):
        self.populationMale = list([Person('Male', int(random()*100*12)) for i in range(Male)])
        self.populationFemale = list([Person('Female', int(random()*100*12)) for i in range(Female)])
        self.TimeLimit = T*12
        self.total_matching = 0
        self.total_breakups = 0
        self.list_of_matching = []
        self.deaths = 0
        self.born = 0
        self.data_per_year = [[Male,Female,self.born,self.deaths,self.total_matching,self.total_breakups]]


    def run_simulation(self):
        for current_time in range(0, self.TimeLimit):
            self.matching_and_pregnant()
            self.breakup()
            self.update_population_state()
            if (current_time+1) % 12 == 0:
                self.data_of_the_year()


    def update_population_state(self):
        for person in self.populationMale+self.populationFemale:
            # Actualiza la edad
            person.age += 1
            if want_partner_group(person) > person.want_partner_group:
                person.want_partner_group = want_partner_group(person)
                person.want_partner = False

            # Actualiza el tiempo desde la ruptura
            if not (person.breakup is None):
                person.timefrombreakup += 1
                if person.timefrombreakup >= person.breakup:
                    person.timefrombreakup = None
                    person.breakup = None
                    person.single = True

            # Comprueba si hay algun parto y actualiza la poblacion
            if not (person.time_pregnant is None):
                person.time_pregnant += 1
                if person.time_pregnant == 9:
                    children = ChildBirth()
                    person.total_children += len(children)
                    for child in children:
                        if child == 'Male':
                            self.populationMale.append(Person(child, 0))
                        else:
                            self.populationFemale.append(Person(child, 0))
                        self.born += 1
                    person.time_pregnant = None

            # Comprueba si hay alguna muerte y actualiza la poblacion
            if Die(person):
                if not (person.partner is None):
                    partner = person.partner
                    partner.partner = None
                    partner.breakup = BreakUp(partner, person)[0]
                    partner.timefrombreakup = 0
                    partner.total_children_want = partner.total_children = 0

                if person in self.populationMale:
                    self.populationMale.remove(person)
                else:
                    self.populationFemale.remove(person)
                self.deaths += 1

    def matching_and_pregnant(self):
        for person in self.populationMale+self.populationFemale:
            if person.single and not person.want_partner:
                person.want_partner = WantPartner(person)
        
        for man in self.populationMale:
            if man.want_partner:
                for woman in self.populationFemale:
                    if woman.want_partner:
                        if WillBePartner(man, woman):
                            man.single = woman.single = False
                            man.want_partner = woman.want_partner = False
                            man.partner = woman
                            woman.partner = man
                            man.total_children_want = NumberMaxChildren()
                            woman.total_children_want = NumberMaxChildren()
                            self.list_of_matching.append([man, woman])
                            self.total_matching += 1
                            break
        for woman in self.populationFemale:
            if (not woman.single)\
                and woman.breakup is None\
                and woman.total_children < max(woman.total_children_want, woman.partner.total_children_want)\
                and woman.time_pregnant is None\
                and Pregnant(woman):
                woman.time_pregnant = 0

    def breakup(self):
        while self.total_breakups < Breakup_probability*self.total_matching:
            man, woman = self.list_of_matching[randint(0,len(self.list_of_matching)-1)]
            man.partner = woman.partner = None
            man.breakup, woman.breakup = BreakUp(man, woman)
            man.timefrombreakup = woman.timefrombreakup = 0
            man.total_children_want = woman.total_children_want = 0
            self.list_of_matching.remove([man, woman])
            self.total_breakups += 1
    
    def data_of_the_year(self):
        man = len(self.populationMale)
        woman = len(self.populationFemale)
        self.data_per_year.append([man,woman,self.born,self.deaths,self.total_matching,self.total_breakups])


if __name__ == '__main__':
    try:
        sim = Simulation(Male=int(sys.argv[1]), Female=int(sys.argv[2]))
    except:
        sim = Simulation()
    initialize()
    sim.run_simulation()
    for i in range(len(sim.data_per_year)):
        year = sim.data_per_year[i]
        print(f'Año: {i+1} / Hombres: {year[0]} / Mujeres: {year[1]} / Nacimientos: {year[2]}\
 / Fallecimientos: {year[3]} / Emparejamientos: {year[4]} / Rupturas: {year[5]}')