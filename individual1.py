def check_ranking(teams, scores):
    sorted_teams = sorted(teams, key=lambda x: scores[teams.index(x)], reverse=True)
    return sorted_teams == teams

# Ввод списка команд и очков
teams = input("Введите названия команд через запятую (например, 'Команда1, Команда2, Команда3'): ").split(", ")
scores = list(map(int, input("Введите суммы очков через пробел (например, '10 5 8'): ").split()))

# Проверяем, соответствуют ли команды занятым ими местам
result = check_ranking(teams, scores)

if result:
    print("Команды перечислены в соответствии с занятыми местами.")
else:
    print("Команды НЕ перечислены в соответствии с занятыми местами.")
