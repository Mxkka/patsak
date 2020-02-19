f = open("keimeno.txt", "r")
word_list=[word for line in f for word in line.split()]
                   #χωριζει τις λεξεις ως στοιχεια μιας λιστας             



word_list.sort(key=len) #ταξινομει τις λεξεις με βαση το μεγεθος τους
#print(word_list)


b=word_list[-5:]        #δημιουργει λιστα με τις 5 τελευταιες που θα ειναι και οι πιο μεγαλες

print (b)

        


f="aeiouAEIOU"



                    #αφαιρει τα φωνηεντα των 5 μεγαλυτερων λεξεων

for x in range(0,len(b)):
    string=b[x]
    b2=""
    for c in range (0,len(string)):
        if string[c] not in f:
            b2+=string[c]
    print (b2)
            
