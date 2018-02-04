#def f(a, b):
#    return a>b;
#
#def dict_interdiff(d1, d2):
#    newd1 = d1.copy();
#    newd2 = d2.copy();
#    intersect = {};
#    different = {};
#    for key in d1:
#        if key in d2:
#            intersect[key] = f(newd1.pop(key), newd2.pop(key));
#    for key in newd1:
#        different[key] = newd1[key];
#    for key in newd2:
#        different[key] = newd2[key];
#    return (intersect, different);
#
#d1 = {1:30, 2:20, 3:30}
#d2 = {1:40, 2:50, 3:60}
#print(dict_interdiff(d1, d2));

#def f(i):
#    return i + 2
#def g(i):
#    return i > 5;
#    
#def applyF_filterG(L, f, g):
#    if len(L) == 0:
#        return -1;
#    filtered = [];
#    maxNumber = -1;
#    for i in L:
#        if g(f(i)):
#            filtered.append(i);
#            if i > maxNumber:
#                maxNumber = i;
#    L[:] = filtered;
#    return maxNumber;
#    
#L = [0, -10, 6, 5, -4]
#print(applyF_filterG(L, f, g))
#print(L)

#def flatten(aList):
#    newList = [];
#    if type(aList) != list:
#        newList.append(aList)
#        return newList;
#    else:
#        for item in aList:
#            newList.extend(flatten(item));
#    return newList;
#    
#aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5];
#print(flatten(aList));

#def Square(x):
#    return SquareHelper(abs(x), abs(x))
#
#def SquareHelper(n, x):
#    if n == 0:
#        return 0
#    return SquareHelper(n-1, x) + x
#
#print(Square(7));

#def genPrimes():
#    primes = [];
#    start = 2;
#    flag = True;
#    while True:
#        flag = True;
#        for prime in primes:
#            if start%prime == 0:
#                flag = False;
#                break;
#        if flag:
#            primes.append(start);
#            yield start;
#        start += 1;

#trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si', '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
#
#def convert_to_mandarin(us_num):
#    mandarin = [];
#    num = int(us_num);
#    while num//10>0:
#        if num//10 != 1:
#            mandarin.append(trans[str(num//10)]);
#        mandarin.append(trans["10"]);
#        num = num%10;
#    if num != 0:
#        mandarin.append(trans[str(num%10)]);
#    if mandarin == []:
#        return trans[us_num];
#    return " ".join(mandarin);

#def longest_run(L):
#    run = 0;
#    largestStart = 0;
#    index = 0;
#    while index < len(L)-1:
#        before = index;
#        after = before + 1;
#        count = 0;
#        if after < len(L):
#            if L[before] == L[after]:
#                while L[before] == L[after]:
#                    count += 1;
#                    before += 1;
#                    after += 1;
#                    if after >= len(L):
#                        break;
#            if L[before] <= L[after]:
#                while L[before] <= L[after]:
#                    count += 1;
#                    before += 1;
#                    after += 1;
#                    if after >= len(L):
#                        break;
#                if count > run:
#                    run = count;
#                    largestStart = index;
#            if L[before] >= L[after]:
#                while L[before] >= L[after]:
#                    count += 1;
#                    before += 1;
#                    after += 1;
#                    if after >= len(L):
#                        break;
#                if count > run:
#                    run = count;
#                    largestStart = index;
#            index = before;
#    runSum = 0;
#    index = largestStart;
#    while largestStart < index + run+1:
#        runSum+= L[largestStart];
#        largestStart+=1;
#    return runSum;
#L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
#print(longest_run(L));

#class Person(object):
#    def __init__(self, name):
#        #create a person with name name
#        self.name = name
#        try:
#            firstBlank = name.rindex(' ')
#            self.lastName = name[firstBlank+1:]
#        except:
#            self.lastName = name
#        self.age = None
#    def getLastName(self):
#        #return self's last name
#        return self.lastName
#    def setAge(self, age):
#        #assumes age is an int greater than 0
#        #sets self's age to age (in years)
#        self.age = age
#    def getAge(self):
#        #assumes that self's age has been set
#        #returns self's current age in years
#        if self.age == None:
#            raise ValueError
#        return self.age
#    def __lt__(self, other):
#        #return True if self's name is lexicographically less
#        #than other's name, and False otherwise
#        if self.lastName == other.lastName:
#            return self.name < other.name
#        return self.lastName < other.lastName
#    def __str__(self):
#        #return self's name
#        return self.name
#        
#class USResident(Person):
#    """ 
#    A Person who resides in the US.
#    """
#    def __init__(self, name, status):
#        """ 
#        Initializes a Person object. A USResident object inherits 
#        from Person and has one additional attribute:
#        status: a string, one of "citizen", "legal_resident", "illegal_resident"
#        Raises a ValueError if status is not one of those 3 strings
#        """
#        Person.__init__(self, name);
#        if status!="citizen" and status!="legal_resident" and status!="illegal_resident":
#            raise ValueError;
#        else:
#            self.status = status;
#        
#    def getStatus(self):
#        """
#        Returns the status
#        """
#        return self.status;
#
#a = USResident('Tim Beaver', 'citizen')
#print(a.getStatus())
#b = USResident('Tim Horton', 'non-resident')

#class Person(object):     
#    def __init__(self, name):         
#        self.name = name     
#    def say(self, stuff):         
#        return self.name + ' says: ' + stuff     
#    def __str__(self):         
#        return self.name  
#
#class Lecturer(Person):     
#    def lecture(self, stuff):         
#        return 'I believe that ' + Person.say(self, stuff)  
#
#class Professor(Lecturer):
#    def __init__(self, name):
#        Person.__init__(self, name);
#        self.name = name;
#        self.title = "Prof. ";
#    
#    def say(self, stuff): 
#        return self.title + self.name + ' says: ' + self.lecture(stuff)
#
#class ArrogantProfessor(Professor): 
#    def say(self, stuff): 
#        return self.title + self.name + ' says: It is obvious that ' + Lecturer.lecture(self, stuff)
#        
#    def lecture(self, stuff):
#        return 'It is obvious that ' + Lecturer.lecture(self, stuff);
#        
#e = Person('eric') 
#le = Lecturer('eric') 
#pe = Professor('eric') 
#ae = ArrogantProfessor('eric')
#
#
#print(e.say('the sky is blue'))
#print()
#print(le.say('the sky is blue'))
#print()
#print(le.lecture('the sky is blue'))
#print()
#print(pe.say('the sky is blue'))
#print()
##print(pe.lecture('the sky is blue'))
##print()
#print(ae.say('the sky is blue'))
##print()
##print(ae.lecture('the sky is blue'))

def general_poly(L):
    def polyfy(num):
        sumPoly = 0;
        exp = len(L)-1;
        for integer in L:
            sumPoly += integer * num**exp;
            exp -= 1;
        return sumPoly;
    return polyfy;
    
print(general_poly([1, 2, 3, 4])(10))