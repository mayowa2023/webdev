file6=open('new3.txt', 'r')

counter=0 #will be counting the number of lines in the file

#read the file line by line

fileread=file6.read()

#\n means new line

lines=fileread.split('\n')

for x in lines:

if x:

counter+=1

print(counter, "total number of lines")