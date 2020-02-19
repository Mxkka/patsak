number=int(input("dwse noumero"))
sum= [int(x) for x in str(number)]
while len(sum)!=1:
    number=number*3+1    #τριπλασιαζει και προσθετει 1 στο νουμερο
    sum=[int(x) for x in str(number)]
    b=0
    for i in sum:
        b+=i       #προσθετει ολα του τα ψηφια μαζι
        number=b
    print (number)
    sum=[int(x) for x in str(b)]
print ("menei o monopshfios arithmos",sum)   #τυπωνει τον τελικο μονοψηφιο αριθμο

    
        
        
        
    
    
    
