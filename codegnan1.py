a=9
b=5

##arthemetic operators

print(a+b)## add
print(type(a+b))
print(a-b)#sub
print(type(a-b))
print(a*b)#mul
print(type(a*b))
print(a/b)#division
print(type(a/b))
print(a//b)#float division
print(type(a//b))
print(a%b)#modelues
print(type(a%b))
print(a**b)#exponential
print(type(a**b))

##comparision operators

print(a<b)#less than
print(a>b)#greaterthan
print(a<=b)#lessthan or equalto
print(a>=b)#greaterthan or equalto
print(a==b)#equalto
print(a!=b)#not equalto
print(type(a>b ),type(a>=b),type(a<b),type(a<=b),type(a==b),type(a!=b))

##logical operators

print(a and b)#logical and operation
print(a<=b)and(a>=b)
print(a or b)#logical or operation
print(a<=b)or(a!=b)
print(a, not b)#logical not operation
print(a==b)
print(a!=b)

##assignment operators

a=9
b=3
a += b# a= a+b (add and assignment)
print(a)
a -= b# a= a-b(sub and assignment)
print(a)
a *= b# a= a*b (mul and assignment)
print(a)
a %= b# a= a%b  (modules and assignment)
print(a)
a /= b# a= a/b (division and assignment)
print(a)
a //= b# a= a//b (float division and assignment)
print(a)
a **= b# a= a**b (expontential and assignment)
print(a)

##membership operators

print (2 in [1,2,3,4])# checking the value present in the sequence or list
print (2 in [3,6,7.8,60])# checking the value present in the sequence or list
print (2 not in[1,2,3,7.9])# checking the value present in the sequence or list
print (26 not in[1,2,3,7.9])# checking the value present in the sequence or list
print (26,2 not in[1,2,3,7.9])
print ((26 not in[1,2,3,7.9]),(2 not in[1,2,3,7.9]))


##identity operaters

num= 3
print(id(num))# identify the id of num value

n1=6
n2=6
print(id(n1))
print(id(n2))#here the num values are equal so then the id value is also same

l1=[1,2,4.5,8]
l2=[1,2,4.5,8]
print(id(l1))
print(id(l2))#here the num values are equal but the id value  values are different beacause the values are in one list
print (l1 is l2)#here id of l1 is not id of l2 then it false


l1=[1,2,4.5,8]
l1=l2
print(id(l1))
print(id(l2))# here the l1 id is goes for l2 id also thats why there both ids are equal
print (l1 is l2)#here id of l1 is id of l2 then it true


l1=20
l2=30
print (l1 is not l2)
print (l1 is l2)

##bitwise opertors

print(100&25)#and(&)operation
print(~2)#not(~)operation
print(~-2)#not(~)operation
print(~2,~-3)#not(~)operation
print(100|25)#or(|)operation
print(30^2)#xor(^)operation
print(30<<1)#bitwise left operation
print(30>>2)#bitwise right operation


##strings

S=["1","g","14.6","f","hai","k"]
print(S[4])#string find list
print(S[0:])#string formate from starting to ending
print(S[0:4])#string slicing
print(S[:5])#string slicing
print(S[0:-1])#string slicing
print(S[ : ])#string slicing
print(S[-1:4])#string slicing but no element in between th two list numbers
print(S[-1:-5])#string slicing but no element in between th two list numbers
print(S[-5:-1])#string slicing
print(S[1:2:3])#string slicing but in between those numbers
print(S[::-1])#string  reverse slicing
print(S[1:5:-1])#string  reverse slicing but here deosnot reverse takes place   
print(S[-1:-6:-1])#string  reverse slicing
print(S[-1:-7:-1])#string  reverse slicing


##string case conversation

s="I am Sivangi Kiran"
print(s.lower())
print(s.upper())
print(s.title())
print(s.capitalize())
print(s.swapcase())

##remove blank spaces

s="      I am Sivangi Kiran    "
print(s.strip())
print(s.rstrip())
print(s.lstrip())

s="@@@kir@n@@@"
print(s.strip('@'))
print(s.rstrip('@'))
print(s.lstrip('@'))

##split the string

s="I am Sivangi Kiran"
print(s.split())
print(s.rsplit())
print(s.split('a'))


##join methods

l=("hi","this","is","kiran","sivangi","from","andhra pradesh")
print(''.join(l))
print('@'.join(l))
print('1432'.join(l))
print('_'.join(l))

print('@'.join("sivangi kiran".split()))


##finding(),indexing(),replace().

s="I am Sivangi Kiran"
print(s.find('n'))#finding()
print(s.find(''))
print(s.find('n,n'))


print(s.index('n'))#indexing()
print(s.index('i'))
print(s.index(''))

print(s.replace('i','!'))#replace()
print(s.upper().replace('K','#'))
print(s.lower().replace('a','#'))

##checking function()

s1="abcd"
s2="abc1234"
s3="12345"
print(s1.isalpha(),s2.isalpha(),s3.isalpha()) #checking the given string is having only alphabets by ujsing isalpha()
print(s1.isalnum(),s2.isalnum(),s3.isalnum())#checking the given string is having both alphabets and digits by using isalmun()
print(s1.isdigit(),s2.isdigit(),s3.isdigit()) #checking the given string is having only digits by using isdigits()

##string comparision

s1="abcds"
s2="abcdefgh"
print(s1<s2)#checking the given string is having in the dictionary order and  by that order is declaration the greater
print(s1>s2)


##LIST[]

l=[1,2,3,'hi','a','b',2.3,1,2]
print(l[0])  #index value
print(l[-1])
l[0]=100  #assign the value in the index vaslue #mutable operation
print(l)


lst=[]
lst1=list() # chcking the data type
print(type(lst),type(lst1))

s="sivangi kiran"
l=list(s)  #convert the string into list
print(l)
print(type(s),type(l))


##l=list(map(str,input().split()))#reading list of string values from user,
##l1=list(map(int,input().split()))#reading list of integer values from user
##l2=list(map(float,input().split()))#reading list of float values from user
##print(l,l1,l2)""

#list concatination

l1=[1,2,3,4,5]
l2=[6,7,8,9,0]
print(l1+l2)

#list repetation by using '*'

l1=[1,2,3,4]
print(l1*4)

##list methods

#append()
l=[1,2,3,'hi','a','b',2.3,1,2]
l.append(100)
print(l)

#extend()
l=[1,2,3,'hi','a','b',2.3,1,2]
l1=[100,200,300]
l.extend(l1)
print(l)

# Using a extend in tuple
a = [1, 2, 3]
b = (4, 5)
a.extend(b)
print(a) 

# Using a extend in set
a = [1, 2, 3]
b = {4, 5}
a.extend(b)
print(a)  

# Using a extend in string
a = ['a', 'b']
b = "cd"
a.extend(b)
print(a)


#insert()

l=[1,2,3,'hi','a','b',2.3,1,2]
l.insert(100,'kiran')
print(l)

l=[1,2,3,'hi','a','b',2.3,1,2]
l.insert(0,'kiran')
print(l)

#index()

l=[1,2,3,'hi','a','b',2.3,1,2]
ind=l.index('a')
print(ind)

l=[1,2,3,'hi','a','b',2.3,1,2]
ind=l. backwardindex(1)
print(ind)

























