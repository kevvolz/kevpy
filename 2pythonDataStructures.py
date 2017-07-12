#https://www.coursera.org/learn/python-data/
#-Continuation of Python for Everybody

#Python'2.7'Quick'Reference'Sheet:
#http://www.astro.up.pt/~sousasag/Python_For_Astronomers/Python_qr.pdf

#Python Built-in Functions:
#https://docs.python.org/2/library/functions.html

#String Methods:
#https://docs.python.org/release/2.7.10/library/stdtypes.html#string-methods

#Strings
#Files
#Lists
#Dictionaries
#Tuples

#6.5. Finds text in string, creates index, converts to number (not necessarily needed for print) and prints desired text based off index
text = "X-DSPAM-Confidence:    0.8475";
index = 0

for number in text:
    index = text.find(".")
    sol = float(text[index-1:])
print sol

#7.1. Takes an input file, removes \n, returns each line in upper case; otherwise extra spaces
fname = raw_input("Enter file name: ")
fh = open(fname)

for words in fh:
    words = words.rstrip()
    print str.upper(words)

#7.2. Takes input file, selects string .startswith(), selects text, strips \n, converts string to float(), stores variable, sums, increases count, calculates average, and prints, converting to str(). Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
val = 0
top = 0
holder = 0
avg = 0
topholder = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue    #ignore lines of no interest
    val = line[19:].strip()
    holder = float(val)
    top = holder
    topholder = top + topholder
    #print line
    count = count + 1

avg = topholder/count
print "Average spam confidence: " + str(avg)

#8.4. Asks for file input, assigns handle, creates empty lists, iterates through each line in file, splits the line into list, evaluates word in list to see if already in list, if not adds word, sorts new list, prints

fname = raw_input("Enter file name: ")    #prompt for file name
fh = open(fname)    #assign handle
lst = list()    #create empty list
answer = list() #create empty list
index = 0

for line in fh:    #for each line in file:
    cut = line.split()    #splits line into list
    for word in cut:    #iterates through items in list
        if word not in lst:    #avoids adding duplicate words
            lst.append(word)    #puts split line into list
answer = lst.sort()    #sorts the list
print lst    #prints the list

#8.5. Open file and read it line by line. Find a line that starts with ‘From ‘ and parse the line. Print second word in the line and print a count.
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst = list()

for line in fh:
    if not line.startswith("From ") : continue
    cut = line.split()
    lst.append(cut[1])
    count = count + 1

for i in lst:
    print i
print "There were", count, "lines in the file with From as the first word"

#1 parse the From line using split() and print out the second word in the line
#  the entire address of who sent the message
#2 print out each item in list and the count at the end

name = raw_input("Enter file:")	#prompt for user to input file name
if len(name) < 1 : name = "mbox-short.txt"	#if no input entered will default to...
handle = open(name)	#handle assigned to input
lst = list()	#create empty list
emails = dict()	#create empty dictionary

for line in handle:	#for lines of text in file
	if not line.startswith("From ") : continue	#if it doesn't start with 'From ', keep going
	cut = line.split()	#add lines that do start with 'From ' to cut (list), split by spaces
	lst.append(cut[1])	#append the 2nd block of text to lst (list)

for addresses in lst:	#for 2nd blocks of text in list...
	emails[addresses] = emails.get(addresses, 0) + 1	#grab email, add (if not there) and count in dictionary

bigcount = None	#define variable for value
bigword = None	#define variable for key
for k, v in emails.items():	#for key, value in dictionary
	if bigcount is None or v > bigcount:	#if bigger or not there, replace
		bigword = k
		bigcount = v
print bigword, bigcount	#print email with highest count, and what the count is


#9.4. Read input file to find out who has sent greatest number of messages with dictionary with counts.
name = raw_input("Enter file:")    #asks for file input
if len(name) < 1 : name = "mbox-short.txt"    #if input empty, inputs mbox-short.txt as default

handle = open(name)    #file handle for input file
purse = dict()    #create empty dictionary called purse

for line in handle:    #for line in file
    if not line.startswith("From ") : continue    #only consider lines that start with "From "
    clip = line.split()    #Split the line
    email = clip[1] #email is the second item in the list
    for emails in purse:
        if email not in purse: #if the email key doesn't already exist
            purse[email] = email #add key, email, to list
        else:
            purse[email] = purse[email] + 1 #otherwise increase the value of the key by one
print email    #print dictionary

#10.2. Read input file and figure out distribution of messages by hour of the day.
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

lst = list()    #create list
months = dict()    #create dictionary

for line in handle:    #for lines of text in file
    if not line.startswith("From ") : continue    #if it doesn't start with 'From ', keep going
    cut = line.split()    #add lines that do start with 'From ' to cut (list), split by spaces
    delimiter = ':' #define variable to be used as a delimiter
    cut2 = cut[5].split(delimiter)  #grab just the hour blocks
    lst.append(cut2[0])    #append the 1st block of text to lst (list)
#print lst
#for nums in lst:
for a in lst:   #for each item, hour block, in list
    months[a] = months.get(a, 0) +1 #key, hour block, defaults to 0, or increments existing value for each key present

answer = list() #new list
for k, v in months.items(): #for key, value in dictionary (key, value)
    newtup = (k, v) #new tupple equals (k, v)
    answer.append(newtup)   #append k, v for each tupple
answer.sort()   #sorts list
for x, z in answer: #for each tupple item
    print x, z  #print each tupple item
