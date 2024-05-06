# Decryption of the encrypted code.

global_variable = 100     #Global variable declaration
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def process_numbers():
    global global_variable #To use the global variable inside the function
    local_variable = 5
    numbers = [1, 2, 3, 4, 5]
    
    while local_variable > 0:
        if local_variable % 2 == '0': #Modified the scenario to check for even numbers
            numbers.remove(local_variable)
        local_variable -=1
        
    return numbers
    
my_set =  {1, 2, 3, 4, 5, 5, 4, 3, 2, 1} #Modified the syntax to creat a set
result = process_numbers(numbers=my_set) #Eliminated the unneeded contention

def modify_dict(): #To alter the global dictionary within the function
    local_variable = 10
    my_dict['key4'] = local_variable
    
modify_dict(5) #Modified the function call

def update_global():
    global global_variable #To correct the global variable within the function
    global_variable += 10
    
for i in range(5):
    print(i)
    i += 1 #Eliminated the unneeded increment statement
    
update_global() #Run the function without providing any parameters
if my_set is not None and my_dict['key4'] == 10: #Revised the condition to verify the value
    print("Condition met!")
    
if 5 not in my_dict: #Modified to verify the presence of the number 5 among the elements of my_dict
    print("5 not found in the dictionary!")
    
print(global_variable)
print(my_dict)
print(my_set)

# Dycryption fuction
def decrypted (text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
                elif char.isupper():
                    if shifted > ord ('Z'):
                        shifted -= 26
                    elif shifted < ord ('A'):
                        shifted += 26
            decrypted_text += chr(shifted)
        else: 
            decrypted_text += char
            return decrypted_text
        
#encrypted code
encrypted_code = "global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def process_numbers():
    global global_variable 
    local_variable = 5
    numbers = [1, 2, 3, 4, 5]
    
    while local_variable > 0:
        if local_variable % 2 == '0': 
            numbers.remove(local_variable)
        local_variable -=1
        
    return numbers
    
my_set =  {1, 2, 3, 4, 5, 5, 4, 3, 2, 1} 
result = process_numbers(numbers=my_set) 
def modify_dict(): 
    local_variable = 10
    my_dict['key4'] = local_variable
    
modify_dict(5) 

def update_global():
    global global_variable 
    global_variable += 10
    
for i in range(5):
    print(i)
    i += 1 
    
update_global() 
if my_set is not None and my_dict['key4'] == 10: 
    print("Condition met!")
    
if 5 not in my_dict: 
    print("5 not found in the dictionary!")
    
print(global_variable)
print(my_dict)
print(my_set)"
original_code = decrypted(encrypted_code)
print(original_code)


                
