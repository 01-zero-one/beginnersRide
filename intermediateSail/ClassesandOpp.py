# Random module for providing random id's
import random
'''
    This is a simples Class built for a Bus Company Called Carriage.
    This class will show all the hubs in the company with number of buses
    and Employees working in each hub.
'''


class Carriage:
    # Args and Attr
    def __init__(self, hub_id, no_buses, num_emp):
        self.hub_id = hub_id
        self.no_buses = no_buses
        self.num_emp = num_emp

    # This hub method is going to generate distinct id number for each employee
    def employee_id(self, num_emp):
        for _ in range(num_emp):
            a = random.randint(111111, 999999)
            li = []
            li.append(a)
            print('List of Employees id\'s ', li)





# To get random id numbers for the hubs
def random_id():
    random_id = [random.randint(1, 10) for _ in range(10)]
    random_id_str = ' '.join(map(str, random_id))
    print('Hub id: ', random_id_str)

#To get random amount of buses for each hub
num_buses = random.randint(1, 5)
def random_no_buses(buses):
    print('This Hub Has', buses, ' buses')

# To get random amount of employees depending on number of buses
def number_of_emp(num_bus):
    final = 1 + 2 * int(num_bus)
    print('This hub has ', final, ' number of Employees')
    return final

if __name__ == "__main__":
    hub_1 = Carriage(random_id(), random_no_buses(num_buses), number_of_emp(num_buses))
    hub_1.employee_id(number_of_emp(num_buses))


'''This is a code snippet of my undestanding of basic classes or OOP -Object Oriented Programming'''
#Sincerely this code is all over the place 😒