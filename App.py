# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 16:01:34 2023

@author: lEO
"""

print('\nMini Episode\nBY: Onyiriuba Leonard\n')
name = input('Name: ')
age = int(input('Age: '))
role = int(input('PRESS 1: Instructor\nPRESS 2: Student\nRESPONSE: '))

if role == 1:
    print(f'Welcome to the world of episode. As you dive in as instructor {name}, a world of possiblities await you.')
    print(f'DAY 1:\nInstructor {name} walked into the class on a Monday morning and notices the class is empty even though it is 9:30am when he and his students are scheduled to begin.')
    print('What do you do?')
    q1 = int(input('PRESS 1: Message the GroupChat asking everybody where they are\nPRESS 2: Leave and go back home\nPRESS 3: Report to Management'))

elif role == 2:
    pass
else:
    print('Invalid Response')