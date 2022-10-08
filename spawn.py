from random import choice

spawn = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
cords = {1: True, 2: True, 3: True, 4: True, 5: True, 6: True, 7: True, 8: True, 9: True, 10: True, 11: True, 12: True,
         13: True, 14: True, 15: True}


def spawn_x():
    ans = choice(spawn)
    while True:
        if cords[ans] == True:
            cords[ans] = False
            break
        else:
            ans = choice(spawn)
    return ans
