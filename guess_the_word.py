words=['Airplane','Ears','Piano','Bat','Elephant','Sunflower','Archer','Fish','Ghost',
       'Shoelaces','Stamp','Baseball','Football','Balloon','Basketball','Singer','Skateboard',
       'Matrimony','Snail']
hints={'Airplane':"Although I’m not a bird\n I have wings so I can fly\n I can help you travel\n By jetting off through the sky",
      'Ears':"Part of human body, and helps in maintaining balance",
      'Piano':"It has 88 keys,but none of these will open a door",
      'Bat':"I’m black but I’m not a marker pen\n I’m a mammal but I’m not a whale\n I can fly but I’m not a plane\n I go before ‘man’ to make a superhero but I’m not a spider\n I might be found in a cave but I’m not a stalagmite",
      'Elephant':"I’m gray but I’m not a cloud\nI have a tail but I’m not a cat\nI have big ears but I’m not a bunny\nI’m tall but I don’t play basketball\nI’m jumbo but I’m not a jet\nI have a trunk but I’m not a car",
      'Sunflower':"I’m yellow but I’m not a banana\nI can be over ten feet tall but I’m not a giraffe\nI have seeds but I’m not a lemon\nI can provide oil but I’m not canola\nI’m a plant but I’m not a rose",
      'Archer':"whos is farsighted,\nand has a true shot,\nand who rarely tires?",
      'Fish':"I am alive without breath and cold as death. I am never thirsty but always drinking. What am I?",
      'Ghost':"You're in a room and there is a ghost in the room, but you're the only one in the room. Who am I?",
      'Shoelaces':"I get sold in a box but I’m not breakfast cereal\nI come as a pair but I’m not glasses\nI can be shined but I’m not a flashlight\nI have a tongue but I can’t speak\nI’m worn on your feet but I’m not socks",
      'Stamp':"I have no wallet, but I pay my way. I travel the world, but in the corner I stay. I am a? ",
      'Baseball':"Name the only sport in which the ball is always in possession of the team on defense, and the offensive team can score without touching the ball?",
      'Football':"In this game\nYou will not frown\nIf you score\nA great touchdown",
      'Balloon':"I get blown up but I’m not a stick of dynamite\nI sometimes have a string attached but I’m not a kite\nI sometimes float but I’m not a swimmer\nI’m seen at birthday parties but I’m not a candle",
      'Basketball':"James Naismith, a teacher at a YMCA in Springfield, Massachusetts, is credited with inventing _______________ in 1891.",
      'Singer':"No Hint",
      'Skateboard':"You ride on me, I don't have windows, doors, engine, paddles. I'm a board but you cant'write on me.",
      'Matrimony':"My first is often at the front door.\nMy second is found in the cereal family.\nMy third is what most people want.\nMy whole is one of the United States.",
      'Snail':"If a man carried my burden he would break his back.\nI am not big but leave silver in my tracks.\nWhat am I?",
      }

name=input("Enter your name : ")
fhand=open("Score_Card.txt","a")
print("-Game Rules-\n------------")
print("1) You will be given an incomplete word, you have to complete it.")
print("2) If the correct answer is 'Divyansh' and you type 'divyansh' it will be considered wrong, i.e., first alphabet must be capital.")
print("3) Points will be deducted according to no of failed attempts")
print("4) Require a HINT not a problem just type HINT")
print("5) Want to know the answer just type ANSWER")
print("6) Want to quit not a problem just type QUIT")
import random
import time
tot_score=0
len_words = len(words)
time.sleep(10)
tot_penalties=0
while True:
  selected_word_index=random.randint(0,len_words-1)
  selected_word=words[selected_word_index]
  upper_limit=int(len(selected_word)/2)+(len(selected_word)%3)+(len(selected_word)%5)+(len(selected_word)%4)
  Blank_space_number=random.randint(1,upper_limit)
  Blank_pos=list()
  score=len(selected_word)
  out_screen=""
  penalty=0
  flag2=0
  for i in range(0,Blank_space_number):
    flag1=random.randint(0,len(selected_word))
    if flag1 not in Blank_pos:
      Blank_pos.append(flag1)
    else:
      i-=1
  for i in range(0,len(selected_word)):
    if i not in Blank_pos:
      out_screen=out_screen+selected_word[i]
    else:
      out_screen=out_screen+" _ "
  print(out_screen)
  print("Type your answer please : ")
  input_answer = input()
  while True:
    if input_answer=="QUIT":
        flag2 = 1
        print("Correct Answer was : "+selected_word)
        print("Your total score is : " + str(tot_score))
        write="\n"+name+"\t\t"+str(tot_penalties)+"\t\t"+str(tot_score)
        fhand.write(write)
        break
    elif input_answer == "ANSWER":
        print("Correct Answer was : " + selected_word)
        break
    elif input_answer=="HINT":
      print("HINT is : ")
      print("\n"+hints[selected_word]+"\n")
      print("Type your answer please : ")
      input_answer = input()
    elif input_answer==selected_word:
      print("\nCorrect Answer\n")
      tot_score+=(score-penalty)
      break
    else:
      print("Wrong Answer, try again : ")
      tot_penalties+=1
      if penalty>score:
        penalty=score
      else:
        penalty+=1
        print("Type your answer please : ")
        input_answer = input()
  if flag2==1:
      break
fhand.close()