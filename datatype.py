#datatype

#1. Demonstrate int, float, str, bool, and complex
a = 10              # int
b = 10.5            # float
c = "Hello"         # str
d = True             # bool
e = 3 + 4j          # complex

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))

#2. Demonstrate 2 numbers and display their data types
a = 10
b = 20.5

print("a =", a)
print("Data type of a:", type(a))

print("b =", b)
print("Data type of b:", type(b))


#3. Convert a string number into integer and float
num = "25"

integer_num = int(num)
float_num = float(num)

print("Integer:", integer_num)
print("Float:", float_num)

#4. Find the length of a string
text = "Python"

length = len(text)

print("String:", text)
print("Length:", length)


#5. Create a list, tuple, set, and dictionary and display their types
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_set = {1, 2, 3}
my_dictionary = {"name": "Rahul", "age": 20}

print("List:", my_list)
print("Type:", type(my_list))

print("Tuple:", my_tuple)
print("Type:", type(my_tuple))

print("Set:", my_set)
print("Type:", type(my_set))

print("Dictionary:", my_dictionary)
print("Type:", type(my_dictionary))
