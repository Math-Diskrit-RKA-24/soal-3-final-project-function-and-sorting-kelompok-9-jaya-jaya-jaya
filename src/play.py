import game as g
import random as rd

def initialize_players():
    g.initPlayers()
    jumlahp = int(input("Masukin jumlah player: "))
    for i in range(jumlahp):
        name = input(f"Masukin nama player {i+1}: ")
        damage = int(input("Masukin damage : "))
        defensePower = int(input("Masukin defense power: "))
        player = g.createNewPlayer(name, damage, defensePower)
        g.addPlayer(player)
    
    for i in range(len(g.PlayerList)):
        player = g.PlayerList[i]
        print(f"Player {i+1}: {player['name']} | Damage: {player['damage']} | Defense Power: {player['defensePower']}")

def automatic(round_max=None):
    round_now = 1
    while len(g.PlayerList) > 1 and (round_max is None or round_now <= round_max):
        print(f"🎮 ROUND {round_now} MULAI 🎮")
        defended_players = []
        # Acak urutan pemain
        rd.shuffle(g.PlayerList)

        # Cek pemain yang sudah berlindung atau tidak sama dengan attacker
        for attacker in g.PlayerList:
            if attacker["name"] in defended_players:
                continue
            potential_targets = [p for p in g.PlayerList if p != attacker]
            if not potential_targets:
                break
            target = rd.choice(potential_targets)

            print(f"⚔️ {attacker['name']} menyerang {target['name']} ⚔️")
            # Gacha berlindung atau tidak
            if target["defensePower"] > 0:
                berlindung = rd.choice([True, False])
                if berlindung:
                    print(f"🛡️ {target['name']} memilih berlindung! 🛡️")
                    g.setPlayer(target, "defense", True)
                    defended_players.append(target["name"])
                else:
                    print(f"❌ {target['name']} tidak berlindung! ❌")
            else:
                print(f"❌ {target['name']} tidak bisa berlindung karena defense power 0! ❌")

            # Serang target
            g.attackPlayer(attacker, target)
            
            # Hapus pemain yang mati
            if target["health"] <= 0:
                print(f"💀 {target['name']} telah mati! 💀")
                g.removePlayer(target["name"])

        round_now += 1
        g.displayMatchResult()

def manual(round_max=None):
    round_now = 1
    while len(g.PlayerList) > 1 and (round_max is None or round_now <= round_max):
        print(f"🎮 ROUND {round_now} MULAI 🎮")
        # Nampilin player
        for i in range(len(g.PlayerList)):
            print(f"{i+1}. {g.PlayerList[i]['name']}")

        n = int(input("Pilih attacker (masukkan nomor pemain): ")) - 1
        attacker = g.PlayerList[n]

        # Pilih target
        print("Pilih target:")
        potential_targets = [p for p in g.PlayerList if p != attacker]
        for i, target in enumerate(potential_targets):
            print(f"{i+1}. {target['name']}")
        m = int(input("Masukkan nomor target: ")) - 1
        target = potential_targets[m]

        # Pilih bertahan atau tidak
        print(f"⚔️ {attacker['name']} menyerang {target['name']} ⚔️")
        if target["defensePower"] > 0:
            berlindung = input("Masukkan 'y' untuk bertahan atau 'n' untuk tidak: ").lower()
            if berlindung == 'y':
                print(f"🛡️ {target['name']} memilih berlindung! 🛡️")
                g.setPlayer(target, "defense", True)
            else:
                print(f"❌ {target['name']} tidak berlindung! ❌")
        else:
            print(f"❌ {target['name']} tidak bisa berlindung karena defense power 0! ❌")

        # Serang target
        g.attackPlayer(attacker, target)

        # Hapus pemain yang mati
        if target["health"] <= 0:
            print(f"💀 {target['name']} telah mati! 💀")
            g.removePlayer(target["name"])

        g.displayMatchResult()
        round_now += 1

initialize_players()

print("--Pilih Otomatis atau Manual--")
print("1. Otomatis")
print("2. Manual")

pilih = int(input("Masukkan pilihan: "))
if pilih == 1:
    print("Pilih mode")
    print("1. Round Terbatas")
    print("2. Battle Royale")
    mode = int(input("Masukkan mode: "))
    if mode == 1:
        round_max = int(input("Masukkan jumlah maksimal round: "))
        automatic(round_max)
    elif mode == 2:
        automatic()
elif pilih == 2:
    print("Pilih mode")
    print("1. Round Terbatas")
    print("2. Battle Royale")
    mode = int(input("Masukkan mode: "))
    if mode == 1:
        round_max = int(input("Masukkan jumlah maksimal round: "))
        manual(round_max)
    elif mode == 2:
        manual()
