import webbrowser as web
import random
import sys

print('The code is running under python version: ', sys.version)
# Database for Michael Jackson
michael_jackson = {'You are not alone':"https://www.youtube.com/watch?v=pAyKJAtDNCw",
 'Remember the time':"https://www.youtube.com/watch?v=LeiFF0gvqcc",
 'Billie jEan':"https://www.youtube.com/watch?v=Zi_XLOBDo_Y",
 'liberian girl':"https://www.youtube.com/watch?v=f3V-7DEAgdc",
 'the way you make me feel':"https://www.youtube.com/watch?v=HzZ_urpj4As&list=PLYagrqIg-kgTNL4-c4N6-zeURIPqVkrdK&index=7",
 "they don't care about us":"https://www.youtube.com/watch?v=QNJL6nfu__Q&list=PLYagrqIg-kgTNL4-c4N6-zeURIPqVkrdK&index=3",
 'dangerous':"https://www.youtube.com/watch?v=jr9uliNQwNA"}

shakira = {"hips don't lie":"https://www.youtube.com/watch?v=DUT5rEU6pqM",
'waka waka':"https://www.youtube.com/watch?v=pRpeEdMmmQ0",
'loca':"https://www.youtube.com/watch?v=XAhTt60W7qo",
'la tortura':'https://www.youtube.com/watch?v=Dsp_8Lm1eSk',
'gypsy':"https://www.youtube.com/watch?v=_3-GiVIE8gc",
'try everything':'https://www.youtube.com/watch?v=c6rP-YP4c5I',
'perro fiel':"https://www.youtube.com/watch?v=SHq2qrFUlGY",
'me enamore':"https://www.youtube.com/watch?v=sPTn0QEhxds",
"can't remember to forget you":"https://www.youtube.com/watch?v=o3mP3mJDL2k",
'la la la':"https://www.youtube.com/watch?v=7-7knsP2n5w",
'la bicicleta':"https://www.youtube.com/watch?v=-UV0QGLmYys",
'chantaje':"https://www.youtube.com/watch?v=6Mgqbai3fKo",
'Rabiosa':"https://www.youtube.com/watch?v=a5irTX82olg"}

riahanna = {'wild thoughts':'https://www.youtube.com/watch?v=fyaI4-5849w',
'Only girl (in the world)':"https://www.youtube.com/watch?v=pa14VNsdSYM",
'stay (feat Mikky Ekko)':"https://www.youtube.com/watch?v=JF8BRvqGCNs",
"what's my name? (feat Drake)":"https://www.youtube.com/watch?v=U0CGsw6h60k",
"Work (Explicit) feat Drake":'https://www.youtube.com/watch?v=m2hI1_UBN2c',
'diamonds':"https://www.youtube.com/watch?v=lWA2pjMjpBs"}

britney_spears = {'circus':"https://www.youtube.com/watch?v=lVhJ_A8XUgc",
'pretty girls':"https://www.youtube.com/watch?v=uV2uebhnqOw",
'till the world ends':"https://www.youtube.com/watch?v=qzU9OrZlKb8",
'oops I did it again':"https://www.youtube.com/watch?v=CduA0TULnow",
'womanizer':'https://www.youtube.com/watch?v=rMqayQ-U74s',
'I wanna go':"https://www.youtube.com/watch?v=T-sxSd1uwoU",
'work bitch':"https://www.youtube.com/watch?v=pt8VYOfr8To",
'Toxic':'https://www.youtube.com/watch?v=LOZuxwVk7TU',
'baby one more time':'https://www.youtube.com/watch?v=C-u5WLJ9Yk4',
'scream and shout':'https://www.youtube.com/watch?v=kYtGl1dX5qI'}

enrique_iglesias = {'hero':'https://www.youtube.com/watch?v=koJlIGDImiU',
'no me digas que no':'https://www.youtube.com/watch?v=zyqt2avPkoA',
'duelle el corazon':'https://www.youtube.com/watch?v=xFutjZEBTXs',
'loco':'https://www.youtube.com/watch?v=RSyUWjftHrs',
'coando me enamoro':'https://www.youtube.com/watch?v=4DO8GsIYfhQ',
'el perdedor':'https://www.youtube.com/watch?v=tLcfAnN2QgY',
'I like how it feels':'https://www.youtube.com/watch?v=klk8QPcfFYQ',
"I'm a freak":'https://www.youtube.com/watch?v=YUiVIPgJA0o',
'Not in love':'https://www.youtube.com/watch?v=njKo3l0MKQ0',
'Love to see you cry':'https://www.youtube.com/watch?v=LWdwkdYPz-o',
'heartbeat':'https://www.youtube.com/watch?v=NVk4vENObiI',
'Addicted':'https://www.youtube.com/watch?v=2M-2BFS6Jxc',
'Rythm divine':'https://www.youtube.com/watch?v=UZrzOZaI7UE'}

singers = ('Michael Jackson','Shakira', 'Rihanna', 'Britney', 'Enrique')

print('From which one do you want to watch? \n1.Michael Jackson\n2.Shakira\n3.Rihnna\n4.Britney\n5.Enrique')
while True:
    selected_singer = input()
    if selected_singer.isdigit() and 1 <= int(selected_singer) <= len(singers):
        break
    else:
        print('Please type a number between 1 and ',len(singers))
        pass

print("How often do you want me to play music video? (Please type in min)")

while True:
    wait_time = input()
    if wait_time.isdigit():
        break
    else:
        print('Oops!, type a digit.')


video = random.choice(list(michael_jackson.keys()))
print("Michael Jackson video: ",video, 'is playing, enjoy!')
# web.open(michael_jackson[video])
