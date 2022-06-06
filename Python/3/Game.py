vidas=5
i=5

print('Rescate a la princesa de la torre')
print('Click ENTER to start the game')

input()

print('elige el nombre de tu principe: ')
name=input()
print('Una princesa es capturada por una bruja malvada y es encerrada en lo alto de un castillo.El principe',name,'decide ir a salvarla porque es su amor verdadero.')

input()

print('El principe debera de tomar peligrosas y arriesgadas decisiones que arriesgaran su vida para poder llegar a salvo a la cima del castillo y poder salvar a la princesa')

input()

print('el primer desafio sera...')
print('3..')
input()
print('2...')
input()
print('1...')
input()

print('all the game will be in English')
print('so lets start the game')

input()

print('First..')
input()
print('You are going to start the game with 5 lifes ')
print('but...')
input()
print('you will lose them if you think in a dumb way')
input()
print('START')
input()

print('choose another character name:')
elf=input()
print('hello, my name is ',elf,'i take care of the castle ')
input()

print('you are here to safe the princess right??')
print('HAHAHA you are not te first to try it')
print('to enter to the castle you need a   passcode')
print('the pascode will be the answer of this riddle')
input()

print('What has to be broken before you can use it?')


while True:
  answer=input("here goes your answer: ")
  if answer=='egg':
    print('thats the correct answer,                  welcome   to the castle')
    break 
  elif (answer!="egg"):
    print('thats incorrect, try again')
    i=i-1
    print("you have ",i, "tries")
    
    
    if(i==0):
      print("you have lost one life")
      vidas=vidas-1
      break

print(elf,':you may continue with your rescue')

input()

print('In the castle there are 2 roads to choice, you must decide the right one and in that way you wont loose a life')
print('Theres no difference between the beginning of the road, is in your hands what to choose')

puerta=input("u must choose a/b:")

if (puerta=="a"):
  print("good")
  vidas=vidas+1
  print('you win an extra life')

else:
  vidas=vidas-1
  print('OH YOU FELL, you loose a life')
  
print('you can continue with your mission')
print("follow the arrows that are on the floor")

print(elf, ':you have been walking for to long, you have to choose a sword⚔️ ')
print(elf,':you must enter to this room and fight with this ogre ')
print('click ENTER to start the chaellenge')
input()

vidaogre=3
while True:
   ataque=input('you can choose three attacks:poke eye (a), punch tummy(b), spank in the ass (c)')

   if ataque==('a'):
    print('the ogre cries')
   vidaogre=vidaogre-0.5
   print('ogre is losing lifes, continue      like that, ogres life:',vidaogre)

   if ataque==('b'):
    print('ogre throw ups ')
   vidaogre=vidaogre-0.5
   print('KEEP GOING, hes dying,ogres         life:',vidaogre)

   if ataque==('c'):
    print('ogre passed out')
    vidaogre=vidaogre-2
    print('it loose two lifes, ogres life: ', vidaogre)

   if (vidaogre<0):
       print("you win")
       break

print('congratulations, you finish withthe ogre')
input()

print('you may continue with your rescue')
input()

print('YOU LEAVE THE ROOM ')
input()

print(elf, 'Hi again, well done! you finish him')
input()

print(elf, 'you can continue exploring the castle until your next challenge  ')
input()

print('The prince',name, 'explores the castle and suddenly he stopped... ')
input()
print('he found a picture, when the princess was younger...')
input()
print('but there was something stange...')
input()
print('but he decided to continue with the rescue because he had to be fast to safe her ')
input()
print('the prince continue walking around the castle until he founds the elf')
print(elf,': hi again, you must be ready for the next challenge...so go to the North part of the castle')
print('you will find something there, see you later')
input()

print('THE PRINCE CONTINUE WALKING TO THE NORTH OF THE CASTLE')
print('choose another character name: ')

bad=input()

print('Hi, im',bad, 'and i want you to introduce you my family ')
input()

print('the prince follows', bad, 'till a little hut')
input()

print('the family was not big, it was two parents and two kids... and they were all dwarfs')
input()
print('they all introduced temselves')
input()
print(bad,'ohhh they are coming ')
print ('THE PRINCE WAS CONFUSED OF WHO WERE COMING UNTIL HE HEAR A SOUND...')
input()
print('HE LOOKS BACK AND HE SAW A LOT OF DWARFS BUTTT')
input()
print('they were all different, unusual, they all were ugly and they had paint ball weapons')
print(elf,'came driving a barbie pink car and he said...')
input()
print('ohhh your next challenge is here, click ENTER to star the count down to start the challenge')
input()

print('3')
input()

print('2')
input()

print('1')
input()

print('READY GO')


vidadwarfs=3
while True:
   battle=input('you can choose three tools :shield (a), invisible cape(b), bomb(c)')

   if battle==('a'):
    print('the paint balls bounce the shield and hit the dwarfs back')
   vidadwarfs=vidadwarfs -1
   print('dwarfs are losing a life, continue like that, dwarfs life:',vidadwarfs)

   if ataque==('b'):
    print('dwarfs cant see the prince anymore ')
   vidadwarfs=vidadwarfs-1
   print('KEEP GOING, prince is winning dwarfs life:',vidadwarfs)

   if ataque==('c'):
    print('dwarfs explote')
    vidadwarfs=vidadwarfs-1
    print('Well done, dwarfs life: ', vidadwarfs)


   if (vidadwarfs<0):
       print("you win")
       break

print('The prince start walking around the castle again and he found...')
input()
print('the same picture appear in the hallway of the castle but it was a different place than before')
input()

print ('he ignore the picture again, but he was thinking about it')
input()

print ('he continued with his journey to rescue the beatiful princess')
input()

print('in a desk he founded something...')
input()

print('it was a map')
input()

print('and sudenly',elf, 'appear')
input()

print(elf, ':hi again!! are you ready?')
input()

print('prince: ready for what?')
input()

print(elf,':for your next challenge!')
input()

print('prince: but i just fnished one, im tired')
input()

print(elf,':fine you can rest in the bedroom')
input()

print('prince: where is it?')
input()

print(elf,'you must find it')
input()

print('THE PRINCE FOUNDED THE BEDROOM')
input()

bed=input("you must click a to go to sleep and b to wake up")



if (bed=="a"):
  print("now you are sleeping ZZzzzzzz")
  print('good night 😴')

if (bed=="b"):
  print('good morningg you wake up')
  print(elf,"good morning you must go to     explore the castle again and find a new    mission")



print('RiSe AnD sHiNeeeee')
input()

print('its a new day and new challenges that u must complete')
input()

print('ELF APPEARS')
input()
print(elf,':hiii, now you are ready?')
input()

print('prince mind💭: i was thinking about giving up...')
input()

print('i cant...why?...')
input()

print('because she is my true love')
#eww cringe
input()

print('prince: yes, im ready')
print(elf,'alright, you will need to explore the castle again')
input()

print('PRINCE START EXPLORING THE CASTLE, AND WAITING FOR HIS NEXT CHALLENGE')
input()

print('AT THIS POINT HE WAS SO MUCH CLOSER TO THE PRINCESS')
input()

print('but...')
input()

print('the challenges will be different...')
input()

print('it will be MORE DIFFICULT ')
input()


print('click ENTER to star the challenge ')
input()

print('prince: where i am?')
input()

print('you are at the magic room!')
input()

print('prince: mmm ok but who are you?')
input()

print('SELECT ANOTHER CHARACTER NAME:')
wiz=input ()

print('im the wizard ', wiz, 'and im going to tell you your next challenge ')
input()

print(wiz, ': okay, you have a bowl of polvorix infront of you, that will be your main ingredient')
input()

print(' and then on the other side you have 2 small jars, that have liquids that looks like they are the same but...')
input()

print('they are completely different, one is unicorn slobber')
input()

print('and the other is elf pee')
input()

print('you must choose wich one to mix with the polvorix but here is the challenge...')
input()

print('one of them will make an explosion and you will loose a life')
input()

print('prince💭: OMG I FORGOT ABOUT THE LIFES')
input()

print('prince: and how im supposed to know?')
input()

print(wiz, 'mm thats not my problem ')
input()

print('CLICK ENTER TO START THIS CHALLENGE ')
input()


while True:
   mix=input('if you want to use the  unicorn slubber click (s) and if you want to use elf pee click (p)')

   if (ataque=='s'):
    print('it occured a rainbow mix!!')
     
    print('you rae not losing lifes,           congrats')
    print('you have ', vidas, 'lifes')

   if ataque==('p'):
    
     print('EXPLOSION!!! ')
     print('OHHH NOOO')
     print('you lost a life')
     print('u have',vidas, 'lifes')
     break

print(wiz,':you are done here, you can leave ')    
input()

print('THE PRINCE KEPT EXPLORING THE CASTLE AND HE FIGURED IT OUT...')
input()

print('THAT HE WAS REALLY CLOSE TO THE PRINCESS')
input()

print(elf,': why are you so happy?')
input()

print('prince: because ill meet my true love')
input()

print(elf, 'im not gonna lie to you, you are doing a great job and yes...')
input()

print(elf,'you are really close')
input()

print(elf, 'you have one last challenge...')
input()

print('prince: tell me!!!')
input()

print('you must have to fight over me')
input()

print('what!!')
input()
print('yes, and you must start right now if you want to meet your princess')
input()
print('CLICK ENTERT TO START')
input()


while True:
   sad=input('you can choose three tools : sward (a), knife (b), poison(c)')

   if sad==('a'):
    print('you kill him with the sward')
    print(elf,'before i die, i need  to    tell you something that you must know')
    input()
    print('the picture... the woman that is her mom... locked her in the room...  she is the villain')

     
   if sad==('b'):
    print('you kill him with the knife')
    print(elf,'before i die, i need  to    tell you something that you must know')
    input()
    print('the picture... the woman that is her mom... locked her in the room...  she is the villain')


   if ataque==('c'):
    print('you kill him with a poison, so  it will be less harmful ')
    print(elf,'before i die, i need  to    tell you something that you must know')
    input()
    print('the picture... the woman that is her mom... locked her in the room...  she is the villain')
    break


print('prince: thanks for everything ',elf)
input()    
print('THE PRINCE WAS VERY SAD ABOUT THE ELF, BUT HE HAD TO SAVE HIS PRINCESS ')
input()
print('before the elfs last breath he openend his hand and gave the prince a key so he could save the princess ')
input()
print('the prince took the key and he ran to the princess room')
input()
print('he opened the door and he found her')
input()
print('princess: YOU ARE HERE, YOU SAFE ME!!')
input()
print('prince: i know we dont know each other yet, but i already love you')
print('princess:i love you too')

print('1 YEAR LATER')
print(' The prince and the princess got married and they had a kid, they named him...',elf)
print('end')