#************* DATA TYPE: NUMBERS*************

print(True+False)
#The output is 1.By default, True indicates 1 and False indicates 0.
print( True or False)
#if True is displayed,enter OR or perform the OR operation.
print(5//2)
#The output is 2 and // is the rounding operator.
print(5%2)
#The output is 1, and % is the modulp operator.
print(3**2)
#The ouput is 9 and ** indicates the power operator.
print(5+1.6)
#The output is 6.6. By default, the sum of the number of different precisons is the number of the higest precision type.


#************DATA TYPE: CHARACTER STRING**************

#Step 1 :- Basic operations on character strings:
s = 'python'
#Assign value python to variable S.
print(len(s))
#Output is 6. This function returns the object length.
print(s[0],s[2],s[5])
#The output is p y n. Elements are obtained by index.
print(s + '1',s*2)
#The output is python1 pythonpython , which indicates mergence and duplication.

#Step 2 :- Unchangeability of character strings:

s1 = 'Z' + s
#New character string Zython is generated and assigned to s1.
print("s:%s,s1:%s"%(s,s1))

#Data Type: List

animals = ['cat','dog','monkey']
print(animals)
#print elments from the list animal.
animals.append('fish')
print(animals)
#append function helps to add a new object to the end of a list.
animals.remove('fish')
print(animals)
#Remove function is used to remove the object form the list.
animals.insert(1,'monkey')
print(animals)
#Insert a specified object to a specified position in the list. The index indictes the position.
for i in enumerate(animals):
    print(i)
#Enumerate(sequence): Return an index sequence consisting of a data object that can be traversed and list the data and subscripts . This function is usually used in the loop.
squares = [x*2 for x in animals]
print(squares)

#Data Type: Tuple

t = (1,2,3)
print(t + (4,5))

#Data type: Dictionary

#First value assignment operations on dictionaries.
x = {'food':'spam','quantity':'4','color':'pink'}
print(x)
#Second value assignment operations on dictionaries.
X = dict(food='spam',quantity =4,color='Pink')
print(X)
d = x.copy()
d['color'] = 'red'
print(d)

#Data Type: Set

sample_set = {'prince','Techs'}
print("Data" in sample_set)
# The output is False. in is used to check whether an element exists in the set.
print('prince' in sample_set)
sample_set.add("sushil")
#The add function is used to add a new element in the set.
print(sample_set)
sample_set.remove("sushil")
# The remove function is used to remove an element from the set.
print(sample_set)
dict1 = {'name':'lee','age':'89','num':[1,2,3]}
print(dict1)
dict_copy = dict1.copy()
print(dict_copy)