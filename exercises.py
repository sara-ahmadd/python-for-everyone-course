location = input('Europe floor: ')
USA_floor = int(location) + 1
print(USA_floor)

name = input('Enter your name: ')
print('Welcome', name)

hr = input("Enter Hours: ")
rate = input('Enter rate: ')
pay = float(hr) * float(rate)
print('Pay:',pay)

celisus = input("Write degree in Celisus: \n")
fahrenhiet = float(celisus) * (5 / 9) + 32
print("Fahrenhiet degree is :", round(fahrenhiet, 3))

# EXERCISE 03_01
hrs = input("Enter hours:\n ")
rate = input("Enter Rate:\n ")

hr_num = float(hrs)
rate_num = float(rate)

if hr_num > 40:
    diff = hr_num - 40
    pay = (40 * rate_num) + (diff * rate_num * 1.5)
    print("Pay:", pay)
else:
    pay = hr_num * rate_num
    print("Pay:", pay)


# EXERCISE 03_02
score = input("Enter a score:\n ")
score_num = float(score)
if score_num > 0 and score_num <= 1:
    if score_num >= 0.9:
        print("A")
    elif score_num >= 0.8:
        print("B")
    elif score_num >= 0.7:
        print("C")
    elif score_num >= 0.6:
        print("D")
    else:
        print("F")
else:
    print("Enter score between 0 and 1.")

# EXERCISE 04_06
def computepay(hrs, rate):
    hr_num = float(hrs)
    rate_num = float(rate)
    if hr_num > 40:
        diff = hr_num - 40
        pay = (40 * rate_num) + (diff * rate_num * 1.5)
        print("Pay:", pay)
    else:
        pay = hr_num * rate_num
        print("Pay:", pay)


hrs = input("Enter hours:\n ")
rate = input("Enter Rate:\n ")
computepay(hrs, rate)

# EXERCISE 05_02
small = None
large = None


while True:
    num = input("Enter a number:\n ")
    if num == "done":
        break
    else:
        try:
            number = int(num)
        except:
            print("Invalid input")

    if small != None:
        if small > number:
            large = small
            small = number
        else:
            if large != None and large > number:
                large = large
            else:
                large = number
    else:
        small = number


print("Maximum", large)
print("Minimum", small)

# EXERCISE 07_02
file_input = input("Enter file name: ")
count = 0
average = None
result = 0
try:
    file_handle = open(file_input)
except:
    print("File doesnot exist:", file_input)
    quit()
for line in file_handle:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        nums_index = line.find("0")
        result = result + float(line[nums_index:])
print("Average spam confidence:", result / count)

# EXERCISE 08_04
file = input("Enter file name: ")
file_h = open(file)
lis = []

for line in file_h:
    new_line = line.split()
    for word in new_line:
        if not word in lis : lis.append(word)
lis.sort()
print(lis)

# EXERCISE 08_05
file = input("Enter file name: ")
file_h = open(file)
count = 0

for line in file_h :
    if line.startswith('From ') :
        count = count + 1
        new_line = line.split()
        print(new_line[1])
print("There were", count, "lines in the file with From as the first word")

EXERCISE 09_04
file = input("Enter file name: ")
file_h = open(file)
dictinary = dict()
array = list()

for line in file_h:
    if line.startswith("From "):
        new_line = line.split()
        array.append(new_line[1])

for person in array:
    dictinary[person] = dictinary.get(person, 0) + 1

big_count = 0
name = None

for a, b in dictinary.items():
    if b > big_count:
        big_count = b
        name = a
    else:
        continue

print(name, big_count)


# EXERCISE 10_02
file = input("Enter file name: ")
file_h = open(file)
dic = dict()

for line in file_h:
    if line.startswith("From "):
        words = line.split()
        time = words[5:6]
        hr = time[0][0:2]
        dic[hr] = dic.get(hr, 0) + 1

tup = sorted([(k, v) for (k, v) in dic.items()])

for (a,b) in tup :
    print(a,b)

# REGULAR_EXPRESION_EXERCISE
import re

file = input("Enter file name: ")
file_h = open(file)
lst = list()

for line in file_h:
    found = re.findall("([0-9]+)", line)
    for i in found:
        lst.append(i)
sum_int = 0

for i in lst:
    sum_int = sum_int + int(i)

print(sum_int)
