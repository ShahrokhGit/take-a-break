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

singers = ['Michael Jackson','Shakira', 'Rihanna']

print('From which one do you want to watch? \n1.Michael Jackson\n2.Shakira\n3.Rihnna')
while True:
    selected_singer = input()
    if selected_singer.isdigit() and 1 <= int(selected_singer) <= 3:
        break
    else:
        print('Please type a number between 1 and ',len(singers))
        pass

video = random.choice(list(michael_jackson.keys()))
print("Michael Jackson video: ",video, 'is playing, enjoy!')
# web.open(michael_jackson[video])
