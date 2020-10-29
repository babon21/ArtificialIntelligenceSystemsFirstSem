from anytree import Node, RenderTree
from anytree.exporter import UniqueDotExporter
from anytree.exporter import JsonExporter
import pydot

class Sport:
    name = ""
    olympic = False
    min_age = 0
    min_participants = 0
    popularity = 0

    def __init__(self, name, olympic, min_age, min_participants):
        self.name = name
        self.olympic = olympic
        self.min_age = min_age
        self.min_participants = min_participants
        # self.popularity = popularity

    def getLine(self):
        line = ""
        line += "name: " + str(self.name) + "\n"
        line += "olympic: " + str(self.olympic) + "\n"
        line += "min_age: " + str(self.min_age) + "\n"
        line += "min_participants: " + str(self.min_participants) + "\n"
        # line += "popularity: " + str(self.arom) + "\n"
        return line


root = Node("Виды спорта")

record = Node("Рекордные", parent=root)
contact = Node("Контактные", parent=root)

cyclic = Node("Циклические", parent=record)
speed_power = Node("Скоростно-силовые", parent=record)

single_combat = Node("Единоборства", parent=contact)
sport_games = Node("Спортивные игры", parent=contact)

personal_team = Node("Лично-командные", parent=sport_games)
team = Node("Командные", parent=sport_games)

shock = Node("Ударные", parent=single_combat)
wrestling = Node("Борцовские", parent=single_combat)
mixed = Node("Смешанные", parent=single_combat)

weightlifting = Node("Тяжелая атлетика", parent=speed_power, props=Sport("Тяжелая атлетика", True, 10, 1))
throwing = Node("Метание", parent=speed_power, props=Sport("Метание", True, 9, 1))
jumping = Node("Прыжки", parent=speed_power, props=Sport("Прыжки", True, 9, 1))
boating = Node("Гребля", parent=cyclic, props=Sport("Гребля", True, 9, 1))
swimming = Node("Плавание", parent=cyclic, props=Sport("Плавание", True, 7, 1))
run = Node("Бег", parent=cyclic, props=Sport("Бег", True, 7, 1))
freestyle_wrestling = Node("Вольная борьба", parent=wrestling, props=Sport("Вольная борьба", True, 11, 2))
judo = Node("Дзюдо", parent=wrestling, props=Sport("Дзюдо", True, 11, 2))
jujutsu = Node("Джиу-джитсу", parent=wrestling, props=Sport("Джиу-джитсу", False, 9, 2))
boxing = Node("Бокс", parent=shock, props=Sport("Бокс", True, 9, 2))
thai_boxing = Node("Тайский бокс", parent=shock, props=Sport("Тайский бокс", False, 9, 2))
karate = Node("Карате", parent=shock, props=Sport("Карате", True, 9, 2))
taekwondo = Node("Тхэквондо", parent=shock, props=Sport("Тхэквондо", True, 7, 2))
checkers = Node("Шашки", parent=personal_team, props=Sport("Шашки", False, 6, 2))
golf = Node("Гольф", parent=personal_team, props=Sport("Гольф", False, 7, 2))
billiards = Node("Бильярд", parent=personal_team, props=Sport("Бильярд", False, 8, 2))
chess = Node("Шахматы", parent=personal_team, props=Sport("Шахматы", True, 6, 2))
tennis = Node("Теннис", parent=personal_team, props=Sport("Теннис", True, 6, 2))
table_tennis = Node("Настольный теннис", parent=personal_team, props=Sport("Настольный теннис", True, 6, 2))
badminton = Node("Бадминтон", parent=personal_team, props=Sport("Бадминтон", True, 8, 2))
rugby = Node("Регби", parent=team, props=Sport("Регби", False, 10, 15))
hockey = Node("Хоккей", parent=team, props=Sport("Хоккей", True, 9, 20))
football = Node("Футбол", parent=team, props=Sport("Футбол", True, 9, 11))
handball = Node("Гандбол", parent=team, props=Sport("Гандбол", True, 9, 7))
volleyball = Node("Волейбол", parent=team, props=Sport("Волейбол", True, 9, 6))
water_polo = Node("Водное поло", parent=team, props=Sport("Водное поло", True, 9, 13))
softball = Node("Софтбол", parent=team, props=Sport("Софтбол", True, 9, 9))
baseball = Node("Бейсбол", parent=team, props=Sport("Бейсбол", True, 9, 9))
basketball = Node("Баскетбол", parent=team, props=Sport("Баскетбол", True, 8, 5))

# for pre, fill, node in RenderTree(sports):
#     print("%s%s" % (pre, node.name))

print(RenderTree(root))


def getProps(node):
    propsLine = ""
    if hasattr(node, "props"):
        propsLine += "\n" + node.props.getLine()
    else:
        propsLine += node.name
    return 'label="{}"'.format(propsLine)

dot = UniqueDotExporter(root, nodeattrfunc=getProps)
dot.to_dotfile("tree.dot")

(graph,) = pydot.graph_from_dot_file("tree.dot")
graph.write_png("tree.png")
