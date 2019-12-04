# Creating a Nested Dictionary  
Dict = {
        1: 'Vlad', 
        2: 'World',  
        3: {'A' : 'Welcome', 'B' : 'To', 'C' : 'Geeks'}
} 
  
print(Dict)


Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 
  
# Adding elements one at a time 
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ") 
print(Dict) 


# Accesing a element from a Dictionary  
  
# Creating a Dictionary  
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'} 
  
# accessing a element using key 
print("Acessing a element using key:") 
print(Dict['name']) 
  
# accessing a element using key 
print("Acessing a element using key:") 
print(Dict[1]) 
  
# accessing a element using get() 
# method 
print("Acessing a element using get:") 
print(Dict.get(3)) 

# Difference between Dict['name'] and metod get(): https://www.geeksforgeeks.org/get-method-dictionaries-python/