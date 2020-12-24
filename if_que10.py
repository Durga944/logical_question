u1 = "rock"
u2 = "paper"
if u1==u2:
       print( "It's a tie!")
elif u1 == 'scissors':
    if u2 =="rock":
        print( "Rock wins!")
    else:
        print( "Paper wins!")
elif u1 == 'paper':
    if u2 == 'scissors':
        print( "Scissors win!")
    else:
        print( "Rock wins!")
elif u1 == 'rock':
    if u2 == 'paper':
        print ("Paper wins!")
    else:
        print ("Scissors win!")
else:
    print ("Invalid input! You have not entered rock, paper or scissors, try again.")