import random
from datetime import datetime
import time

# set time
start = "16/05/2021 06:00:00"
print(f'Start date is {start}')
d = datetime.strptime(start, "%d/%m/%Y %H:%M:%S")
t0 = time.mktime(d.timetuple())


def distance_and_time_cal(s, v):
    """
    Calculate distance from Earth to current spaceship location, current spaceship location to Mars and
the estimated time to go to Mars
    :param s: distance between Earth and Mars in kilometers
    :param v: current velocity of spaceship in kilometers/secs
    :return: distance from Earth to current spaceship location, current spaceship location to Mars and
the estimated time to go to Mars
    """
    print(f'Distance between Earth and Mars: {s} km')
    print(f'Spaceship velocity: {v} km/s')
    while True:
        time.sleep(10)
        named_tuple = time.localtime()  # get struct_time
        time_string = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
        print("\nTime now {}".format(time_string))
        t1 = time.time()  # current time
        delta_time_seconds = t1 - t0

        # distance from Earth
        distance_from_Earth = v * delta_time_seconds
        print(f'Current distance from spaceship to Earth: {distance_from_Earth} km')

        # distance from Mars
        distance_from_Mars = s - delta_time_seconds * v
        print(f'Current distance from spaceship to Mars: {distance_from_Mars} km')

        # estimated time of arrival
        estimate_time = ((s - v * delta_time_seconds) / v) / 3600  # hours
        print(f'Estimated time of arrival: {estimate_time} hours')

        if distance_from_Earth >= s or distance_from_Mars <= 0:
            print("You have arrived")
            break
        else:
            print("You are on the way")


def fuel_cal(current_fuel_level, fuel_burn_rate):
    """
    Calculate the current fuel level of spaceship
    :param current_fuel_level: current fuel level
    :param fuel_burn_rate: fuel burn rate
    :return: the change of spaceship's fuel
    """

    print(f'Current fuel level: {current_fuel_level} liters')
    while current_fuel_level != 0:
        current_fuel_level -= fuel_burn_rate
        time.sleep(60)  # delay 60 seconds
        print(f'Current fuel: {current_fuel_level} liters')
    else:
        print('Out of energy')


def health_of_crew_members(number_of_members):
    """
    Define the number of members and define how many victims are there and their symptoms
    :param number_of_members: the quantity of members in spaceship
    :return: the number of members, number of victims and their symptoms in spaceship
    """
    # list of symptoms
    health_problem_list = ['fever', 'sneeze', 'stomachache', 'sore throat']
    while True:
        # random the number of victims
        victims = random.randrange(0, number_of_members)

        # random the symptom
        problem = random.choice(health_problem_list)

        # if the number of victims larger than 2 and have symptom
        if victims >= 2:
            print(f'There are {number_of_members} total members and {victims} members have {problem}')

        # if the number of victims equal to 1 and have symptom
        elif victims == 1:
            print(f'There are {number_of_members} total members and {victims} member has {problem}')

        # if no one has symptom
        else:
            print(f'There are {number_of_members} total members and all of them are normal')
        time.sleep(60)


def spaceship_health(health_of_spaceship, problems):
    print(f'Health of spaceship: {health_of_spaceship}')
    for name, damage in problems.items():
        if random.random() < 0.5:  # random the possibility of problems happen
            continue
        print(f'Problems: {name}')  # print problems
        health_of_spaceship -= damage
        print(f'current_health: {health_of_spaceship}')
        if health_of_spaceship <= 0:
            print("Your spaceship is stop working")
            break
