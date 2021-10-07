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
parser.add_argument('--save', '-s', action='store', nargs='?', default='', 
                    help='name of the file to save plot to (default no save)', dest='savefile')

args = parser.parse_args()
args.letters = list(dict.fromkeys((map(str.lower,args.letters))))
print(f'\n{args}\n')

dictionary = dict(zip(args.letters,[0 for l in args.letters]))
nlines = 0
nwords = 0
nchars = 0

time0 = time.time()

with open(args.filename, 'r', encoding=args.encoding) as f:
    whole_text = f.read().lower()
    if (args.skip_):
        whole_text = whole_text[whole_text.find('\n',whole_text.find("*** start"))+1 :
                                whole_text.find("*** end")-1]
    nchars = len(whole_text)
    lines = whole_text.splitlines()
    nlines = len(lines)-lines.count('')
    nwords = len(whole_text.split())
    for l in args.letters:
        dictionary[l] = whole_text.count(l)

time1 = time.time()-time0

if (args.disp_time):
    print(f'Time elapsed: {time1} seconds\n')

if (args.disp_nlines):
    print(f'Total Lines of the file: {nlines} lines\n')
    
if (args.disp_nwords):
    print(f'Total Words of the file: {nwords} words\n')
    
if (args.disp_length):
    print(f'Total Length of the file: {nchars} characters\n')

plt.figure(1)
ax = plt.axes()
ax.tick_params(axis="y", labelsize=20*(len(args.letters)**-0.35))
ax.grid()
ax.set_title(args.filename)
plt.barh(-np.linspace(0, len(args.letters), len(args.letters)), list(dictionary.values()), 
         tick_label = list(dictionary.keys()))
plt.draw()
if (args.savefile):
    plt.savefig(args.savefile)

plt.show()