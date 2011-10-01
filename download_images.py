import re
import os

with open('list.txt') as fin:
    for line in fin:
        line = line.strip()

        if re.match(r'[\dA-Z]{10}', line):
            print line
            if not os.path.exists(line + '.jpg'):
                cmd = 'wget http://images.amazon.com/images/P/%s.01.LZZZZZZZ.jpg -O %s.jpg' % (line, line)
                print cmd
                os.system(cmd)
