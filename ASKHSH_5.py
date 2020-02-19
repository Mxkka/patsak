f= open("keimeno.txt", "r")
                #βαζει σε μια λιστα ολες τις λεξεις του κειμενου
lista=[word for line in f for word in line.split()]

                #βαζει το πρωτο γραμμα στο τελος και
                #προσθετει ay σε οσες λεξεις ειναι μεγαλυτερες απο 3 γραματα
for x in (lista):
    if len(x)>3:
        print(x[1:] + x[0] + "ay")
    else:
        print (x)
    
f.close()
