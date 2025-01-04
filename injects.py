import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory', type=str, help='the directory from which the injects are stored in')
parser.add_argument('-u', '--users', type=int, help="number of users in the competition (at least one team is needed)", required =True)
parser.add_argument('-t', '--timesheet', type=str, help='the csv where the timesheet is stored', required=True)
args = parser.parse_args()


# if you got different folder names change here
source = 'upload'
dest = 'injects'

all = os.listdir(source)
x = 1
# Creates teams based of input (starts from team 1)
with open ('dwayne.conf', 'a', encoding='utf-8') as dwayne:
    password = 'password'
    for x in range(args.users+1):
        appendedTxt = '\n[[team]]\nip = "{tid}"\npw = "{pw}"'.format(
            tid = x,
            pw = password # change this for new password
            )
        dwayne.write(appendedTxt)
        
# Moves all injects from upload into the destination folder

for f in all:
    sp = os.path.join(source, f)
    dp = os.path.join(dest, f)
    os.rename(sp, dp)


# Initiates the injects based on info from the csv (title,body,file,time,due,close,points)
with open(args.timesheet, 'r') as s, open ('injects.conf', 'a', encoding ='utf-8') as d:
    for line in s:
        ls = line.split(',')
        appendedText = '\n[[inject]]\ntitle="{title}"\nbody = "{body}"\nfile = "{file}"\ntime = {time}\ndue = {due}\ncloses = {closes}\npoints = {points}'.format(
            title = ls[0],
            body = ls[1],
            file = ls[2],
            time = ls[3],
            due = ls[4],
            closes = ls[5],
            points = ls[6]
            )        
        d.write(appendedText)
