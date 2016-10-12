import json,os
import mouse_position as mp

def setupDungeon():
    if os.path.isfile('./dragon.json'):
        with open('dragon.json','rb') as f:
            data = json.load(f)
    else:
        data = {
            'start':[],
            'victory':[
                [],
                [],
                [],     #checking victory 0-2
                [],    #checking rune 3
                [],    #checking repaly 4
                [],                  #US,MS,rainbowmon 5
                [0,0,[0,0,0]],              #checking 4 star rune 6
                [0,0,[0,0,0]],              #sell rune button 7
                []      #HOH pieces OK button 8
            ],
            'defeated':[
                [0,0,[0,0,0]],               #revive crystal label
                [0,0,[0,0,0]],               #revive 10 text
                []      #revive NO text
            ],
            'buyEnergy':[
                [],     #recharge yes button background
                [],    #shop energy background
                [],     #confirm yes button background
                [],     #purchase successful OK button
                []     #shop close button
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

    print 'point 4: rune 5th star'
    nothing = raw_input('Enter 0 to skip or just press Enter to start\n')
    if nothing != '0':
        data['victory'][6] = mp.get_mouse_position()

    print 'point 5: rune Get button text'
    nothing = raw_input('Enter 0 to skip or just press Enter to start\n')
    if nothing != '0':
        data['victory'][3] = mp.get_mouse_position()

    print 'point 6: rune sell button'
    nothing = raw_input('Enter 0 to skip or just press Enter to start\n')
    if nothing != '0':
        data['victory'][7] = mp.get_mouse_position()

    print 'point 7: scroll OK button below text'
    nothing = raw_input('Enter 0 to skip or just press Enter to start\n')
    if nothing != '0':
        data['victory'][5] = mp.get_mouse_position()

    print 'point 8: HOH pieces OK button'
    nothing = raw_input('Enter 0 to skip or just press Enter to start\n')
    if nothing != '0':
        data['victory'][8] = mp.get_mouse_position()

    print 'point 9: replay button text'
    nothing = raw_input('Enter 0 to skip or just press Enter to start\n')
    if nothing != '0':
        data['victory'][4] = mp.get_mouse_position()

    print 'point 10: Revive crystal label'
    nothing = raw_input('Enter 0 to skip or just press Enter to start\n')
    if nothing != '0':
        data['defeated'][0] = mp.get_mouse_position()

    print 'point 11: Revive "10" text'
    nothing = raw_input('Enter 0 to skip or just press Enter to start\n')
    if nothing != '0':
        data['defeated'][1] = mp.get_mouse_position()

    print 'point 12: Revive NO text'
    nothing = raw_input('Enter 0 to skip or just press Enter to start\n')
    if nothing != '0':
        data['defeated'][2] = mp.get_mouse_position()

    print 'point 13: recharge Yes button background'
    nothing = raw_input('Enter 0 to skip or just press Enter to start\n')
    if nothing != '0':
        data['buyEnergy'][0] = mp.get_mouse_position()

    print 'point 14: shop recharge energy'
    nothing = raw_input('Enter 0 to skip or just press Enter to start\n')
    if nothing != '0':
        data['buyEnergy'][1] = mp.get_mouse_position()

    print 'point 15: recharge comfirm yes button'
    nothing = raw_input('Enter 0 to skip or just press Enter to start\n')
    if nothing != '0':
        data['buyEnergy'][2] = mp.get_mouse_position()

    print 'point 16: purchase successful OK button'
    nothing = raw_input('Enter 0 to skip or just press Enter to start\n')
    if nothing != '0':
        data['buyEnergy'][3] = mp.get_mouse_position()

    print 'point 17: shop Close button'
    nothing = raw_input('Enter 0 to skip or just press Enter to start\n')
    if nothing != '0':
        data['buyEnergy'][4] = mp.get_mouse_position()

    with open('dragon.json','w') as f:
        json.dump(data,f)

    print 'set up finished\n'
