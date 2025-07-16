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























