from dataclasses import dataclass

@dataclass
class PERSON():
   height : float = 0.0
   weight : float = 0.0
   bmi : float = 0.0

people = [ PERSON() for i in range(5)]

people[0].height = 1.75
people[0].weight = 70.5
people[0].bmi = people[0].weight / people[0].height **2

people[1].height = 1.62
people[1].weight = 55.8
people[1].bmi = people[1].weight / people[1].height **2

people[2].height = 1.88
people[2].weight = 95.2
people[2].bmi = people[2].weight / people[2].height **2

people[3].height = 1.70
people[3].weight = 82.3
people[3].bmi = people[3].weight / people[3].height **2

people[4].height = 1.80
people[4].weight = 68.0
people[4].bmi = people[4].weight / people[4].height **2

print(people)