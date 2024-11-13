file=open('new.txt','r') #default mode is read mode
print(file.read()) #read
file.close() #close

file2=open('new33.txt','w' ) #open file in write mode-- delete the content and give the file new content

file2.write('this is the new file content')

file2.write('this is another new file content')

file2.close()

file3=open('new33.txt', 'r')

print(file3.read())

file4=open('new33.txt', 'a')

file4.write('This is the append text')

file4.close()

file5=open('new33.txt', 'r')

print(file5.read())

#r means read- read()

#w means write - write()- delete old content and give new conten

# means append -write()- will add new content to the existing.