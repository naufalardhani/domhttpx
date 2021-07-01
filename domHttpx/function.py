import glob
import os

from domHttpx import write

def check_result():
    result_name = glob.glob('./result/*')
    counter = 0
    for name in result_name:
        counter += 1
        print('%i. %s' % (counter, name.replace('./result/', '')))

def show_result(filename):
    os.system('cat result/%s' % filename)

def remove_result(filename):
    os.system('cat result/%s' % filename)
    file = open('result/%s' % filename)
    counter = 0
    for i in file:
        counter += 1
    write.tab()
    # info('Total %i line' % counter)
    confirm = input('Are you sure to remove %s which has %i results? (y/n) ' % (filename, counter))
    if confirm == "y":
        os.system("rm result/%s" % filename)