print("dictionary - 사전")

player = {10: "son", 20: "kim", 5: "lee"}

print(player)

print(player[10])

print(player.get(10))

player[50] = "hwan"

print(player[50])

key = 10

if key in player:
    print(f"key {key} exist - value : {player[10]}")
else:
    print(f"key {key} is not exit")


print(player)

del player[50]

print(player)

print(player.keys())

print(player.values())

print(player.items())

player.clear()

print(player)

