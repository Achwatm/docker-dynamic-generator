
import sys, time
from pyfiglet import Figlet
import os
from helpers import subscriber

f = Figlet(font='slant')
print(f.renderText('OBSERVER'))

channel = os.environ["CHANNEL"]

subscriber.run(channel)