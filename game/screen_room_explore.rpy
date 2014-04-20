#

# Путь до кнопок-спрайтов предметов.
# rooms/[CHARACTER]/items/buttons/[ITEM_TAG]_%s.png 

# Путь до соответствующих им больших превьюшек.
# rooms/[CHARACTER]/items/pictures/[ITEM_TAG]_%s.png 

# класс предметов

init python:
    # ??? enumeration
    #class Approach:
    #    Hook = "Hook"
    #    Key = "Key"
    #    Needle = "Needle"

    #
    class RoomItem:
        """
        Содержит описание предмета в комнате
        """
        def __init__(self, tag=None, approach=None, name = None, x = 0, y = 0, is_active = True, description = None):
            """
            Конструктор класа
                `tag`
                    Описывает ключевое слово, по которому выбираются файлы предметов.
                `approach`
                    Определяет 'подход' предмета. В идеале перечисление, но так строковый:
                        "Hook" - крючок
                        "Needle" - игла
                        "Key" - ключ
                        "Simple" - обычный
                `name`
                    Название предмета, для удобства пересекается с `tag`. Показывается в подсказке
                    и в названии при осмотре.
                `x`
                    Положение предмета по ости X.
                `y`
                    Положение предмета по оси Y.
                `is_active`
                    Активен ли предмет для использования? True - да, False - нет.
                `description`
                    Описание предмета, используется при его осмоттре.
            """
            self.tag = tag
            self.type = approach
            self.name = name
            self.x = x
            self.y = y
            self.is_active = is_active
            self.description = description

    #class RoomItemShowHint(Action):
    #    def __init_

###########################################
#           Комната персонажа             #
###########################################
screen room_explore:
    tag tag_room_explore # Если другой screen будет помечен таким же тего, текущий заменится.
    
    modal True # Может отключить?
    $ room_back = "rooms/" + room_name + "/back/clear.png"
    add room_back
    if room_items:
        for index, item in enumerate(room_items):
            $ item_filemask = "rooms/"+room_name+"/items/buttons/"+item.tag+"_%s.png"
            #TODO Поправить. Должно быть условие else, при котором вместо кнопки выводится idle картинка. или выставить еще какое стостояние кнопки.
            if item.is_active:
                imagebutton:
                    auto item_filemask 
                    focus_mask True # Использовать как активную зону только непрозрачные изображения.
                    hovered Show("room_item_hint", my_hint = item.name) # Вызов подсказки
                    unhovered Hide("room_item_hint") # Скрытие подсказки
                    xpos item.x
                    ypos item.y
                    action Show("room_item_dialog", my_item = item) # Вызов осмотра предмета.

###########################################
#           Осмотр предмета
###########################################
screen room_item_dialog:
    #tag tag_room_item_dialog
    #add "color fade"    # Добавляет затенение экрану, описано в script.rpy
                        #TODO пернести описания ресурсов в специальную init зону в отдельном скрипте

    # Фон меню осмотра.
    $ gui_splash_menu_bg = "gui/rooms/splash_menu_bg.png"
    add gui_splash_menu_bg xpos 540 ypos 140

    # Картинка предмета.
    #$ item_picture = "rooms/"+room_name+"/items/pictures/"+my_item.tag+".png"
    #add item_picture xalign 0.5 yalign 0.3

    # Заголовок
    text my_item.name xanchor 0.5 xpos 1470 ypos 190 font "gui/fonts/calibri.ttf" size 36
    # Описание
    text my_item.description maximum (480,315) xpos 1240 ypos 250 font "gui/fonts/calibri.ttf" size 24

    # Изучить
    imagebutton auto "gui/rooms/btn1_%s.png" xpos 1280 ypos 630
    # Продолжить
    imagebutton auto "gui/rooms/btn2_%s.png" xpos 1280 ypos 740 action Hide("room_item_dialog")

###########################################
#           Подсказка для предмета
###########################################
screen room_item_hint:
    #tag tag_room_explore
    text my_hint xalign 0.5 yalign 1.0 color "#000" 


# """ Пример использования в игре.
#$ room_name = "KODIN"
#$ room_items = []
#$ room_items.appeng( Item("book",x,y,"Книга", "Книга сказок.") )
#if flag["kodin"]["purity"] < 5:
#    $ room_items.appeng( Item("panty",x,y,"Трусики", "Небрежно брошенные трусики.") )
#call screen room_explore
#"""