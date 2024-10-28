# empty turple

my_tuple = ()

print(my_tuple)

#Tuples having integers

my_tuple = (1,3,5)

print("\n", my_tuple)

# turple with mixed datatypes

my_tuple = (1, 'hello', 3.2)

print("\n", my_tuple)

# nested tuple

my_tuple = ("mouse", [3,5,7], (2,5,7))

print("\n", my_tuple)

# Accssing tuple elements using indexing

my_tuple = ('p','e','r','m','i','t')

print(my_tuple[0])

print(my_tuple[5])

# # nested tuple

n_tuple = ("mouse", [3,5,7], (2,5,7))

# # nested index

print(n_tuple[0][3])

print(n_tuple[1][1])

print(n_tuple[2][0])

# # slicing

print("Sliced :", my_tuple[1:4])

# Iterating through tuple

for l in my_tuple:
    print("Hello", l)