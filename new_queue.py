import json,os
import mouse_position as mp

def setupDungeon():
    if os.path.isfile('./dragon.json'):
        with open('dragon.json','rb') as f:
            data = json.load(f)
    else:
        data = {
            'start':[1240,595],
            'victory':[
                [493,450,[63,165,241]],
                [818,445,[247,205,102]],
                [1151,448,[230,37,87]],     #checking victory 0-2
                [888,669,[244,229,169]],    #checking rune 3
                [616,475,[247,206,102]],    #checking repaly 4
                [799,663],                  #US,MS,rainbowmon 5
                [0,0,[0,0,0]],              #checking 4 star rune 6
                [0,0,[0,0,0]]               #sell rune button 7
            ],
            'defeated':[
                [0,0,[0,0,0]]               #revive crystal label
                [0,0,[0,0,0]]               #revive 10 text
                [842,227,[135,171,51]]      #revive NO text
            ],
            'buyEnergy':[
                [649,523,[204,159,67]],     #recharge yes button background
                [525,486,[226,197,130]],    #shop energy background
                [732,529,[202,158,68]],     #confirm yes button background
                [835,522,[203,157,68]],     #purchase successful OK button
                [787,705,[236,227,194]]     #shop close button
            ]
        }

    print 'point 0: start button'
    nothing = raw_input('Enter 0 to skip or just press Enter to start\n\n')
    if nothing != '0':
        x,y,c = mp.get_mouse_position()
        data['start'] = [x,y]

    print 'point 1: victory mana label'
    nothing = raw_input('Enter 0 to skip or just press Enter to start\n\n')
    if nothing != '0':
        data['victory'][0] = mp.get_mouse_position()

    print 'point 2: victory energy label'
    nothing = raw_input('Enter 0 to skip or just press Enter to start\n')
    if nothing != '0':
        data['victory'][1] = mp.get_mouse_position()

    print 'point 3: victory crystal label'
    nothing = raw_input('Enter 0 to skip or just press Enter to start\n')
    if nothing != '0':
        data['victory'][2] = mp.get_mouse_position()

    print 'point 4: rune Get button text'
    nothing = raw_input('Enter 0 to skip or just press Enter to start\n')
    if nothing != '0':
        data['victory'][3] = mp.get_mouse_position()

    print 'point 5: scroll OK button below text'
    nothing = raw_input('Enter 0 to skip or just press Enter to start\n')
    if nothing != '0':
        data['victory'][5] = mp.get_mouse_position()

    print 'point 6: replay button text'
    nothing = raw_input('Enter 0 to skip or just press Enter to start\n')
    if nothing != '0':
        data['victory'][4] = mp.get_mouse_position()

    print 'point 7: Revive crystal label'
    nothing = raw_input('Enter 0 to skip or just press Enter to start\n')
    if nothing != '0':
        data['defeated'][0] = mp.get_mouse_position()

    print 'point 8: Revive 10 text'
    nothing = raw_input('Enter 0 to skip or just press Enter to start\n')
    if nothing != '0':
        data['defeated'][1] = mp.get_mouse_position()

    print 'point 9: Revive NO text'
    nothing = raw_input('Enter 0 to skip or just press Enter to start\n')
    if nothing != '0':
        data['defeated'][2] = mp.get_mouse_position()

    print 'point 10: recharge Yes button background'
    nothing = raw_input('Enter 0 to skip or just press Enter to start\n')
    if nothing != '0':
        data['buyEnergy'][0] = mp.get_mouse_position()

    print 'point 11: shop recharge energy'
    nothing = raw_input('Enter 0 to skip or just press Enter to start\n')
    if nothing != '0':
        data['buyEnergy'][1] = mp.get_mouse_position()

    print 'point 12: recharge comfirm yes button'
    nothing = raw_input('Enter 0 to skip or just press Enter to start\n')
    if nothing != '0':
        data['buyEnergy'][2] = mp.get_mouse_position()

    print 'point 13: purchase successful OK button'
    nothing = raw_input('Enter 0 to skip or just press Enter to start\n')
    if nothing != '0':
        data['buyEnergy'][3] = mp.get_mouse_position()

    print 'point 14: shop Close button'
    nothing = raw_input('Enter 0 to skip or just press Enter to start\n')
    if nothing != '0':
        data['buyEnergy'][4] = mp.get_mouse_position()

    print 'point 15: rune 5th star'
    nothing = raw_input('Enter 0 to skip or just press Enter to start\n')
    if nothing != '0':
        data['victory'][6] = mp.get_mouse_position()

    print 'point 16: rune sell button'
    nothing = raw_input('Enter 0 to skip or just press Enter to start\n')
    if nothing != '0':
        data['victory'][7] = mp.get_mouse_position()

    with open('dragon.json','w') as f:
        json.dump(data,f)
