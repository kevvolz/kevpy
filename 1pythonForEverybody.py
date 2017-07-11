#Coursera: Python for Everybody

#Variables and Expressions
#Conditional Code
#Functions
#Loops and Iteration


#1. Print statement
print "hello world”

#2.2. Raw inputs
name = raw_input("Enter your name")
print "Hello " + name

#2.3. Compute gross pay; convert input
hrs = raw_input("Enter Hours:")
rph = raw_input("Enter hourly wage:")

print float(hrs) * float(rph)

#3.1. Compute gross pay with overtime;
hrs = raw_input("Enter Hours:")
h = float(hrs)

rph = raw_input("Enter hourly wage:")
r = float(rph)

if h > 40:
    pay = 40*r + (h-40)*(1.5*r)

print pay

#3.3. Print grade; elif statements
inp = raw_input("Enter a score btw 0.0 and 1.0: ")
score = float(inp)

if score > 1.0:
    print "Score out of range."
elif score >= 0.9:
    print "A"
elif score >= 0.8:
    print "B"
elif score >= 0.7:
    print "C"
elif score >= 0.6:
    print "D"
elif score < 0.6:
    print "F"

#4.6. Define function and use; convert string to float
def computepay(h,r):
    if h > 40:
        p = 40 * r + (h-40)*(1.5*r)
        return p
    else:
        p = h * r
        return p

hrs = raw_input("Enter Hours:")
hours = float(hrs)

rate = raw_input("Enter rate:")
rph = float(rate)

p = computepay(hours, rph)
print p

#5.2. Print largest and smallest numbers, catch invalid user input (try and except)
largest = None
smallest = None

while True:
    num = raw_input("Enter a number: ")
    if num == "done":
        break
    try:
        test = int(num)
    except:
        print 'Invalid input'
        num = raw_input("Enter a number: ")

    if largest is None:
           largest = int(num)
    if smallest is None:
        smallest = int(num)

    if num > largest:
        largest = int(num)
    if num < smallest:
        smallest = int(num)

print "Maximum is", largest
print "Minimum is", smallest