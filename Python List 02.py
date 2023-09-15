#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("***********menu*********")
print("1:list\n2:tuple\n3:set\n4:dictionary")
print("*************************")
ab=int(input("ENTER YOUR CHOICE"))
if ab==1:
        while True:
            print('***list***')
            print("1:defination of list\n2:change item\n3:add item\n4:remove item\n5:exit")
            print("***********************")
            ab11=int(input("enter a number"))
            if ab11==1:
                print("""DEFINATION OF LIST:-Lists are used to store multiple items in a single variable.
                      Lists are one of 4 built-in data types in Python used to store collections of data, 
                      the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
                      Lists are created using square brackets""")
            elif ab11==2:
                l=["thane","mumbai",421201,"raj"]
                print(l)
                l[0]="kalyan"
            elif ab11==3:
                s=["thane","mumbai",421201,"raj"]
                print(s)
                s.append("thakurli")
                print(s)
            elif ab11==4:
                l=["thane","mumbai",421201,"raj"]
                print(l)
                l.remove("thane")
                print(l)
            else:
                break
if ab==2:
    while True:
        print("*******tuple*******")
        print("1:tuple defination\n2:update\n3:access\n4:exit")
        ab12=int(input("enter a number"))
        if ab12==1:
            print("""DEFINATION OF TUPLE:-Tuples are used to store multiple items in a single variable.
            Tuple is one of 4 built-in data types in Python used to store collections of data,
            the other 3 are List, Set, and Dictionary, all with different qualities and usage.
            A tuple is a collection which is ordered and unchangeable.Tuples are written with round brackets.""")
        elif ab12==2:
            a=("apple","banana","chery")
            b=list(a)
            b[1]="kiwi"
            a=tuple(b)
            print(a)
        elif ab12==3:
            a=("apple","banana","cherry")
            print(b[0])
        else:
            break        
if ab==3:
     while True:
        print("******************set******************")
        print("1:defination of set\n2:access\n3:add\n4:remove\n5:exist")
        ab13=int(input("ENTER YOUR CHOICE"))
        if ab13==1:
                print("""DEFINATIO OF SET:-Sets are used to store multiple items in a single variable.
                  Set is one of 4 built-in data types in Python used to store collections of data,
                  the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
                  A set is a collection which is unordered, unchangeable*, and unindexed.""")
        elif ab13==2:
                a={"ayodhya","shree ram","shrikrushna","vijaya",1234}
                for b in a:
                    print(b)
        elif ab13==3:
                k={"ayodhya","shree ram","shrikrushna","vijaya",1234}
                k.add("sita")
                print(k)
        elif ab13==4:
                d={"ayodhya","shree ram","shrikrushna","vijaya",1234}
                d.remove(1234)
                d.remove("ayodhya")
                print(d)
        else:
            break
if ab==4:
    while True:
        print("**********DICTIONARY***********")
        print("1:DEFINATION\n2:ACCESS\n3:ADD\n4:CHANGE\n5:REMOVE\n6:EXIT")
        ab14==int(input("ENTER YOUR CHOICE:-"))
        if ab14==1:
                print("""DEFINATION OF DICTIONARY:-Dictionaries are used to store data values in key:value pairs
                    A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
                    Dictionaries are written with curly brackets, and have keys and values:""")
        elif ab14==2:
                a={"name":"abhijit rana","age":"1002","gender":"male","married status":"unmarried"}
                x=a["name"]
                print(x)
        elif ab14==3:
                a={"name":"abhijit rana","age":"1002","gender":"male","married status":"unmarried"}
                a.update("id",1)
                print(a)
        elif ab14==4:
                a={"name":"abhijit rana","age":"1002","gender":"male","married status":"unmarried"}
                a["name"]="allu arjun"
                print(a)
        elif ab14==5:
                a={"name":"abhijit rana","age":"1002","gender":"male","married status":"unmarried"}
                a.pop("age")
                print(a)
        else:
            break
print("task completed")


# In[ ]:




