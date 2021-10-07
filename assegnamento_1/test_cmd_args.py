import argparse
import time
import numpy as np
from matplotlib import pyplot as plt

#class argparse.ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class=argparse.HelpFormatter, prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True, allow_abbrev=True, exit_on_error=True)

#ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])

parser = argparse.ArgumentParser(description='Letter frequencies and other stats')
parser.add_argument('filename', action='store', nargs='?', default='DC_italiano.txt', 
                    help='name of the file to analyze')
parser.add_argument('--letter', '-l', action='store', nargs='*', 
                    default='a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(), 
                    help='add letter to count (everything is converted lowercase and repetitions are ignored)', dest='letters')
parser.add_argument('--length', '-len', action='store_true',  
                    help='display total number of chracters', dest='disp_length')
parser.add_argument('--nlines', '-nl', action='store_true', 
                    help='display total number of lines', dest='disp_nlines')
parser.add_argument('--nwords', '-nw', action='store_true',  
                    help='display total number of words', dest='disp_nwords')
parser.add_argument('--onlytext', '-skip', action='store_true', 
                    help='skip all non-main text sections (preface, index, ...)', dest='skip_')
parser.add_argument('--encoding', '-enc', action='store', nargs='?', default='utf8', 
                    help='set encoding (default = utf8', dest='encoding')
parser.add_argument('--time', '-t', action='store_true', 
                    help='display execution time', dest='disp_time')

args = parser.parse_args()
args.letters = list(dict.fromkeys((map(str.lower,args.letters))))
print(f'\n{args}\n')

print(f'Analyzing with method 1...\n')

dictionary1 = dict(zip(args.letters,[0 for l in args.letters]))
other1 = 0
lines1 = 0
words1 = 0

if (args.disp_time):
    time0 = time.time()

with open(args.filename, 'r', encoding=args.encoding) as f:
    c = f.read(1).lower()
    if (args.skip_):
        line = f.readline()
        while (line.find("** START") < 0):
            line = f.readline()
    while c:
        try:
            dictionary1[c] = dictionary1[c] + 1
        except:
            other1 = other1 + 1
        c = f.read(1).lower()
        if (args.skip_):
            if (c=='*'):
                break

if (args.disp_time):
    time1 = time.time()-time0
    print(f'Time elapsed: {time1} seconds\n')

if (args.disp_length):
    print(f'Total Length of the file: {sum(dictionary1.values())+other1} characters\n')

plt.figure(1)
ax1 = plt.axes()
ax1.tick_params(axis="y", labelsize=20*(len(args.letters)**-0.35))
ax1.grid()
ax1.set_title('Method 1')
plt.barh(-np.linspace(0, len(args.letters), len(args.letters)), list(dictionary1.values()), 
         tick_label = list(dictionary1.keys()))

print(f'Analyzing with method 2...\n')

dictionary2 = dict(zip(args.letters,[0 for l in args.letters]))
other2 = 0

if (args.disp_time):
    time0 = time.time()

with open(args.filename, 'r', encoding=args.encoding) as f:
    whole_text = f.read().lower()
    for l in args.letters:
        dictionary2[l] = whole_text.count(l)
    other2 = len(whole_text) - sum(dictionary2.values())

if (args.disp_time):
    time2 = time.time()-time0
    print(f'Time elapsed: {time2} seconds\n')

if (args.disp_length):
    print(f'Total Length of the file: {len(whole_text)} characters\n')

plt.figure(2)
ax2 = plt.axes()
ax2.tick_params(axis="y", labelsize=20*(len(args.letters)**-0.35))
ax2.grid()
ax2.set_title('Method 2')
plt.barh(-np.linspace(0, len(args.letters), len(args.letters)), list(dictionary2.values()), 
         tick_label = list(dictionary2.keys()))

if (args.disp_time):
    if (time2==0):
        print(f'Too little time to divide\n')
    print(f'time1/time2 = {time1/time2:.4f}\n')
    
plt.show()
