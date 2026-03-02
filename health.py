def take_damage(player, amount):
    player ["health"] = max(0, player["health"] - amount)
    if player["health"] == 0:
        player ["alive"] == False
    return player - amount

def heal(player, amount):
    return player + amount

def is_alive(player):
    if player > 0:
        return True
    else:
        return False