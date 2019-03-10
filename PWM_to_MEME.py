import sys
import os
import re

regex=re.compile('[1-4]')

pwm_folder=sys.argv[1]

for file in os.listdir(pwm_folder):
    motif=open(os.path.join(pwm_folder,file))
    for line in file:
        if not line.startswith('POS'):
            line=regex.split(line)[0]
            print line
