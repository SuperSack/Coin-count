bag_amount = 0

weight = ""

end=0

correct=0

incorrect=0

while end==0:
    loop=0
    A = input("Show bag count (c) or add bag (a).(e) end program:")
    if A=="e":
        end=1
    if A=="c" :
        print(bag_amount,"bags have been counted with",correct,"having the correct amount of coins and",incorrect,"having the incorrect amount of coins")
    if A == "a" :
        input("enter name:")
        
        while loop==0:
            loop=1
            B=input("enter coin type:")
            if B=="£2" :
                weight = 12
                bag_amount=bag_amount+1
            elif B=="£1" :
                weight = 8.75
                bag_amount=bag_amount+1
            elif B=="50p" :
                weight = 8
                bag_amount=bag_amount+1
            elif B=="20p" :
                weight = 5
                bag_amount=bag_amount+1
            elif B=="10p" :
                weight = 6.5
                bag_amount=bag_amount+1
            elif B=="5p" :
                weight = 2.35
                bag_amount=bag_amount+1
            elif B=="2p" :
                weight = 7.12
                bag_amount=bag_amount+1
            elif B=="1p" :
                weight = 3.56
                bag_amount=bag_amount+1
            else :
                print ("invalid coin type")
                loop=0
            

        
        weight_guessed=float(input("enter bag weight:"))
        if weight == weight_guessed :
                print ("The bag has the right amount of coins")
                correct=correct+1
        else :
                print ("The bag is supposed to weigh", weight,"g")
                incorrect=incorrect+1
