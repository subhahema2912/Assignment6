import json
class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state
employee_data={"employees":[
    {
        "Name": "Aravindh",
      "DOB": "1983-08-23",
      "Height": 170,
      "City": "Chennai",
      "State": "Tamilnadu"
    },
    {
      "Name": "Hema",
      "DOB": "1985-12-29",
      "Height": 151,
      "City": "Hyderabad",
      "State": "Telangana"
    },
    {
      "Name": "Revathi",
      "DOB": "1992-03-10",
      "Height": 160,
      "City": "Madurai",
      "State": "Tamilnadu"
    },
    {
      "Name": "Vedha",
      "DOB": "1999-10-25",
      "Height": 150,
      "City": "Namakkal",
      "State": "Tamilnadu"
    },
    {
      "Name": "Vasanthraj",
      "DOB": "1956-02-10",
      "Height": 167,
      "City": "Bangalore",
      "State": "Karnataka"
    }
  ]
}


with open('employee.json', 'w') as file:
    json.dump(employee_data, file)

with open('employee.json') as file:
    data = json.load(file)
    employee_list = []

    for employee_data in data['employees']:
        name = employee_data['Name']
        dob = employee_data['DOB']
        height = employee_data['Height']
        city = employee_data['City']
        state = employee_data['State']
        employee = Employee(name, dob, height, city, state)
        employee_list.append(employee)

for employee in employee_list:
    print("Name:", employee.name)
    print("DOB:", employee.dob)
    print("Height:", employee.height)
    print("City:", employee.city)
    print("State:", employee.state)
    print()


# 2. Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.

import json
indian_states = {
    "Tamilnadu": "Chennai",
    "Telangana": "Hyderabad",
    "Karnataka": "Bengaluru",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Gujarat": "Gandhinagar",
    "Maharashtra": "Mumbai",
    }
with open('states and capital.json', 'w') as file:
    json.dump(indian_states, file)

print("Indian states and capitals have been written to indian_states.json.")



class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def get_info(self):
        print(f"{self.name}'s coat color is {self.coat_color}.")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, hunting_skill):
        super().__init__(name, age, coat_color)
        self.hunting_skill = hunting_skill

    def special_skill(self):
        print(f"{self.name} has a special skill: {self.hunting_skill}")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color, strength):
        super().__init__(name, age, coat_color)
        self.strength = strength

    def display_strength(self):
        print(f"{self.name}'s strength is {self.strength}.")


dog1 = Dog("Sam", 2, "Black")
dog1.description()
dog1.get_info()
dog2 = JackRussellTerrier("Sweety", 2, "White", "excellent digging")
dog2.description()
dog2.get_info()
dog2.special_skill()
dog3 = Bulldog("Ritsy", 3, "Brown", "impressive")
dog3.description()
dog3.get_info()
dog3.display_strength()