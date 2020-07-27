import numpy as np


def game_core_v3(number):
    count = 1

    predict = 50  # Начинаем гадать с 50
    number_from = 1
    number_to = 101

    while predict != number:
        count += 1

        if predict < number:
            number_from = predict
        elif predict > number:
            number_to = predict

        # После каждой попытки сужаем границы генерации случайного числа
        predict = np.random.randint(number_from, number_to)
    else:
        return count


def score_game(game_core):
    # Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core_v3)