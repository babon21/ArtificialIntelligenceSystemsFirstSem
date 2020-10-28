from anytree import Node, RenderTree
from anytree.exporter import DotExporter

sports = Node("Виды спорта")

record = Node("Рекордные", parent=sports)
contact = Node("Контактные", parent=sports)

cyclic = Node("Циклические", parent=record)
speed_power = Node("Скоростно-силовые", parent=record)

weightlifting = Node("Тяжелая атлетика", parent=speed_power)
throwing = Node("Метание", parent=speed_power)
jumping = Node("Прыжки", parent=speed_power)

boating = Node("Гребля", parent=cyclic)
swimming = Node("Плавание", parent=cyclic)
run = Node("Бег", parent=cyclic)

single_combat = Node("Единоборства", parent=contact)
sport_games = Node("Спортивные игры", parent=contact)

shock = Node("Ударные", parent=single_combat)
wrestling = Node("Борцовские", parent=single_combat)
mixed = Node("Смешанные", parent=single_combat)

freestyle_wrestling = Node("Вольная борьба", parent=wrestling)
judo = Node("Дзюдо", parent=wrestling)
jujutsu = Node("Джиу-джитсу", parent=wrestling)

boxing = Node("Бокс", parent=shock)
thai_boxing = Node("Тайский бокс", parent=shock)
karate = Node("Карате", parent=shock)
taekwondo = Node("Тхэквондо", parent=shock)

personal_team = Node("Лично-командные", parent=sport_games)
team = Node("Командные", parent=sport_games)

checkers = Node("Шашки", parent=personal_team, olympic=False)
golf = Node("Гольф", parent=personal_team, olympic=False)
billiards = Node("Бильярд", parent=personal_team, olympic=False)

chess = Node("Шахматы", parent=personal_team, olympic=True)
tennis = Node("Теннис", parent=personal_team, olympic=True)
table_tennis = Node("Настольный теннис", parent=personal_team, olympic=True)
badminton = Node("Бадминтон", parent=personal_team, olympic=True)

rugby = Node("Регби", parent=team, olympic=False)
motoball = Node("Мотобол", parent=team, olympic=False)
lapta = Node("Лапта", parent=team, olympic=False)

hockey = Node("Хоккей", parent=team, olympic=True)
football = Node("Футбол", parent=team, olympic=True)
handball = Node("Гандбол", parent=team, olympic=True)
volleyball = Node("Волейбол", parent=team, olympic=True)
water_polo = Node("Водное поло", parent=team, olympic=True)
softball = Node("Софтбол", parent=team, olympic=True)
baseball = Node("Бейсбол", parent=team, olympic=True)
basketball = Node("Баскетбол", parent=team, olympic=True)

for pre, fill, node in RenderTree(sports):
    print("%s%s" % (pre, node.name))

print(RenderTree(sports))

# graphviz needs to be installed for the next line!
DotExporter(sports).to_picture("udo.png")


