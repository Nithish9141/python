#Data Types and Variables


#variables are the name given to the memory location


#rules for the variables

#1.first letter A-Z or a-z or _
#2.no number in the first character
#3.special character are not allowed
#4.variable are case senstive
#5.donot use keywords. there are 32 keywords

#example

##a=10
##A=46
##_ab=46
##uday=467
##print()
##print(a)
##print(A)
##print(_ab)
##print(uday)



#Data Types

#1.primitive DataTypes
#2.non-primitive DataTypes

##1.primitive DataTypes------>which stores only one values
##>int
##>float
##>str
##>char
##
##
##2.non-primitive DataTypes----->which stores more than one values
##>list
##>tuple
##>dict
##>set


###example
###1.int
##a=5
###2.float
##b=45.643
###3.string
##c="uday"
###4.char
##d='d'




#if-else


#syntax

##if(condition):
##    //code
##    //code
##    //code
##
##else:
##    //code
##    //code
##    //code
##

#example
#1.simple if-else
#age=25

##if(age>=18):
##    print("eligible to vote")
##    print("eligible to drive")
##else:
##    print("not eligible to vote")
##    print("not eligible to drive")
##    


#2.if elif else statement
#to check more than one conditon

#syntax

##if(condition):
##    //code
##    //code
##
##elif(condtion):
##    //code
##    //code
##elif(condition):
##    //code
##    //code
##else:
##    //code
##    //code

##a=60
##if(a>90):
##    print("good")
##elif(a>70):
##    print("better")
##elif(a>59):
##    print("luck")
##elif(a>58):
##    print("good luck")
##else:
##    print("fail")




#3.nested if-else statement

#syntax

##if(condtion):
##    if(condition):
##        //code
##        //code
##    else:
##        //code
##        //code
##
##else:
##    //code
##    //code
##a=10
##b=40
##c=30
##
##
##if(a>b):
##    if(a>c):
##        print("a is grater")
##    else:
##        print("c is greater")
##
##else:
##    if(b>c):
##        print("b is greater")
##    else:
##        print("c is greater")
##







##loops---->iterate

##1.for
##2.while


#for loop

##syntax

##for i in range(start_index,end_index,increment):
##    //code
##    //code


#question1
#1.print the number for 1 to n
##for i in range(1,10,2):
##    print(i)
#2.print the even number from 1 to n
##for i in range(1,100):
##    if(i%2==0):
##        print(i)

#3.prime number


        
#4.sum of number from 1 to n
##sum=0
##for i in range(1,10):
##    sum=sum+i
##
##print(sum)


#5.sum of even number from 1 to n

##for i in range(1,10):
##    print(i*5)





















