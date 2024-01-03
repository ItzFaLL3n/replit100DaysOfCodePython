from getpass import getpass as input

print("E P I C    🪨  📄 ✂️    B A T T L E ")
print()
print("Select your move (R, P or S)")
print()

player1_score = 0
player2_score = 0

while True:
  player1move = input("Player 1 >")
  player2move = input("Player 2 >")

  if player1move == "R":
    if player2move == "R":
      print("Tie, You both picked Rock")
    elif player2move == "S":
      print("Player1 smashed Player2's Scissors into dust with their Rock!")
      player1_score +=1
    elif player2move == "P" :
      print("Player1's Rock is smothered by Player2's Paper!")
      player2_score +=1
    else:
      print("Player2 threw an invalid move!")
  elif player1move == "P":
    if player2move == "P":
      print("Two bits of paper flap at each other. Dissapointing. Draw.")
    elif player2move == "R":
      print("Player2's Rock is smothered by Player1's Paper!")
      player1_score +=1
    elif player2move == "S":
      print("Player1's Paper is cut into tiny pieces by Player2's Scissors")
      player2_score +=1
    else:
      print("Player2 threw an invalid move!")
  elif player1move == "S":
    if player2move == "S":
      print("Tie, you both picked Scissors")
    elif player2move == "P":
      print("Player2's Paper is cut by Player1's Scissors")
      player1_score +=1
    elif player2move == "R":
      print("Player1's Scissors are smashed by Player2's Rock")
      player2_score +=1
    else:
      print("Player2 threw an invalid move!")
  else:
    print("Player1 threw an invalid move!")

  print("Player 1 has", player1_score, "wins.")
  print("Player 2 has", player2_score, "wins.")

  if player1_score == 3 or player2_score == 3:
    if player1_score == 3:
      print("Player 1 wins!")
    elif player2_score == 3:
      print("Player 2 wins!")
    print("Thanks for playing!")
    exit()
  else:
   continue
  

