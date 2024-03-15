TwinTowers = 452
MyCityTallestBuilding = int(input("What's the height of your tallest building in metres?"))
if TwinTowers < MyCityTallestBuilding:
    print("Oh ok, our tower is smaller than yours.")
elif TwinTowers == MyCityTallestBuilding:
    print("You must live in KL too!")
elif TwinTowers > MyCityTallestBuilding:
    print("Haha, your tower small.")
