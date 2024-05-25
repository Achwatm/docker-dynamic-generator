
import sys, time
from pyfiglet import Figlet
import os
from helpers import dispatcher
import random

f = Figlet(font='slant')
print(f.renderText('PUBLISHER'))

while True:
    users = ['first_user', 'second_user']
    
    dispatcher.run(random.choice(users))
    time.sleep(20)