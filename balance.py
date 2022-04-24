import math


#This list will be referenced later as a dictionary for atributes of certain elements
#[element name, level of reactivity for single replacement, how many of that element show up when the element is alone,charge]
elements = [['H',4,2,1,1.01],
['Li',0,1,1,6.94],
['Be',0,1,2,9.01],
['He',0,1,0,4.00],
['B',0,1,3,10.81],
['C',9,1,4,12.01],
['N',0,2,3,14.01],
['O',0,2,2,16.00],
['F',0,2,1,19.00],
['Ne',0,1,0,20.20],
['Na',13,1,1,23.00],
['Mg',11,1,2,24.31],
['Al',10,1,3,26.98],
['Si',0,1,4,28.09],
['P',0,1,3,30.97],
['S',0,1,2,32.06],
['Cl',0,2,1,35.45],
['Ar',0,1,0,39.95],
['K',14,1,1,39.10],
['Ca',12,1,2,40.08],
['Sc',0,1,3,44.96],
['Ti',0,1,4,47.90],
['V',0,1,0,50.94],
['Cr',0,1,0,52.00],
['Mn',0,1,0,54.94],
['Fe',7,1,0,55.85],
['Co',0,1,0,58.93],
['Ni',0,1,2,58.70],
['Cu',3,1,1,63.55],
['Zn',8,1,2,65.38],
['Ga',0,1,3,69.72],
['Ge',0,1,2,72.59],
['As',0,1,3,74.92],
['Se',0,1,2,78.96],
['Br',0,2,1,79.90],
['Kr',0,1,0,83.80],
['Rb',0,1,1,85.47],
['Sr',0,1,2,87.62],
['Y',0,1,3,88.91],
['Zr',0,1,4,91.22],
['Nb',0,1,3,92.91],
['Mo',0,1,3,95.94],
['Tc',0,1,6,98.00],
['Ru',0,1,3,101.07],
['Rh',0,1,4,102.91],
['Pd',0,1,2,106.4],
['Ag',2,1,1,107.87],
['Cd',0,1,2,112.41],
['In',0,1,3,114.82],
['Sn',6,1,2,118.69],
['Sb',0,1,3,121.75],
['Te',0,1,2,127.60],
['I',0,2,1,126.90],
['Xe',0,1,0,131.30],
['Cs',0,1,1,132.91],
['Ba',0,1,2,137.33],
['Hf',0,1,4,178.49],
['Ta',0,1,5,180.95],
['W',0,1,6,183.85],
['Re',0,1,2,186.21],
['Os',0,1,3,190.20],
['Ir',0,1,3,192.22],
['Pt',0,1,2,195.09],
['Au',1,1,1,197.00],
['Hg',0,1,2,200.59],
['Tl',0,1,3,204.37],
['Pb',5,1,4,207.20],
['Bi',0,1,3,208.98],
['Po',0,1,2,209.00],
['At',0,1,0,210.00],
['Rn',0,1,0,222.00],
['Fr',0,1,0,223.00],
['Ra',0,1,2,226.03],
['Rf',0,1,0,261.00],
['Db',0,1,0,262.00],
['Sg',0,1,0,263.00],
['Bh',0,1,0,262.00],
['Hs',0,1,0,255.00],
['Mt',0,1,0,256.00],
['Ds',0,1,0,281],
['Rg',0,1,0,282],
['Cn',0,1,0,285],
['Nh',0,1,0,286],
['Fl',0,1,0,289],
['Mc',0,1,0,289],
['Lv',0,1,0,293],
['Ts',0,1,0,0],
['Og',0,1,0,294],
['La',0,1,0,138.91],
['Ce',0,1,0,140.12],
['Pr',0,1,0,140.91],
['Nd',0,1,0,144.24],
['Pm',0,1,0,145.00],
['Sm',0,1,0,150.4],
['Eu',0,1,0,151.96],
['Gd',0,1,0,157.25],
['Tb',0,1,0,158.93],
['Dy',0,1,0,162.50],
['Ho',0,1,0,164.93],
['Er',0,1,0,167.26],
['Tm',0,1,0,168.93],
['Yb',0,1,0,173.04],
['Lu',0,1,0,174.97],
['Ac',0,1,3,227.03],
['Th',0,1,4,232.04],
['Pa',0,1,5,231.04],
['U',0,1,3,238.029],
['Np',0,1,0,237.05],
['Pu',0,1,0,242.00],
['Am',0,1,0,243.00],
['Cm',0,1,0,247.00],
['Bk',0,1,0,247.00],
['Cf',0,1,0,251.00],
['Es',0,1,0,252.00],
['Fm',0,1,0,257.00],
['Md',0,1,0,258.00],
['No',0,1,0,250.00],
['Lr',0,1,0,260.00]]

#this function will balance combonation reactions but if you flip it, it will also balance decomposition
def balancecombo(side1a,side1b,side2):
    #defining variables for the next piece
    e1a = side1a[1]
    e1b = side1b[1]
    e2a = side2[1]
    e2b = side2[-1]
    b1a = 1
    b1b = 1
    b2 = 1
    b2 = 1
    if e1a == e2a and e1b == e2b:
        print(str(b1a) + side1a[0] + str(e1a) + '+' + str(b1b) + side1b[0] + str(e1b) + '=' + str(b2) + side2[0] + str(e2a) + side2[-2] + str(e2b) )
    else:
        # these are all of the different possibilities and it balances every case
        if e1a != e2a and e1b == e2b:
            if e1a == 1:
                b1a = e1a * e2a

            if e1a == 2:
                if e2a % 2 == 0:
                    b1a = e2a / 2

                if e2a % 2 != 0:
                    b1a = e2a
                    b2b = 2
                    b2a = 2

        if e1a == e2a and e1b != e2b:
            if e1b == 1:
                b1b = e1b * e2b

            if e1b == 2:
                if e2b % 2 == 0:
                    b1b = e2b / 2

                if e2b % 2 != 0:
                    b1a = 2
                    b1b = e2b
                    b2 = 2

        if e1a != e2a and e1b != e2b:
            if e1a == 1 and e1b == 1:
                b1a = e1a * e2a
                b1b = e1b * e2b

            if e1a == 1 and e1b == 2:
                if e2b % 2 == 0:
                    b1a = e1a * e2a

                    b1b = e2b / 2
                else:
                    b1a = e1a * e2a * 2

                    b1b = e2b
                    b2 = 2



            if e1b == 2 and e1b == 2:
                if e2a % 2 == 0:
                    b1a = e2a / 2

                if e2b % 2 == 0:
                    b1b = e2b / 2
                
                if e2a % 2 != 0:
                    b1a = e2a
                    b2a = 2

                if e2b % 2 != 0:
                    b1b = e2b
                    b2 = 2

        print(str(b1a) + side1a[0] + str(e1a) + '+' + str(b1b) + side1b[-2] + str(e1b) + '=' + str(b2) + side2[0] + str(e2a) + side2[2] + str(e2b) )


def balancesinglereplace(side1a,side1b,side2a,side2b):
    #this asigns a variable to each element on each side they may not line up they just make it easier for the next piece of code to sort them
   if len(side1a) == 2:
       e1a = side1a[1]
       e1b = side1b[1]
       e1c = side1b[-1]
  
   if len(side1a) != 2:
       e1a = side1b[1]       
       e1b = side1a[1]
       e1c = side1a[-1]
  
   if len(side2a) == 2:
       e2a = side2b[1]
       e2b = side2b[-1]              
       e2c = side2a[1]
 
   if len(side2a) != 2:
       e2a = side2a[1]
       e2b = side2a[-1]
       e2c = side2b[1]
 
   #find out which element is constant and put details about it in a list list 
   #The amount of it on side1 should be at index 2 and side 2 at index 5 
   #the lists that it can be found in are at indexes 0 and 2. The places in those lists where it can be found are indexes 1 and 4 this will help to find which element is with it later
   if len(side1a) == 2 and len(side2a) == 2:
       if side1b[1] == side2b[1]:
           const = [side1b, 1, e1b, side2b, 1, e2a]
       if side1b[1] == side2b[-1]:
           const = [side1b, 1, e1b, side2b, -1, e2b]
       if side1b[-1] == side2b[1]:
           const = [side1b, -1, e1c, side2b, 1, e2a]
       if side1b[-1] == side2b[-1]:
           const = [side1b, -1, e1c, side2b, -1, e2b]
 
   if len(side1a) == 2 and len(side2a) != 2:
       if side1b[1] == side2a[1]:
           const = [side1b, 1, e1b, side2a, 1, e2a]
       if side1b[1] == side2a[-1]:
           const = [side1b, 1, e1b, side2a, -1, e2b]
       if side1b[-1] == side2a[1]:
           const = [side1b, -1, e1c, side2a, 1, e2a]
       if side1b[-1] == side2a[-1]:
           const = [side1b, -1, e1c, side2a, -1, e2b]
   if len(side1a) != 2 and len(side2a) == 2:
       if side1a[1] == side2b[1]:
           const = [side1a, 1, e1b, side2b, 1, e2a]
       if side1a[1] == side2b[-1]:
           const = [side1a, 1, e1b, side2b, -1, e2b]
       if side1a[-1] == side2b[1]:
           const = [side1a, -1, e1c, side2b, 1, e2a]
       if side1a[-1] == side2b[-1]:
           const = [side1a, -1, e1c, side2b, -1, e2b]
 
   if len(side1a) != 2 and len(side2a) != 2:
       if side1a[1] == side2a[1]:
           const = [side1a, 1 ,e1b, side2a, 1, e2a]
       if side1a[1] == side2a[-1]:
           const = [side1a, 1, e1b, side2a, -1, e2b]
       if side1a[-1] == side2a[1]:
           const = [side1a,-1,e1c, side2a, 1, e2a]
       if side1a[-1] == side2a[-1]:
           const = [side1a,-1,e1c, side2a, -1, e2b]
    #find exact spot of other elements the values of the variable will be a list with the amount of that emement on side1 at index 0 and side 2 at index 1
   if const[0] == side1a:
       if const[3] == side2a:
           e1 = [side1a[const[1]*-1], side2b[1]]
           
           e2 = [side1b[1], side2a[const[4]*-1]]
           

       if const[3] == side2b:
           e1 = [side1a[const[1]*-1], side2a[1]]
           
           e2 = [side1b[1], side2b[const[4]*-1]]
           

   if const[0] == side1b:
       if const[3] == side2a:
           e1 = [side1b[const[1]*-1], side2b[1]]
           
           e2 = [side1a[1], side2a[const[4]*-1]]
           


       if const[3] == side2b:
           e1 = [side1b[const[1]*-1], side2a[1]]
           
           e2 = [side1a[1], side2b[const[4]*-1]]
           
       print(e1)
       a = e2[0]
       b = e1[0]
       c = const[2]
       d = const[5]
       e = e1[1]
       print(a)
       print(b)
       print(c)
       print(d)
       print(e)
       #this temporaily sets all variables equal to 1 as 0. 
       #This is because balancing multiplies by the number in front of it and multiplying by one doesn't change it. 
       # This way, when it adds the variable to the balancing process, it doesn't mess it up
       if a == 1:
           a = 0
       if b == 1:
           b = 0
       if c == 1:
           c = 0
       if d == 1:
           d = 0
       if e == 1:
           e = 0
       b1a = c + b + e
       b1b = a + d + e
       b2a = a + c + e
       b2b = a + d + b
       if b1a == 0:
           b1a = 1
       if b1b == 0:
           b1b = 1
       if b2a == 0:
           b2a = 1
       if b2b == 0:
           b2b = 1
       #this simplifies by finding the greatest common factor and dividing by it
       gcfa = math.gcd(b1a,b1b)
       gcfb = math.gcd(b2a,b2b)
       gcf = math.gcd(gcfa,gcfb)
       b1a/=gcf
       b1b/=gcf
       b2a/=gcf
       b2b/=gcf
       #This is determining where to put hings when they are printed so that elements are next to the right balancing amount
       if const[0] == side1a:
           s1a = side1b
           s1b = side1a
       else:
           s1b = side1b
           s1a = side1a
       if const[3] == side2a:
           s2a = side2b
           s2b = side2a
       else:
           s2b = side2b
           s2a = side2a

       print(str(b1a) + ''.join(map(str,s1a)) + '+' + str(b1b) + ''.join(map(str,s1b)) + '=' + str(b2a) + ''.join(map(str,s2a)) + '+' + str(b2b) + ''.join(map(str,s2b)))
   
#balances combustion reactions
def balancecombustion(side1a,side1b,side2a,side2b):
    
    
    s2a = side2a
    s2b = side2b
    #this starts by balancing everything by a multiple of 2. If this turns out to be unecessary, it corrects later
    b1a = 2
    b2a = side1a[1] * 2
    b2b = side1a[3]
    b1b = b2a * 2 + b2b
    b1b/=2
    #if everything is divisible by 2 then divide everything by 2
    if b2b % 2 ==0:
        b1a/=2
        b1b/=2
        b2a/=2
        b2b/=2
    
    print(str(int(b1a)) + ''.join(map(str,side1a)) + '+' + str(int(b1b)) + ''.join(map(str,side1b)) + '=' + str(int(b2a)) + ''.join(map(str,s2a)) + '+' + str(int(b2b)) + ''.join(map(str,s2b)))
    
    

def finishsinglereplace(side1a,side1b):
    if len(side1a) == 2:
        s1a = side1a[0]
        s2a = side1a
        s1b = side1b[0]
        s2b = side1b
    else:
        s1a = side1b[0]
        s2a = side1b
        s1b = side1a[0]
        s2b = side1a
    side2a = [s2b[1],s2b[2]]
    for i in elements:
        e2 = i[0]
        s1b = s1b.upper()
        if s1b == e2.upper():
            e2 = i
            side2b.append(e2[0])
            side2b.append(e2[2])
            side2b2 = side2b
            
            print(side2b)

    for i in elements:
        e1 = i[0]
        s1a = s1a.upper()
        if s1a == e1.upper():
            e1 = i
            side2a.append(e1[3])
            side2a.insert(0,e1[0])
            side2a2 = side2a
            print(side2a)
        
            
    print(side2a2)
    print(side2b2)
    print(s1b)
    print(e2)
    print(e1)
    #side2a = [e1[0], s2b[1], s2b[2], e1[3]]
    #side2b = [e2[0], e2[2]]
    
    print(''.join(map(str,side1a)) + '+' + ''.join(map(str,side1b)) + '=' + ''.join(map(str,side2a2)) + '+' + ''.join(map(str,side2b2)))
    balancesinglereplace(side1a,side1b,side2a2,side2b2)


def balancedoublereplace(side1a,side1b,side2a,side2b):
    
    #define variables for the equation that I derived
    a = side1a[1]
    b = side1a[3]
    c = side1b[1]
    d = side1b[3]
    
    #this multiplies everything in the least simplified way possible to encombas all cases
    b1a = c * d
    b1b = a * b
    b2a = a * d
    b2b = c * b
    if b1a == 0:
        b1a = 1
    if b1b == 0:
        b1b = 1
    if b2a == 0:
        b2a = 1
    if b2b == 0:
        b2b = 1
    
    #simplify
    gcfa = math.gcd(b1a,b1b)
    gcfb = math.gcd(b2a,b2b)
    gcf = math.gcd(gcfa,gcfb)
    b1a/=gcf
    b1b/=gcf
    b2a/=gcf
    b2b/=gcf

    #makes sure to print second side in the right order with the balancing amounts
    if side1a[0].upper() == side2a[0].upper():
        s2a = side2a
        s2b = side2b
    else:
        s2a = side2b
        s2b = side2a

    #print the answer
    print(str(b1a) + ''.join(map(str,side1a)) + '+' + str(b1b) + ''.join(map(str,side1b)) + '=' + str(b2a) + ''.join(map(str,s2a)) + '+' + str(b2b) + ''.join(map(str,s2b)))

def findmass(side1):
    #find list in elements containing the element to find mass
    #print(side1)

    if len(side1) == 3:
        for i in elements:
            if i[0].upper() == side1[1].upper():
                
                a = i[4]
                b = 0
                c = 0
                a *= side1[2] * side1[0]
                
    elif len(side1) == 5:
        for i in elements:
            if i[0].upper() == side1[1].upper():
                
                a = i[4]
            if i[0].upper() == side1[3].upper():
                b = i[4]
        c = 0

        a *= side1[2] * side1[0]
            
        b *= side1[4] * side1[0]
        
    elif len(side1) == 7:
        for i in elements:
            if i[0].upper() == side1[1].upper():
                a = i[4]
            if i[0].upper() == side1[3].upper():
                b = i[4]
            if i[0].upper() == side1[5].upper():
                c = i[4]
        a *= side1[2] * side1[0]
            
        b *= side1[4] * side1[0]
            
        c *= side1[6] * side1[0]
    
            
    else:
        print('sorry I didn\'t understand that, make sure it\'s balanced')

    answer = a+b+c
    #print(f'{answer: .3e}')
    return(answer)

#put a result into scientific notation


#e1 is [how many grams, moles or molecules, type of measurement]   
def conversiona(e1a,e1b,e2a,e2b):
    
    #if the first unit is in grams, then divide grams by the grams to moles ratio
    if e1a[-1].upper() == 'G':
        e1c = float(findmass(e1b))
        print('\n\n(' + str(e1a[0]) + ')' + '\n---\n(' + str(e1c) + ')\n*')
        e1c = float(e1a[0]) / float(e1c)
    #if the first unit is in molecules, then divide molecules by 6.022 E23
    elif e1a[-1].upper() == 'MO':
        e1c = 6.022 * 10**23
        print('\n\n(' + str(e1a[0]) + ')' + '\n---\n(' + str(e1c))
        e1c = e1a[0] / e1c
    #if the first unit is in mole, then print the molecules divided by 1
    elif e1a[-1].upper() == 'M':
        e1c = 1
        print('\n\n(' + str(e1a[0]) + ')' + '\n---\n(' + str(e1c))
        e1c = e1a[0] / e1c
    
    #If the second unit is moles, then multiply by the mole to mole ratio
    if e2a[-1].upper() == 'M':
        print('(' + str(e1b[0]) + ')' + '\n---\n(' + str(e2b[0]) + ')\n')
        e1d = e1b[0] / e2b[0]
        e1c *= float(e1d)
    
    #if the second unit is in grams, then multiply by the moles to moles ration then multiply moles by the moles to grams ratio
    elif e2a[-1].upper() == 'G':
        print('(' + str(e1b[0]) + ')' + '\n---\n(' + str(e2b[0]) + ')\n*' + str(findmass(e2b)))
        e1d = e1b[0] / e2b[0]
        e1c *= float(e1d)
        e1c *= float(findmass(e2b))

    #if the second unit is in molecules, then multiply by the moles to moles ration then multiply moles by 6.022 E 23
    elif e2a[-1].upper() == 'MO':
        print('(' + str(e1b[0]) + ')' + '\n---\n(' + str(e2b[0])+')\n*\n6.022 E23')
        e1d = e1b[0] / e2b[0]
        e1c *= e1d
        e1c *= 10**23 * 6.022

    print(e1c)

    

        
    


#this is in a while loop so that you don't have to keep rerunning everytime you want to balance something new
while True:
    typea = int(float(input('If you want to find mass, type 1 (you will need a balanced equation).\nIf you want your equation balanced, type 2  \nif you want to convert, then type 3 \nthen hit enter\n')))

    if typea == 1:

        side1 = input('Type a balanced element or bond. \nBalanced meaning if this is part of an equation, then type the  balncing number, otherwise type 1 \nIf 1 element is a polyatomic ion like (NO3)2, then type it as N2O6. \nIf the balancing number is 1, make sure to still type 1\n then hit enter\n')

        side1 = list(side1)

        blanklist = [int(side1[0])]
        side1.pop(0)
        x = ''
        
        #separate numbers from elements
        for i in side1:
            if i.isnumeric() == True:
                y=int(i)
                blanklist.append(x)
                blanklist.append(y)
                x = ''
            else:
                    
                x += i

            

        side1 = blanklist


        print(findmass(side1))
    if typea == 2:
        #get the equation
        equation = input(' \n type the equation you want to balance \n if there is a plus sign only on one side then make sure to put it on the first side. \n Also make sure to put a number in front of every element even if it is 1.\n if it is a combustion reaction, make sure that it is in this format: C*H* + O2 = C1O2 + H2O1\n if you are dealing with polyatomic ions for example SO4 put it as SO1 and if you have for example S2O8, that would be SO2 \n then hit enter\n')
        #define variables to use when splitting and organizing the equation

        #turn equation into list
        equation = list(equation)
        #this will be changed in a for loop and represents the position in the equation
        pos = 0
        #this will be added to in a for loop. it is a list of positions in the equation with a plus sign. this will be used to split the equation into lists
        pluspos = []
        #these are the spots where the equation will be split
        splitspots = []
        #these are all the lists that the equation will be split into
        side1=[]
        side1a=[]
        side1b=[]
        side2=[]
        side2a=[]
        side2b=[]
        blanklist = []

        #x will be what is used to put together 2 parts of an element with no number between. 
        #This way if you have something like pb1 the list won't be ['p','b',1], it will be ['pb',1]
        x=''
        equalpos = 0
        #locate the plus and equal sign to split the list later
        for i in equation:
            if i.isnumeric() == True:
                splitspots.append(pos)
            if i == '+':
                pluspos.append(pos)
            if i == '=':
                equalpos = pos
            pos += 1

        #separate eqaution by equals sign into sides 1 and 2
        if equalpos != 0:
            for i in range(equalpos):
                side1.append(equation[i])

            for i in range(equalpos+1,len(equation)):
                side2.append(equation[i])
            #seaparate first side of equation by plus sign
            for i in range(pluspos[0]):
                side1a.append(side1[i])

            for i in range(pluspos[0]+1,len(side1)):
                side1b.append(side1[i])
            #separate numbers from elements
            for i in side1a:
                if i.isnumeric() == True:
                    y=int(i)
                    
                    blanklist.append(y)
                    
                else:
                    
                    x += i
            blanklist.append(x)
            side1a = blanklist
            blanklist = []

            x=''
            #separate numbers from elements
            for i in side1b:
                if i.isnumeric() == True:
                    y=int(i)
                    
                    blanklist.append(y)
                    
                else:
                    x+=i
                blanklist.append(x)

            side1b = blanklist
            blanklist = []

            side1 = [side1a,side1b]

                

            side1.clear()
            side1.append(side1a)
            side1.append(side1b)


            #makes separate lists on each side of the plus sign on side 2 if there is one
            if len(pluspos) == 2:
                pluspos2 = pluspos[1] - len(equation)
                pluspos2 += len(side2)
                #first side of plus sign
                for i in range(pluspos2):
                    side2a.append(side2[i])
                    
                    print(pluspos2)
                #second side of plus sign
                for i in range(pluspos2 +1,len(side2)):
                    side2b.append(side2[i])
                    
                side2.clear()
                side2.append(side2a)
                side2.append(side2b)
                #separate numbers from elements to organize them in a way in which the computer can interperet them
                for i in side2a:
                    if i.isnumeric() == True:
                        y=int(i)
                        blanklist.append(x)
                        blanklist.append(y)
                        x = ''
                    else:
                        x+=i

                side2a = blanklist
                blanklist = []
                x=''
                #separate numbers from elements to organize them in a way in which the computer can interperet them
                for i in side2b:
                    if i.isnumeric() == True:
                        y=int(i)
                        blanklist.append(x)
                        blanklist.append(y)
                        x = ''
                    else:
                        x+=i

                side2b = blanklist
                blanklist = []

                side2 = [side2a,side2b]

            else:
                #this would be in a case with no plus sign on side 2 like a combination reaction.
                #in that case there is no need to split side2
                for i in side2:
                    if i.isnumeric() == True:
                        y=int(i)
                        blanklist.append(x)
                        blanklist.append(y)
                        x = ''
                    if i.isnumeric() == False:
                        x+=i

                side2 = blanklist
                blanklist = []
            #print(side1)
            #print(side2)
        else:
            for i in range(len(equation)):
                side1.append(equation[i])
            for i in range(pluspos[0]):
                side1a.append(side1[i])

            for i in range(pluspos[0]+1,len(side1)):
                side1b.append(side1[i])
            #separate numbers from elements
            for i in side1a:
                if i.isnumeric() == True:
                    y=int(i)
                    blanklist.append(x)
                    blanklist.append(y)
                    x = ''
                else:
                    
                    x += i

            side1a = blanklist
            blanklist = []

            x=''
            #separate numbers from elements
            for i in side1b:
                if i.isnumeric() == True:
                    y=int(i)
                    blanklist.append(x)
                    blanklist.append(y)
                    x = ''
                else:
                    x+=i

            side1b = blanklist
            blanklist = []

            side1 = [side1a,side1b]

                

            side1.clear()
            side1.append(side1a)
            side1.append(side1b)
            
        #this decides what type of equation it is, and balances it accordingly
        if len(side1a) > 2 or len(side1b) >2:

            if equalpos == 0:
                finishsinglereplace(side1a,side1b)
                print('I am finishing and balancing your single replacement reaction')
                #balancesinglereplace(side1a,side1b,side2a2,side2b2)
            
            if len(side1a) > 2 and len(side1b) >2: 
                balancedoublereplace(side1a,side1b,side2a,side2b)
                print('this is a double replacement reation')
            elif len(side2a) > 2 and len(side2b) > 2:
                balancecombustion(side1a,side1b,side2a,side2b)
                print('this is a combustion reaction')
            
            else:
                balancesinglereplace(side1a,side1b,side2a,side2b)
                print('this is a single replacement reaction')
        elif len(side1a) == 2 and len(side1b) == 2:
            balancecombo(side1a,side1b,side2)
            print('this is a combination reaction')
        else:
            #if none of these are true then it the user made an error in typing the equation
            print('sorry I didn\'t understand that, make sure that you follow all of the directions especially if it is a combustion reaction')

    if typea == 3:
        conversion = input('type the amout of the element that you want to convert and then the unit. \nFor grams the unit is g, for mole it\'s m, and for molecule it\'s mo \n then type * followed by the balanced side1 (balanced meaning how it shows up in the equation)\n then type = and repeat what you did for the first element except instead of giving a value with the unit just give the unit\nthen hit enter\n')
        conversion = list(conversion)
        #this will be changed in a for loop and represents the position in the equation
        pos = 0
        #this will be added to in a for loop. it is a list of positions in the equation with a plus sign. this will be used to split the equation into lists
        pluspos = []
        #these are the spots where the equation will be split
        splitspots = []
        #these are all the lists that the equation will be split into
        side1=[]
        side1a=[]
        side1b=[]
        side2=[]
        side2a=[]
        side2b=[]
        blanklist = []

        #x will be what is used to put together 2 parts of an element with no number between. 
        #This way if you have something like pb1 the list won't be ['p','b',1], it will be ['pb',1]
        x=''
        equalpos = 0
        #locate the plus and equal sign to split the list later
        for i in conversion:
            if i.isnumeric() == True:
                splitspots.append(pos)
            if i == '*':
                pluspos.append(pos)
            if i == '=':
                equalpos = pos
            pos += 1

        #separate eqaution by equals sign into sides 1 and 2
        if equalpos != 0:
            for i in range(equalpos):
                side1.append(conversion[i])

            for i in range(equalpos+1,len(conversion)):
                side2.append(conversion[i])
            #seaparate first side of equation by * sign
            for i in range(pluspos[0]):
                side1a.append(side1[i])

            for i in range(pluspos[0]+1,len(side1)):
                side1b.append(side1[i])
            #separate numbers from elements
            for i in side1a:
                if i.isnumeric() == True:
                    y=int(i)
                    
                    blanklist.append(y)
                    x = ''
                else:
                    
                    x += i
            blanklist.append(x)
            side1a = blanklist
            blanklist = []

            x=''
            #separate numbers from elements
            for i in side1b:
                if i.isnumeric() == True:
                    y=int(i)
                    if x != '':
                        blanklist.append(x)
                    blanklist.append(y)
                    x = ''
                    
                else:
                    x+=i
            

            side1b = blanklist
            blanklist = []

            side1 = [side1a,side1b]

                

            side1.clear()
            side1.append(side1a)
            side1.append(side1b)
            print(side1)

            if side2[1] == '*':
                side2a = [side2[0]]
                side2.pop(0)
                side2.pop(0)
                side2b = side2
            else:
                side2a = [side2[0] + side2[1]]
                side2.pop(0)
                side2.pop(0)
                side2.pop(0)
                side2b = side2

            for i in side2b:
                if i.isnumeric() == True:
                    y=int(i)
                    if x != '':
                        blanklist.append(x)
                    blanklist.append(y)
                    x = ''
                    
                else:
                    x+=i
            

            side2b = blanklist
            blanklist = []


            #print(side1)
            #print(side2)
        
        conversiona(side1a,side1b,side2a,side2b)
       