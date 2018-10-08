
from bs4 import BeautifulSoup
import requests
import csv
from pprint import pprint
import random

confirmation = input('Do you want to specify number of workouts ? (y/n) : ')
if confirmation == 'n':
    pass
elif confirmation == 'y':
    number = input('Enter number of workouts desired ( < 10) : ')

site_link_url = int(input('Enter \n'
            '1 for Chest \n'
            '2 for Forearms \n'
            '3 for Lats \n'
            '4 for Middle Back \n'
            '5 for Lower Back \n'
            '6 for Neck \n'
            '7 for Quadriceps \n'
            '8 for Hamstrings \n'
            '9 for Calves \n'
            '10 for Triceps \n'
            '11 for Traps \n'
            '12 for Shoulders \n'
            '13 for Abdominals \n'
            '14 for Glutes \n'
            '15 for Biceps :'))
url = "https://www.bodybuilding.com/exercises/finder/?muscleid={}".format(site_link_url)

print()

r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
exercises = {}
k = 1
keylist = []
random_vals = []

for i in soup.find_all('h3', class_='ExHeading ExResult-resultsHeading'):
    link = i.a.get('href')
    sections = link.split('/')
    exercise_name = sections[2].replace('-', ' ')
    exercises[k] = exercise_name.capitalize()
    k += 1

if confirmation == 'n':
    pprint(exercises)
elif confirmation == 'y':
    keylist = list(range(1,len(exercises)))
    random_vals = (random.sample(keylist, int(number)))
    for u in random_vals:
        print(exercises[u])
