# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 10:01:06 2018

@author: alvin
"""

#def search2(elem, set):
#    if len(set) == 0:
#        return False
#    elif len(set) == 1:
#        return elem == set[0]
#    else:
#        front = set[:len(set)//2-1]
#        back = set[len(set)//2:]
#        return search2(elem,front) or search2(elem,back)
#
#L = [1,2,3]
#print(search2(1, L))
#print(search2(2, L))
#print(search2(3, L))

#class Person(object):
#    def __init__(self, name):
#        self.myName = name
#    def speak(self, stuff):
#        return self.myName + " says: " + stuff
#    def name(self):
#        return self.myName
#  
#class Student(Person):
#    def _init_(self, name):
#        Person.__init__(self, name);
#
#class Professor(Person):
#    def speak(self, toWhom, stuff):
#        if isinstance(toWhom, Student):
#            words = self.name+ ' says: ' + toWhom.name() + '. It is obvious that ' + stuff
#        else:
#            words = self.name() + ' says: I think that ' + stuff
#        self.speak(self, words)
#
#Eric = Professor ('Eric')
#Alyssa = Student('Aly')
#John = Professor('John')
#
#
#print(Eric.speak(Alyssa, 'Hi there'))
#print(Eric.speak(John, 'Hi there'))

#def sort(L):
#    swap = True
#    step = 0;
#    while swap:
#        swap = False
#        for j in range(1, len(L)):
#            if L[j-1] > L[j]:
#                swap = True
#                temp = L[j]
#                L[j] = L[j-1]
#                L[j-1] = temp
#        step+=1;
#        print(len(L), step, L);
#L = [5, 4, 3, 2, 0];
#sort(L);

#def search1(elem, set):
#    if len(set) == 0:
#        return False
#    elif len(set) == 1:
#        return elem == set[0]
#    else:
#        front = set[:len(set)//2]
#        back = set[len(set)//2:]
#        return search1(elem,front) or search1(elem,back)
#def search2(elem, set):
#    if len(set) == 0:
#        return False
#    elif len(set) == 1:
#        return elem == set[0]
#    else:
#        front = set[:len(set)//2-1]
#        back = set[len(set)//2:]
#        return search2(elem,front) or search2(elem,back)
#import random
#def search3(elem, set):
#    if len(set) == 0:
#        return False
#    elif len(set) == 1:
#        return elem == set[0]
#    else:
#        next = random.choice(set)
#        if elem == next:
#            return True
#        else:
#            set.remove(next)
#            return search3(elem, set)
#        
#L = [5, 4, 3, 2, 0]
#print(search1(2, L));
#print(L)
#print(search2(2, L));
#print(L)
#print(search3(2, L));
#print(L)

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
        If there are no digits in s it 
        raises a ValueError exception. """
    summing = 0;
    digits = False;
    for char in s:
        if char in "1234567890":
            digits = True;
            summing+=int(char);
    if not digits:
        raise ValueError;
    return summing;
    
#print(sum_digits("a;35d4"))
#print(sum_digits("35d4"))
##print(sum_digits("a;d"))
#print(sum_digits("0213"))

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    largest = 0;
    count = -1;
    for num in L:
        if L.count(num)%2==1:
            if count == -1:
                largest = num;
                count = L.count(num);
            elif num>largest:
                largest = num;
                count = L.count(num);
    if count < 0:
        return None;
    return largest;
#
#print(largest_odd_times([2,2,4,4]))
#print(largest_odd_times([3,9,5,3,5,3]))
#print(largest_odd_times([2,22,4,4, 4, 2, 2, 2, 6, 36]))
#print(largest_odd_times([-2,-2, -2, -1]))

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    reverse = [];
    if type(L) != list:
        return L;
    else:
        index = len(L)-1;
        while index >= 0:
            #print(L[index]);
            reverse.append(deep_reverse(L[index]));
            #print("Inside", reverse);
            index -=1;
        #print(reverse);
        L[:] = reverse;
        return reverse;

#L = [[1, 2], [3, 4], [5, 6, 7]]
#L = [5, 4, 3, 2, 1];
#L = [[]]
#L = [[1, [2, 6, 7]], [3], 4, 6]
#deep_reverse(L)
#print(L)

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain
        N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the 
        corresponding value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    trans = {}
    for index in range(len(map_from)):
        trans[map_from[index]] = map_to[index];
    decoded = "";    
    for char in code:
        decoded += trans[char];
    return (trans, decoded)
    
#print(cipher("abcd", "dcba", "dab"))
#print(cipher("cat", "dog", "cattac"))

def sum_digits_recur(n):
    '''
    n: a non-negative integer
    Recursively calculates and returns the sum (an integer) 
    of the digits of n
    '''
    summing = 0;
    power = len(str(n))-1;
    if n < 10:
        return n;
    else:
        summing += n//(10**power) + sum_digits_recur(n%10**power);
        return summing;
print(sum_digits_recur(1231));
print(sum_digits_recur(1));
print(sum_digits_recur(0));
print(sum_digits_recur(9999956));

def f (a, b):
    print(a, b);
    return a+b;    

def score(word, f):
    """
       word: a string of length > 1 of alphabetical 
             characters (upper and lowercase)
       f: a function that takes in two ints and returns an int
       Returns the score of word as defined by the following:
    1) Score for each letter is its location in the alphabet 
       (where a=1 ... z=26) times its distance from start of word.  
    2) The score for a word is the result of applying f to the
       scores of the word's two highest scoring letters. 
    """
    higher = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    lower = higher.lower();
    letterScoreHigher = 0;
    letterScoreLower = -1;
    for index in range(len(word)):
        letterScore = index;
        if word[index] in higher:
            letterScore *= higher.index(word[index])+1;
        elif word[index] in lower:
            letterScore *= lower.index(word[index])+1;
        if letterScore > letterScoreHigher:
            letterScoreLower = letterScoreHigher;
            letterScoreHigher = letterScore;
        elif letterScore > letterScoreLower:
            letterScoreLower = letterScore;
        print(index, letterScore);
    return f(letterScoreHigher, letterScoreLower);
#
print(score('adD', f), "\n")
print(score('azZfg', f))

class myDict(object):
    """ Implements a dictionary without using a dictionary """
    def __init__(self):
        """ initialization of your representation """
        self.key = [];
        self.value = [];
        
    def assign(self, k, v):
        """ k (the key, immutable object) and v (the value) """
        if k in self.key:
            index = (self.key).index(k);
            self.value[index] = v;
        else:
            self.key.append(k);
            self.value.append(v);
        
    def getval(self, k):
        """ k, immutable object  """
        if k not in self.key:
            raise KeyError(k);
        else:
            return (self.value)[(self.key).index(k)];
        
    def delete(self, k):
        """ k, immutable object """   
        if k not in self.key:
            raise KeyError(k);
        else:
            index = (self.key).index(k);
            del(self.key[index]);
            del(self.value[index]);

    def printing(self):
        l = "{";
        for key in self.key:
            l+= str(key) + ": " + str(self.getval(key)) + ", ";
        l += "}";
        print(l);


#d1 = myDict()
#d1.assign(10,2)
#print(d1.getval(10))
#d1.assign(3,3)
#print(d1.getval(3))
#print(d1.getval(10))
#d1.assign(4,2)
#print(d1.getval(4))
#d1.assign(3,6)
#print(d1.getval(3))
#print(d1.getval(10))
#print(d1.getval(3))
#print(d1.getval(4))
#d1.delete(3)
#d1.delete(10)
#print(d1.getval(4))

#d1.printing()
##d1.delete(5);
#d = {};
#d[1]=2;
##print(d);
##del(d[2]);
##print(d[2]);
#d1.getval(2);