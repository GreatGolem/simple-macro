import json,time,win32api,win32con
import capture_scr as scr
from PIL import Image,ImageGrab
import new_queue
#with open('data.json','rb') as f:
#    data = json.load(f)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    print 'click' + str((x,y))

def compare(a,b):
    if(a[0]!=b[0]):
        return False
    elif(a[1]!=b[1]):
        return False
    elif(a[2]!=b[2]):
        return False
    return True

def dungeonVictory(data):
    click(data['victory'][2][0],data['victory'][2][1])      #victory summary
    time.sleep(2)
    click(data['victory'][2][0],data['victory'][2][1])      #chest
    time.sleep(2)
    runeImg = ImageGrab.grab()
    timestr = time.strftime("%Y%m%d-%H%M%S")
    runeImg.save("drop_records/" + timestr +".png","PNG")
    x = data['victory'][3][0]
    y = data['victory'][3][1]
    screen = ImageGrab.grab()
    if(compare(screen.getpixel((x,y)),data['victory'][3][2])):          #checking rune
        x = data['victory'][6][0]
        y = data['victory'][6][1]
        if compare(screen.getpixel((x,y)),data['victory'][6][2]):       #checking 5 star rune
            print '5/6 star rune got'
            click(data['victory'][3][0],data['victory'][3][1])          #click get
        else:
            print '4 star rune got'
            click(data['victory'][7][0],data['victory'][7][1])          #click sell
            print 'selling the rune'
            time.sleep(2)
    else:
        print 'non-rune drop got'
        click(data['victory'][5][0],data['victory'][5][1])

def dungeonDefeated(data):
    click(data['defeated'][2][0],data['defeated'][2][1])
    time.sleep(2)
    click(data['defeated'][2][0],data['defeated'][2][1])

def recharge(data):
    for point in data['buyEnergy']:
        if(compare(scr.pixel_color(point[0],point[1]),point[2])):
            click(point[0],point[1])
            time.sleep(2)
    click(data['victory'][4][0],data['victory'][4][1])  #replay
    time.sleep(1)

def dungeon(t):
    with open('dragon.json','rb') as f:
        data = json.load(f)
    click(data['start'][0],data['start'][1])
    notEnd = True
    print 'wait for ' + str(t) + ' min.'
    time.sleep(60 * t)
    while(notEnd):
        time.sleep(5)
        print 'checking game'
        x1 = data['victory'][0][0]
        y1 = data['victory'][0][1]
        x2 = data['victory'][1][0]
        y2 = data['victory'][1][1]
        x3 = data['victory'][2][0]
        y3 = data['victory'][2][1]
        x4 = data['defeated'][0][0]
        y4 = data['defeated'][0][1]
        x5 = data['defeated'][1][0]
        y5 = data['defeated'][1][1]
        x6 = data['defeated'][2][0]
        y6 = data['defeated'][2][1]
        screen = ImageGrab.grab()
        if( compare(screen.getpixel((x1,y1)),data['victory'][0][2]) and
            compare(screen.getpixel((x2,y2)),data['victory'][1][2]) and
            compare(screen.getpixel((x3,y3)),data['victory'][2][2])):
            notEnd = False
            result = 'victory'
            print 'run end.'
        elif(compare(screen.getpixel((x4,y4)),data['defeated'][0][2]) and
            compare(screen.getpixel((x5,y5)),data['defeated'][1][2]) and
            compare(screen.getpixel((x6,y6)),data['defeated'][2][2])):
            notEnd = False
            result = 'defeated'
            print 'run end.'
    time.sleep(2)
    if(result == 'defeated'):
        print 'run defeated.'
        dungeonDefeated(data)
    elif(result == 'victory'):
        print 'run victory.'
        dungeonVictory(data)
    else:
        print 'no run result found'
    time.sleep(2)
    click(data['victory'][4][0],data['victory'][4][1])  #replay
    time.sleep(1)
    x6 = data['buyEnergy'][0][0]
    y6 = data['buyEnergy'][0][1]

def hohVictory(data):
    click(data['victory'][2][0],data['victory'][2][1])      #victory summary
    time.sleep(2)
    click(data['victory'][2][0],data['victory'][2][1])      #chest
    time.sleep(2)
    click(data['victory'][8][0],data['victory'][8][1])      #HOH pieces OK button
    time.sleep(2)

def hoh(t):
    with open('dragon.json','rb') as f:
        data = json.load(f)
    click(data['start'][0],data['start'][1])
    notEnd = True
    print 'wait for ' + str(t) + ' min.'
    time.sleep(60 * t)
    while(notEnd):
        time.sleep(5)
        print 'checking game'
        x1 = data['victory'][0][0]
        y1 = data['victory'][0][1]
        x2 = data['victory'][1][0]
        y2 = data['victory'][1][1]
        x3 = data['victory'][2][0]
        y3 = data['victory'][2][1]
        x4 = data['defeated'][0][0]
        y4 = data['defeated'][0][1]
        x5 = data['defeated'][1][0]
        y5 = data['defeated'][1][1]
        x6 = data['defeated'][2][0]
        y6 = data['defeated'][2][1]
        screen = ImageGrab.grab()
        if( compare(screen.getpixel((x1,y1)),data['victory'][0][2]) and
            compare(screen.getpixel((x2,y2)),data['victory'][1][2]) and
            compare(screen.getpixel((x3,y3)),data['victory'][2][2])):
            notEnd = False
            result = 'victory'
            print 'run end.'
        elif(compare(screen.getpixel((x4,y4)),data['defeated'][0][2]) and
            compare(screen.getpixel((x5,y5)),data['defeated'][1][2]) and
            compare(screen.getpixel((x6,y6)),data['defeated'][2][2])):
            notEnd = False
            result = 'defeated'
            print 'run end.'
    time.sleep(2)
    if(result == 'defeated'):
        print 'run defeated.'
        dungeonDefeated(data)
    elif(result == 'victory'):
        print 'run victory.'
        hohVictory(data)
    else:
        print 'no run result found'
    time.sleep(2)
    click(data['victory'][4][0],data['victory'][4][1])  #replay
    time.sleep(1)
    x6 = data['buyEnergy'][0][0]
    y6 = data['buyEnergy'][0][1]

print 'Summoners War Auto Farming Script by Infinity'
while(True):
    print 'Please choose 1)start 2)set up 3)exit'
    choice = raw_input('')
    if choice == '1':
        print 'Choose map 1)GB/DB/NB 2)HOH'
        choice = raw_input('')
        print 'Choose mode 1)set number of runs 2)set number of refills'
        mode = raw_input('')
        if mode == '1':
            i = input('set number of runs\n')
            refills = 9999
        elif mode == '2':
            i = 9999
            refills = input('set number of refills\n')
        else:
            print 'invalid input'
            continue
        t = input('set initial wait in minutes\n')
        if choice == '1':
            while(i>0):
                dungeon(t)
                if(compare(scr.pixel_color(x6,y6),data['buyEnergy'][0][2])):
                    print 'not enough energy.'
                    if refills > 0:
                        recharge(data)
                        refills = refills - 1
                        if mode == '2':
                            print str(refills) + ' refill(s) left.'
                    else:
                        print 'run finished.'
                        break
                i = i-1
                if mode == '1':
                    print str(i) + ' run(s) left.'
            print 'run finished.'
        elif choice == '2':
            while(i>0):
                hoh(t)
                if(compare(scr.pixel_color(x6,y6),data['buyEnergy'][0][2])):
                    print 'not enough energy.'
                    if refills > 0:
                        recharge(data)
                        refills = refills - 1
                        if mode == '2':
                            print str(refills) + ' refill(s) left.'
                    else:
                        print 'run finished.'
                        break
                i = i-1
                if mode == '1':
                    print str(i) + ' run(s) left.'
            print 'run finished.'
        else:
            print 'invalid input.'
    elif choice == '2':
        new_queue.setupDungeon()
        print 'set up finished'
    elif choice == '3':
        break
    else:
        print 'invalid input'
