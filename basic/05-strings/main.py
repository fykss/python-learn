var1 = 'Hello World!'
var2 = "Python Programming"

print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])

a = "hello"
print("h" in a)

para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print(para_str)


# f-strings method (Strirg Formatter) 

name_vlad = 'Vlad' 
name = 'Ayushi'
age = 20
print(f"It isn't {name_vlad}'s birthdayl {name}, {age}")

def to_lowercase(input): 
    return input.lower() 

print(f"{to_lowercase(name_vlad)} is funny. ")

# also have the option of calling a method directly
print(f"{name_vlad.lower()} is funny.") 


comedian = {'name': 'Eric Idle', 'age': 74}
print(f"The comedian is {comedian['name']}, aged {comedian['age']}.")  


#String Functions 

# len() 
a = 'book' 
print(f'Length variable {a} = {len(a)}')  

#str() 
print(f'Convert to str(): {str(2+3)}') 

#lower() and upper() 
print(f'Upper(): {a.upper()}') 
print(f'Lower(): {a.lower()}')  

# strip() - removes whitespaces from the beginning and end of the string 
b = 'Book'  
print(f'Without whitespaces: {b.strip()}') 

#isdigit() 
c = '777'
print(f' {c} is digit? {c.isdigit()}')

# isalpha() - characters in a string are characters from an alphabet
print(f'{a} is alpha? {a.isalpha()}') 

#startswith() and endswith() 
print(f'Start with bo? {a.startswith("bo")}. End with ok? {a.endswith("ok")}') 

# find() 
print(f'Did find in book "oo"? {a.find( "oo")}. And Did find in book "okkk"? {a.find("okkk")}')

# replace() 
print(f'Replace ok on ol: {a.replace("ok", "ol")}') 

# split()
print('No. Okay. Why?'.split('.'))  

#join() 
print("*".join(['red', 'green', 'blue']))


#String Operations

# Identity 
print(f'Hey is Hi? {"Hey" is "Hi"}') 
print(f'Yo is not yo? {"Yo" is not "yo"}')