#x = [5, 10, 3, 2, 8, 0]

#y = x[:2:-1]

#print(y)

#Ans 1: a) It will output list index starting from -1 until 2, i.e.[0, 8, 2] from the given list.
#       b) When you do not specify the starting point, it starts from the beginning index of the list, i.e. 0. 
#          And when you mention stride is negative, it starts from the end of the list.

#Ans 2: C) [i+1 for i in a]

#Ans 3: d  = { 1: "good", 2: "morning", 3: "john"}
#       a) for a in d:
#            print("value =", d[a].title())
#       b) Given, set = {'good', 'john', 'morning'}
#          Now, we will be using iterable unpacking operator to create the following set:
#          first, *rest = set
#          print(first)       # Output: good
#          print(rest)        # Output: {'morning', 'john'}

#Ans 4: Given list,
#       list_a = [1, 2, 3, 4]
#       list_b = ['a', 'b', 'c', 'd']
# Now, we will create list_c
#       list_c = ['a1', 'b1', 'c1']

#zipped_list = zip(list_a, list_b, list_c)
#print(list(zipped_list))

#Output:((1, 'a', 'a1'), (2, 'b', 'b1'), (3, 'c', 'c1'), (4, 'd', 'd1'))
# The general rule is that the resulting iterator will have as many elements as 
# the shortest iterator. The iterator will stop when the shortest iterator is exhausted.

#Ans 5: list of students' phone number and a tuple of their names
#      phone = [979921, 989043, 933043, 932902]
#      student = ('jane', 'nika', 'kian', 'mira')

#      Using zip, how can I combine these two list and tuples into dictionary with phones as keys and names as values, respectively?
#      dict(zip(phone, student))

# Output: {979921: 'jane', 989043: 'nika', 933043: 'kian', 932902: 'mira'}
# How?: It will create a dictionary with phone numbers as keys and names as values. 

#Ans 6: Use the listcomp to create a list with three-tuple elements where each tuple contains a number
#       between 1 and 10, its square and cubic; that is,
#       [(0,0,0), (1, 1, 1), (2, 4, 8), (3, 9, 27), ..., (9, 81, 729)]
#       listcomp = [(i, i**2, i**3) for i in range(1, 11)]
#       print(listcomp)

# Ans 7: dict1 = {'A1': 100, 'B1': 20, 'A2':30, 'B2': 405, 'A3':23}
#        a) listcomp without using values() method
#        list_comp = [(k, v) for k, v in dict1.items()]
#        print(list_comp)   
# Output: [('A1', 100), ('B1', 20), ('A2', 30), ('B2', 405), ('A3', 23)]

#        b) iterator unpacking using values() method
#        unpack = [*dict1.values()]
#        print(unpack)

# Output: [100, 20, 30, 405, 23]

#        c) list constructor using values() method
#        list_const = list(dict1.values())
#        print(list_const)

# Output: [100, 20, 30, 405, 23]

# Ans 8: Given, list1 = ['book_john', 'pencil_askar', 'pen_amin', 'pen_john', 
#                'key_askar',\
#                 'pen_askar', 'laptop_askar', 'backpack_john', 'car_john']

# Use the listcomp to find john's belongings in one line of code. The output should look like:
# john_belongings = [item.split('_')[0] for item in list1 if 'john' in item]
# Output: ['book', 'pen', 'backpack', 'car']



