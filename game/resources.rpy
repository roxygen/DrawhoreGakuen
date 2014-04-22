init python:
    import xml.etree.ElementTree as ET
    DGDATA= {}
    DGDATA['items'] = {}
    # xml-файл ресурсов

    itemsRoot = ET.parse(renpy.file('data/items.xml')).getroot()

    #print sys.stdin.encoding #itemsRoot[0][0][1].text

    # Для всех персонажей
    for character in itemsRoot:
        #print ("Character name = " + character.attrib['name'])
        # Добавляем персональный словарь персонажа
        _charname = character.attrib['name']
        DGDATA['items'][_charname] = {}

        # Для всех предметов
        for item in character.findall('item'):
            #print (item.find('name'))
            _tag = item.find('tag').text
            DGDATA['items'][_charname][_tag] = {}
            #DGDATA['items'][_charname][_tag]['tag'] = item.find('tag').text
            DGDATA['items'][_charname][_tag]['name'] = item.find('name').text
            DGDATA['items'][_charname][_tag]['approach'] = int(item.find('approach').text) # Пока что так
            DGDATA['items'][_charname][_tag]['x'] = int(item.find('x').text)
            DGDATA['items'][_charname][_tag]['y'] = int(item.find('y').text)
            DGDATA['items'][_charname][_tag]['description'] = item.find('description').text
            DGDATA['items'][_charname][_tag]['is_active'] = int(item.find('is_active').text)