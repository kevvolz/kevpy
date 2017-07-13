#Extracting Data with Regular Expressions (Chapter 11): Extract all numbers from file using regex and print sum
import re   #imports regular expressions

file = raw_input("Enter file name: ")   #prompt user for filename
if len(file) < 1 : file = "regex_sum_211577.txt"    #default file if no entry
fhand = open(file)  #designate file handle, open and read
numlist = list() #define list
add = list() #define list

for line in fhand:  #for each line in file handle...
    line = line.rstrip()    #removes \n; new line
    stuff = re.findall('[0-9]+', line)  #finds completely, all integers -- in line
    if len(stuff) == 0: continue #if length of int = 0, keep going
    numlist.append(stuff)   #append all found integers to numlist
    for x in stuff: #for items in numlist
        x = int(x)  # convert to integer
        add.append(x)   #append to list called add
print sum(add)  #print sum of add (list of integers) list


#Regex Lessons
import re   #imports regular expressions

file = raw_input("Enter file name: ")   #prompt user for filename
if len(file) < 1 : file = "regex_sum_42.txt"    #default file if no entry
fhand = open(file)  #designate file handle
nums = list()   #empty list

for line in fhand:  #for each line in file handle...
    line = line.rstrip()    #removes \n
    #if line.find('E') >= 0:    #find lines with XXXX
    #if line.startswith('W') :  #find lines starting with 'W'
    #if re.search('vocabulary', line):  #searches for lines with XXXX
    #if re.search('^I', line):   #searches for lines that start with XXXX
        #print line
    if re.search('[0-9]+', line) :
        x = re.findall('[0-9]+', line)
            nums.append(x)
print nums


# Accessing web data
import urllib
fhand = urllib.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
print line.strip()

#Compile all other notes and add here -KV 9/20/2016
