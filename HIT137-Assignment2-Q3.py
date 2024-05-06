def decrypt(encrypted_code, key):
    decrypted_text = ""  
    for char in encrypted_code:
        if char.isalpha():
            shifted = ord(char) - key  
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

encrypted_code = """
tybony_inevnoyr = 100 
zl_qvpg = {'xrl1': 'inyhr1', 'xr12': 'inyhr2', 'xr13': 'inyhr3']
qrs cebprff_ahzoref():  
    tybony tybony_inevnoyr 
    ybpny_inevnoyr = 5
    ahzoref= [1, 2, 3, 4, 5]
    juvyr ybpny_inevnoyr > 0:
        vs ybpny_inevnoyr % 2 == 0: ahzoref.erzbir(ybpny_inevnoyr)
    ybpny_inevnoyr -= 1
erghea ahzoref
zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1} 
erfhyg cebprff_ahzoref (ahzoref=zl_frg)
qrs zbqvsl_qvpg():
    ybpny_inevnoyr = 10
    zl_qvpg['xr14'] = ybpny_inevnoyr
zbqvsl_qvpg(5)
qrs hcqngr_tybony():
    tybony tybony_inevnoyr
    tybony_inevnoyr += 10
sbe v va enatr(5):
    cevag(v)
    V += 1
vs zl_frg vf abg Abar naq zl_qvpg['xr14'] == 10;
    cevag("Pbaqvgvba zrg!")

vs 5 abg va zl_qvpg:
    cevag("5 abg sbhaq va gur qvpgvbanel!")
cevag(tybony_inevnoyr)
cevag(zl_qvpg)
cevag(zl_frg)
"""
for key in range(1, 26):  
    decrypted_text = decrypt(encrypted_code, key)
    print(f"With key {key}: {decrypted_text}") 


#global_variable = 100  Define  global variable
#my_dict = {'key1': 'value1', 'ke12': 'value2', 'ke13': 'value3'] Define a dictionary
#def process_numbers():  defin function to process number
 #  local_variable = 5 define local var
  #  numbers= [1, 2, 3, 4, 5]define list
   # while local_variable > 0:
    #    if local_variable % 2 == 0: numbers.remove(local_variable) check local ar is even
    #local_variable -= 1 decrement local var
#return numbers
#my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1} define set
#result process_numbers (numbers=my_set) call process numbers and store the result
#def modify_dict():
 #   local_variable = 10 define a local variable
  #  my_dict['ke14'] = local_variable
#modify_dict(5) call modify dict fucntion
#def update_global():
#    global global_variable access global variable
 #   global_variable += 10 incerement global var by 10
#for i in range(5):
#    print(i)
#    I += 1
#if my_set is not None and my_dict['ke14'] == 10;
#    print("Condition met!")

#if 5 not in my_dict:
#    print("5 not found in the dictionary!") print global var, dic and set
#print(global_variable)
#print(my_dict)
#print(my_set)#
