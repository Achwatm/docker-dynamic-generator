import time
from pyfiglet import Figlet
import subprocess
from helpers.config import settings

GENERATOR_LOOP_INTERVAL = settings.GENERATOR_LOOP_INTERVAL


f = Figlet(font='slant')
print(f.renderText('GENERATOR'))

while True:
    users = ['first_user', 'second_user']
    for user in users:
        scale = 1
        subprocess.run(["scripts/generator.sh "+str(scale)+" "+user], shell=True)
    time.sleep(GENERATOR_LOOP_INTERVAL)