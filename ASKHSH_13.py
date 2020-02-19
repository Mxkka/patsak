def athroisma(CardCode):
    mhkos=len(CardCode)
    monoi=0
    zygoi=0

    #συναρτηση που περναει απο καθε ζυγη και μονη θεση του κωδικα.σε καθε μονη θεση διπλασιαζει το ψηφιο και αθροιζει ολα τα ψηφια μεταξυ τους
    if (mhkos==0):
        return 0
    else:

        if (mhkos % 2 == 0):
            last=int(CardCode[-1])
            zygoi += last
            return zygoi + athroisma(CardCode[:-1])
        else:
            last = int(CardCode[-1])
            last = 2 *last
            pshfia = last // 10 + last%10
            monoi += pshfia
            return monoi + athroisma(CardCode[:-1])
        
   #συναρτηση που εκτελει τον αλγοριθμο του λουν , ελεγχει δηλαδη αν το αθροισμα ολων των ψηφιων διαιρειται ακριβως με το 10

def luhns_algorithm():
    CardCode = input('εισάγετε 16ψηφιο κωδικό κάρτας:')
    sum = athroisma(CardCode)

    if (sum % 10 ==0):
        print ('ορθός κωδικός')
    else:
        print('μη ορθός κωδικός')


def main():
    luhns_algorithm()

main()
