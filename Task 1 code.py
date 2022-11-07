# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 19:25:00 2022

@author: Vivek
"""

print('Welcome, To register press 1')
print('To login press 2')
select1 = int(input('Enter a value- '))



def mail_enter(mail_id):
    count1 =0
    count2 = 0
    count3 = 0
    f = []
    a1 = 0
    a2 = 0
    c1 = 0
    c2 = 0
    c3 = 0
    final = 0
    special_char = [ '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+',',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', "/", ']', '^', '_', '`', '{', '|', '}', '~']

    for x in mail_id:
        f.append(x)
        
    length = len(f) 
    for x in range(length):
        if f[x] == '@':
            a1 = x
            c1 += 1
            
        elif f[x] == '.':
            a2 = x
            c2 += 1
            

    if c1 == 1 and c2 == 1:
        count1 += 1
        
    count2 = a2 - a1

    if a1 >2 and count2 > 3:
        count1 += 1
        
        
    for x in special_char:
        if f[0] == x:
            c3 += 1    
        else:
            c3 = c3
            
            
    if count1 == 2 and c3 < 1:
        return True
    else:
        return False
    

def char_search(values, search_for):
   search_at = 0
   search_res = False
# Match the value with each data element	
   while search_at < len(values) and search_res is False:
      if values[search_at] == search_for:
         search_res = True
      else:
         search_at = search_at + 1
   return search_res    



def password_check(pass1):
    d1 = 0
    letters = []
    ascii_num = []
    special_ascii = [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 58, 59, 60, 61, 62, 63, 64, 91, 92, 93, 94, 95, 96, 123, 124, 125, 126]
    digits_ascii = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
    uppercase_ascii = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
    lowercase_ascii = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
    
    
    for x in pass1:
        letters.append(x)
        
    for y in letters:
        ascii_num.append(ord(y))
        
    for i in special_ascii:
        if char_search(ascii_num, i) == True:
            d1 += 1
            break
        
        else:
            continue
        
    for i in digits_ascii:
        if char_search(ascii_num, i) == True:
            d1 += 1
            break
        
        else:
            continue
        
    for i in uppercase_ascii:
        if char_search(ascii_num, i) == True:
            d1 += 1
            break
        
        else:
            continue
        
    for i in lowercase_ascii:
        if char_search(ascii_num, i) == True:
            d1 += 1
            break
        
        else:
            continue 
        
    if d1 == 4:
        return True
    else:
        return False




if select1 == 1:
    print('To register, Please enter valid mail ID and password')
    mail = input('Enter valid mail id- ')
    while mail_enter(mail) == False:
        print('You have entered wrong mail id')
        mail = input('Enter valid mail id- ')
        
        
    password = input('Enter valid password- ')
    while password_check(password) == False:
        print('You have entered invalid password')
        password = input('Enter valid password- ')
        
        
        
    f = open('mailregister.txt', 'a')
    f.write('\n')
    f.write(mail)

    f = open('mailregister.txt', 'a')
    f.write("\n")
    f.write(password)

    f.close()

    print('You have successfully registered')
        
        
elif select1 == 2:
    mail_login = input('Enter registered mail id- ')


    f = open('mailregister.txt', 'r')
    stored_details = f.read().split()
    #print(stored_details)
    for x in range(len(stored_details)):
        if mail_login == stored_details[x]:
            stored_mail = stored_details[x]
            stored_password = stored_details[x+1]
     
            
    if stored_mail == mail_login:
        pass_login = input('Enter Password- ')
        
         
    else:
        print('You have not registered. To register, run the program again. Thank you')
 
                   
    f.close()

       
    counter3 = 0
        
    if pass_login == stored_password:
        print('You have successfully logged in')
        
    else:
        print('You have entered incorrect password.')
        print('Press 1 to retieve old password')
        print('Press 2 to add new password')
        counter3 = int(input())
        if counter3 == 1:
            print(stored_password)
            print('Thank you for logging in.')
            
        elif counter3 == 2:
            new_password = input('Enter new password- ')
            f = open('mailregister.txt', 'a')
            f.write(stored_mail)
            f = open('mailregister.txt', 'a')
            f.write(new_password)
            f.close()
            print('Thank you for loggin in.')
            
            
        else:
            print('You have entered a wrong entry. Please try again. Thank you. ')
          
            
        
else:
    print('You have entered a wrong entry. Please try again. Thank you. ')
    

     
    
        
        
        
        
        
        
        
        
        