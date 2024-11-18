file1=open('cover.txt', 'r')

print(file1.read())

file1.close()

print("************************************************")

file2=open('cover.txt', 'r')

print(file2.readline())

file2.close()

print("-----------------------------------")

file2=open('cover.txt', 'r')

print(file2.readline())

print(file2.readline())

print(file2.readline())

file2.close()

print("************************************************")

file2=open('cover.txt', 'r')

print(file2.readlines())

file2.close()

print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

file3=open('cover.txt', 'r')

print(file3.read(10))

file3.close()

#write - write new content and delete the old content

file4=open('cover.txt', 'w')

file4.write('This is a new text')

file4.close()

file5=open('cover.txt', 'r')

print(file5.read())

file5.close()

#append text

file5=open('cover.txt', 'a')

file5.write('Additional text added to the existing text')

file5.close()

file6=open('cover.txt', 'r')

print(file6.read())

file6.close()