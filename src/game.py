PlayerList = []

# ngebuat global dan menginisialisasi playerlist sebagai list kosong
def initPlayers():
    global PlayerList
    PlayerList = []

# ngebuat dictionary berisi data player baru
def createNewPlayer(name, damage=0, defensePower=0):
    return {
        "name": name,
        "damage": damage,
        "defensePower": defensePower,
        "health": 100,
        "defense": False,
        "score": 0
    }

# nambahin player ke playerlist
def addPlayer(player):
    PlayerList.append(player)

# ngehapus player dari playerlist
def removePlayer(name):
    for i in range(len(PlayerList)):
        if PlayerList[i]["name"] == name:
            PlayerList.remove(PlayerList[i])
            return True
    return print("There is no player with that name!")

# ngeset value dari key tertentu dari player sesuai dengan parameter
def setPlayer(player, key, value):
    player[key] = value
    
# ngecek apakah target berlindung atau tidak dan mengurangi health target sesuai dengan damage attacker    
def attackPlayer(attacker: dict, target: dict):
    damage = attacker['damage']
    if target['defense'] == True:
        damage -= target['defensePower']
        setPlayer(attacker, 'score', attacker['score'] + 0.8)
    else:
        setPlayer(attacker, 'score', attacker['score'] + 1)
    if damage < 0:
        damage = 0
    setPlayer(target, 'health', target['health'] - damage)
    setPlayer(target, 'defense', False)                 

# nampilin hasil match menurut score dan health player menggunakan bubble sort
def displayMatchResult():
    sortedplayers = PlayerList[:]
    n = len(sortedplayers)
    for i in range(n):
        for j in range(0, n-i-1):
            if (sortedplayers[j]['score'], sortedplayers[j]['health']) < (sortedplayers[j+1]['score'], sortedplayers[j+1]['health']):
                sortedplayers[j], sortedplayers[j+1] = sortedplayers[j+1], sortedplayers[j]
    
    for i in range(len(sortedplayers)):
        print(f"Rank {i+1}: {sortedplayers[i]['name']} | Score: {sortedplayers[i]['score']} | Health: {sortedplayers[i]['health']}")