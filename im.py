import os
import random

name = input("как вас зовут? ")
if not name:
    name = "Илья"

way_1 = True
way_2 = True
way_3 = True
game = True
key = ""

while game:

    if way_1 or way_2 or way_3:
        key = ""
        os.system("cls")
        print("текс у камня")
        if way_1:
            print("1 - пойти к разбойникам")
        if way_2:
            print("2 - женатому быть")
        if way_3:
            print("3 - богатому быть")

        user_choice = input("введите номер ответа и нажмите ENTER ")
        key += user_choice

    if way_1 and key == "1":
        os.system("cls")
        print("Текс дорога 1")
        print("1 - выбор")
        print("2 - выбор")

        user_choice = input("Введите номер ответа и нажмите ENTER ")
        key += user_choice

    if way_1 and key == "11":
        os.system("cls")
        print("текс дорога 1 - ты победил всех разбойников")
        way_1 = False

    if way_1 and key == "12":
        os.system("cls")
        print("текс дорога 1 - тебя убили разбойники")
        game = False

    if way_2 and key == "2":
        os.system("cls")
        print("текс дорга 2")
        print("1 - выбор")
        print("2 - выбор")

        user_choice = input("введите номер ответа и нажмите ENTER ")
        key += user_choice

    if way_2 and key == "21":
        os.system("cls")
        print("текс дорога 2 - ты поженился ура")
        way_2 = False

    if way_2 and key == "22":
        os.system("cls")
        print("текс дорога 2 - ты попал в засаду,жена была подставная")
        game = False

    if way_3 and key == "3":
        os.system("cls")
        print("текс дорога 3")
        print("1 - выбор")
        print("2 - выбор")

        user_choice = input("введите номер ответа и нажмите ENTER ")
        key += user_choice

    if way_3 and key == "31":
        os.system("cls")
        print("текс дорога 3 - ты забрал все богаства и стал богатым")
        way_3 = False

    if way_3 and key == "32":
        os.system("cls")
        print("текс дорога 3 - это были не настоящие богаства")
        game = False

print("все дороги проедены")