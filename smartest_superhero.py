# Задание «Кто самый умный супергерой (часть 1)?
#Есть API https://akabab.github.io/superhero-api/api/  по информации о супергероях с информацией по всем супергероям. 
# Напишите функцию для определения самого умного супергероя среди Hulk, Captain America, Thanos.

import requests
from pprint import pprint

#  Пример с лекции
#======================================================================================================
# my_heroes = ['Ajax', 'Darkstar', 'Spider-Man']
# url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
# all_heroes_info = requests.get(url).json()
# # pprint(all_heroes_info)
# for hero_info in all_heroes_info:
#     hero_name = hero_info['name']
#     if hero_name in my_heroes:
#         print(hero_name, hero_info['powerstats']['durability'])
#======================================================================================================

# Мое решение
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# def get_the_smartest_superhero() -> str:
#     the_smartest_superhero = ''
#     # print(get_the_smartest_superhero())
#     my_heroes = ['Hulk', 'Captain America', 'Thanos']
#     url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
#     all_heroes_info = requests.get(url).json()
#     smartest_heroes = {}
#     for hero_info in all_heroes_info:
#         hero_name = hero_info['name']   
#         if hero_name in my_heroes:
#             smartest_heroes[hero_name] = [hero_info['powerstats']['intelligence']]        
#     the_smartest_superhero = sorted(smartest_heroes.items(), key=lambda item: item[1], reverse=True)[0][0]     
#     return the_smartest_superhero
# print(get_the_smartest_superhero())

# Решение эксперта
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def get_the_smartest_superhero() -> str:
    base_url = "https://akabab.github.io/superhero-api/api"
    hulk = 332
    captain_america = 149
    thanos = 655
    max_intelligence = 0
    the_smartest_superhero = ''
    for superhero_id in (hulk, captain_america, thanos):
        url = base_url + f"/id/{superhero_id}.json"
        response = requests.get(url)
        info = response.json()
        intelligence = info['powerstats']['intelligence']
        if intelligence > max_intelligence:
            max_intelligence = intelligence
            the_smartest_superhero = info['name']
    return the_smartest_superhero

if __name__ == '__main__':
    assert get_the_smartest_superhero() == 'Thanos'
