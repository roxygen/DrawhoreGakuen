# Список ресурсов.

image bg room kodin = "rooms/KODIN/back/all.png"
image bg locker = "locker_empty.png"
image color fade = Solid("#00000099")
image bust main = "main_character.png"


# Описание NVL персонажа.
define monologue = Character(None, kind=nvl)


init python:
    # описание NVL окна.
    #TODO Подредактировать да перенести куда-нибудь.
    style.nvl_window.background = "window.png"
    #style.nvl_window.xpos = 326
    style.nvl_window.ypos = 0
    style.nvl_window.left_padding = 200
    style.nvl_window.right_padding = 10
    style.nvl_window.top_padding = 50
    style.nvl_window.bottom_padding = 50
    style.nvl_window.left_margin = config.screen_width / 3

init:
    # Задание позиций для персонажей.
    $ CR = Position(xpos = config.screen_width * 2 / 3 )
    $ CC = Position(xpos = config.screen_width / 2 )
    $ LC = Position(xpos = config.screen_width * 1 / 4 )

# Игра начинается здесь.
label start:
    scene bg room kodin
    #show bust main at LC
    #with dissolve


    #monologue "Беспросветно мрачное: «Будь, готов ко всему!»"
    #hide bust main
    call KODIN_ROOM_SCENE
    return

label KODIN_ROOM_SCENE:

    $ room_name = "KODIN"
    $ room_items = []
    #$ room_items.append(RoomItem("", "HOOK", "Книга", 243, 79, True, " Магический фолиант в твердой обложке. От него пахнет ладаном."))
    $ room_items.append(RoomItem("obj1",1,"Фигурка Распутницы", 0,0, True, "Сора. Магический фолиант в твердой обложке. От него пахнет ладаном. Сора. Магический фолиант в твердой обложке. От него пахнет ладаном. Сора. Магический фолиант в твердой обложке. От него пахнет ладаном."))
    $ room_items.append(RoomItem("obj2",1,"Фигурка Учёного", 0,0, True, "Курису"))
    $ room_items.append(RoomItem("obj3",1,"Фигурка Воительницы", 0,0, True, "Рёги."))
    $ room_items.append(RoomItem("obj4",1,"Наушники", 0,0, True, "Дешевые"))


    call screen room_explore
    return