import json

data = {
    'start':[1240,595],
    'victory':[
        [493,450,[63,165,241]],
        [818,445,[247,205,102]],
        [1151,448,[230,37,87]],     #checking victory 0-2
        [888,669,[244,229,169]],    #checking rune 3
        [616,475,[247,206,102]],    #checking repaly 4
        [799,663]                   #US,MS,rainbowmon 5
    ],
    'defeated':[
        [],
        [],
        [842,227,[135,171,51]]      #checking defeated 1
    ],
    'buyEnergy':[
        [649,523,[204,159,67]],     #recharge yes button background
        [525,486,[226,197,130]],    #shop energy background
        [732,529,[202,158,68]],     #confirm yes button background
        [835,522,[203,157,68]],     #purchase successful OK button
        [787,705,[236,227,194]]     #shop close button
    ]
}

with open('dragon.json','w') as f:
    json.dump(data,f)
