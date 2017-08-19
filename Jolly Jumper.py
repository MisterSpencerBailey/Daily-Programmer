

def jumper(jolly):
    differences = []
    for number in range (jolly[1],len(jolly)):
        differences.append(jolly[number]-jolly[number+1])
    for changes in range(len(differences)-1):
        print(differences[changes])
        if differences[changes] - 1 != differences[changes+1]:
            return False
        else:
            print("Good")

jumper([4 ,1 ,4 ,2 ,3])