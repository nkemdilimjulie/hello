

print('Hello', 'Welcome to Python Introductory Part', sep=' ', end='\n')
    
#Tasks

#Task1

'''Printing examples of single Objects 
string, int, float, bool (boolean), complex, None
'''
print('Task1' 'Printing examples of single Objects ')
# integer number
num_integer = 123
print(num_integer )
#print('Integer ',num_integer )
# print(type( num_integer ))

# float number
num_float  = 43.23
print(num_float)
#print('float number', num_float )
# print(type( num_float ))

 # complex number
num_complex  = 4-1j
print( num_complex )
#print('complex number', num_complex )
# print(type( num_float ))

#print string 
string_var = 'How are you?'
print(string_var)

#print boolean
bool_var = True
print(bool_var)

#Task2
print('Task2', 'Print data types of given value')

print(num_integer, 'is', 'type of', type(num_integer))

print(num_float, 'is', 'type of', type(num_float))

print(num_complex, 'is', 'type of', type(num_complex))

print(string_var, 'is', 'type of', type(string_var))
      
print(bool_var, 'is', 'type of', type(bool_var))


print('Task 3', 'check type of value')
      
print(isinstance(num_integer , int))

print(isinstance(num_float , int))

print(isinstance(num_float , float))

print(isinstance(num_complex, complex))

print(isinstance(string_var , bool))

print('Task4', 'Check type of value (version 2)')


print('Is', num_integer, 'an instance of int?', isinstance(num_integer , int))

print('Is', num_float, 'an instance of int?',  isinstance(num_float , int))

print('Is', num_float, 'an instance of float?', isinstance(num_float , float))

print('Is', num_complex, 'an instance of complex?', isinstance(num_complex, complex))

print('Is', string_var, 'an instance of bool?', isinstance(string_var , bool))
