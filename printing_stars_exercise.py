###############################################################################
####################### ************************* #############################


def piramid(rows):
    
    for i in range(rows):
        
        print(" "*(rows-i)+"*"*(2*i-1))
        
#piramid(5)

print("")

def deltoid(rows):
    
    for i in range(rows):
        
        print(" "*(rows-i)+"*"*(2*i-1))
        
    for j in range(rows,0,-1):
        
        print(" "*(rows-j)+"*"*(2*j-1))
        
#deltoid(5)

print("")

def deltoid_opposite(rows):

    for i in range(rows,1,-1): # because 1 is not counted

        print(" "*(rows-i)+"*"*(2*i-1))

    for j in range(1,rows+1):

        print(" "*(rows-j)+"*"*(2*j-1))

#deltoid_opposite(5)

print("")


def half_piramid_from_left(rows):
    
    for i in range(1,rows):
        
        print("*"*i)

#half_piramid_from_left(5)

print("")

def half_piramid_fromTheEnd_from_left(rows):

    for i in range(rows,0,-1):

        print("*"*i)

#half_piramid_fromTheEnd_from_left(5)

print("")

def half_piramid_from_right(rows):

    for i in range(rows):

        print(" "*(5-i)+"*"*i)

#half_piramid_from_right(5)

print("")

def half_piramid_fromTheEnd_from_right(rows):

    for i in range(rows,0,-1):

        print(" "*(rows-i)+"*"*i)

#half_piramid_fromTheEnd_from_right(5)

print("")

def piramid_half(rows):

    for i in range(1,rows):

        print(" "*(rows-i)+"*"*i)

    for j in range(rows,0,-1):

        print(" "*(rows-j)+"*"*j) 

#piramid_half(5)

print("")

def half_piramid2(rows):

    for i  in range(rows):

        print("*"*i)

    for j in range(rows,0,-1):

        print("*"*j)

#half_piramid2(5)

print("")

def piramid_half_opposite(rows):

    for i in range(1,rows):

        print(" "*(rows-i)+"*"*i)

    for j in range(rows,0,-1):

        print(" "*(rows-1)+"*"*j) 

#piramid_half_opposite(5)

print("")

def empty_deltoid(rows):

    print(" "*rows+"*")

    for i in range(1,rows):

        print(" "*(rows-i)+"*"+" "*(2*i-1)+"*")

    for j in range(rows,0,-1):

        print(" "*(rows-j)+"*"+" "*(2*j-1)+"*")

    print(" "*rows+"*")

#empty_deltoid(5)

print("")

def mix(rows):

    print("*"*rows)
    i = (rows//2)-1
    j = 2

    while i != 0:

        while j <=(rows-2):

            print("*"*i,end="")
            print("_"*j,end="")
            print("*"*i,end="\n")
            i -= 1
            j += 2

#mix(14)



























