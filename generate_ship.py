import random

s_x = s_y = 8  # размер игрового поля - не меньше 8 и не больше 18 )))
ships = s_x // 2  # определяем максимальное кол-во кораблей
ship_len1 = s_x // 5  # длина первого типа корабля
ship_len2 = s_x // 3  # длина второго типа корабля
ship_len3 = s_x // 2  # длина третьего типа корабля

def generate_ships_list():
    global ships_list
    ships_list = []
    # генерируем список случайных длин кораблей
    for i in range(0, ships):
        ships_list.append(random.choice([ship_len1, ship_len2, ship_len3]))
    # print(ships_list)

def generate_enemy_ships():
    global ships_list
    enemy_ships = []

    # подсчет суммарной длины кораблей
    sum_1_all_ships = sum(ships_list)
    sum_1_enemy = 0

    # print("sum: ", sum_1_all_ships)

    while sum_1_enemy != sum_1_all_ships:
        # обнуляем массив кораблей врага
        enemy_ships = [[0 for i in range(s_x + 1)] for i in
                       range(s_y + 1)]  # +1 для доп. линии справа и снизу, для успешных проверок генерации противника

        for i in range(0, ships):
            len = ships_list[i]
            horizont_vertikal = random.randrange(1, 3)  # 1- горизонтальное 2 - вертикальное

            primerno_x = random.randrange(0, s_x)
            if primerno_x + len > s_x:
                primerno_x = primerno_x - len

            primerno_y = random.randrange(0, s_y)
            if primerno_y + len > s_y:
                primerno_y = primerno_y - len

            # print(horizont_vertikal, primerno_x,primerno_y)
            if horizont_vertikal == 1:
                if primerno_x + len <= s_x:
                    for j in range(0, len):
                        try:
                            check_near_ships = 0
                            check_near_ships = enemy_ships[primerno_y][primerno_x - 1] + \
                                               enemy_ships[primerno_y][primerno_x + j] + \
                                               enemy_ships[primerno_y][primerno_x + j + 1] + \
                                               enemy_ships[primerno_y + 1][primerno_x + j + 1] + \
                                               enemy_ships[primerno_y - 1][primerno_x + j + 1] + \
                                               enemy_ships[primerno_y + 1][primerno_x + j] + \
                                               enemy_ships[primerno_y - 1][primerno_x + j]
                            # print(check_near_ships)
                            if check_near_ships == 0:  # записываем в том случае, если нет ничего рядом
                                enemy_ships[primerno_y][primerno_x + j] = i + 1  # записываем номер корабля
                        except Exception:
                            pass
            if horizont_vertikal == 2:
                if primerno_y + len <= s_y:
                    for j in range(0, len):
                        try:
                            check_near_ships = 0
                            check_near_ships = enemy_ships[primerno_y - 1][primerno_x] + \
                                               enemy_ships[primerno_y + j][primerno_x] + \
                                               enemy_ships[primerno_y + j + 1][primerno_x] + \
                                               enemy_ships[primerno_y + j + 1][primerno_x + 1] + \
                                               enemy_ships[primerno_y + j + 1][primerno_x - 1] + \
                                               enemy_ships[primerno_y + j][primerno_x + 1] + \
                                               enemy_ships[primerno_y + j][primerno_x - 1]
                            # print(check_near_ships)
                            if check_near_ships == 0:  # записываем в том случае, если нет ничего рядом
                                enemy_ships[primerno_y + j][primerno_x] = i + 1  # записываем номер корабля
                        except Exception:
                            pass

        # делаем подсчет 1ц
        sum_1_enemy = 0
        for i in range(0, s_x):
            for j in range(0, s_y):
                if enemy_ships[j][i] > 0:
                    sum_1_enemy = sum_1_enemy + 1
    return enemy_ships

generate_ships_list()
print(generate_enemy_ships())