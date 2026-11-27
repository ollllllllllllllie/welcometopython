from dataclasses import dataclass

@dataclass
class PERSON():
   height : float = 0.0
   weight : float = 0.0
   bmi : float = 0.0

people = [ PERSON() for i in range(5)]

for i in range(5):
   Height = float(input("What is the height?: "))
   people[i].height = Height
   Weight = float(input("What is the weight?: "))
   people[i].weight = Weight
   people[i].bmi = people[i].weight / people[i].height **2

print(people)