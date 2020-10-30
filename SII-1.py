import json
import math
import pydot
import pandas as pd
from anytree import Node, RenderTree, PreOrderIter
from anytree.exporter import UniqueDotExporter


class Sport:
    name = ""
    olympic = False
    min_age = 0
    min_participants = 0
    popularity = 0

    def __init__(self, name, olympic, min_age, min_participants, popularity):
        self.name = name
        self.olympic = olympic
        self.min_age = min_age
        self.min_participants = min_participants
        self.popularity = popularity

    def getLine(self):
        line = ""
        line += "name: " + str(self.name) + "\n"
        line += "olympic: " + str(self.olympic) + "\n"
        line += "min_age: " + str(self.min_age) + "\n"
        line += "min_participants: " + str(self.min_participants) + "\n"
        line += "popularity: " + str(self.popularity) + "\n"
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

weightlifting = Node("Тяжелая атлетика", parent=speed_power, props=Sport("Тяжелая атлетика", True, 10, 1, 2))
throwing = Node("Метание", parent=speed_power, props=Sport("Метание", True, 9, 1, 2))
jumping = Node("Прыжки", parent=speed_power, props=Sport("Прыжки", True, 9, 1, 2))
boating = Node("Гребля", parent=cyclic, props=Sport("Гребля", True, 9, 1, 1))
swimming = Node("Плавание", parent=cyclic, props=Sport("Плавание", True, 7, 1, 7))
run = Node("Бег", parent=cyclic, props=Sport("Бег", True, 7, 1, 7))
freestyle_wrestling = Node("Вольная борьба", parent=wrestling, props=Sport("Вольная борьба", True, 11, 2, 2))
judo = Node("Дзюдо", parent=wrestling, props=Sport("Дзюдо", True, 11, 2, 2))
jujutsu = Node("Джиу-джитсу", parent=wrestling, props=Sport("Джиу-джитсу", False, 9, 2, 2))
boxing = Node("Бокс", parent=shock, props=Sport("Бокс", True, 9, 2, 5))
thai_boxing = Node("Тайский бокс", parent=shock, props=Sport("Тайский бокс", False, 9, 2, 2))
karate = Node("Карате", parent=shock, props=Sport("Карате", True, 9, 2, 2))
taekwondo = Node("Тхэквондо", parent=shock, props=Sport("Тхэквондо", True, 7, 2, 2))
checkers = Node("Шашки", parent=personal_team, props=Sport("Шашки", False, 6, 2, 2))
golf = Node("Гольф", parent=personal_team, props=Sport("Гольф", False, 7, 2, 1))
billiards = Node("Бильярд", parent=personal_team, props=Sport("Бильярд", False, 8, 2, 1))
chess = Node("Шахматы", parent=personal_team, props=Sport("Шахматы", True, 6, 2, 2))
tennis = Node("Теннис", parent=personal_team, props=Sport("Теннис", True, 6, 2, 8))
table_tennis = Node("Настольный теннис", parent=personal_team, props=Sport("Настольный теннис", True, 6, 2, 4))
badminton = Node("Бадминтон", parent=personal_team, props=Sport("Бадминтон", True, 8, 2, 2))
rugby = Node("Регби", parent=team, props=Sport("Регби", False, 10, 15, 3))
hockey = Node("Хоккей", parent=team, props=Sport("Хоккей", True, 9, 20, 6))
football = Node("Футбол", parent=team, props=Sport("Футбол", True, 9, 11, 16))
handball = Node("Гандбол", parent=team, props=Sport("Гандбол", True, 9, 7, 1))
volleyball = Node("Волейбол", parent=team, props=Sport("Волейбол", True, 9, 6, 3))
water_polo = Node("Водное поло", parent=team, props=Sport("Водное поло", True, 9, 13, 2))
softball = Node("Софтбол", parent=team, props=Sport("Софтбол", True, 9, 9, 1))
baseball = Node("Бейсбол", parent=team, props=Sport("Бейсбол", True, 9, 9, 9))
basketball = Node("Баскетбол", parent=team, props=Sport("Баскетбол", True, 8, 5, 10))

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


# Меры близости
# Объявление структуры для хранения мер близости
class Proximity:
    euclid = 0
    tree = 0
    diffs = 0

    def __init__(self, e, t, d):
        self.euclid = e
        self.tree = t
        self.diffs = d

    def getLine(self):
        print("Euclid: %f\nTree: %i\nDiffs: %i" % (self.euclid, self.tree, self.diffs))

# Евклидово расстояние [0;2]
# Нормирование и формирование массива листьев для реализации перебора
max_min_age = 0
max_min_participant = 0
max_popularity = 0
min_min_age = math.inf
min_min_participant = math.inf
min_popularity = math.inf
sportArr = []
for node in PreOrderIter(root):
    if hasattr(node, 'props'):
        sportArr.append(node)
        if node.props.min_age > max_min_age:
            max_min_age = node.props.min_age
        if node.props.min_age < min_min_age:
            min_min_age = node.props.min_age
        if node.props.min_participants > max_min_participant:
            max_min_participant = node.props.min_participants
        if node.props.min_participants < min_min_participant:
            min_min_participant = node.props.min_participants
        if node.props.popularity > max_popularity:
            max_popularity = node.props.popularity
        if node.props.popularity < min_popularity:
            min_popularity = node.props.popularity
print("%d %d %d %d %d %d" % (max_min_age, max_min_participant, max_popularity, min_min_age, min_min_participant, min_popularity))

min_age_norm = max_min_age - min_min_age
def normalize_min_age(min_age):
    return (min_age - min_min_age) / min_age_norm

min_participant_norm = max_min_participant - min_min_participant
def normalize_min_participants(min_participants):
    return (min_participants - min_min_participant) / min_participant_norm

popular_norm = max_popularity - min_popularity
def normalize_popularity(popular):
    return (popular - max_popularity) / popular_norm

#### Реализация функции Евклидового расстояния
def euclid(vec1, vec2):
    x1 = normalize_min_age(vec1.min_age)
    x2 = normalize_min_age(vec2.min_age)
    y1 = normalize_min_participants(vec1.min_participants)
    y2 = normalize_min_participants(vec2.min_participants)
    z1 = normalize_popularity(vec1.popularity)
    z2 = normalize_popularity(vec2.popularity)

    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)

## Количество отличий в общем [0;6]
def diffs(vec1, vec2):
    dif = 0
    # pricePerGramm1 = vec1.price / vec1.weight
    # pricePerGramm2 = vec2.price / vec2.weight

    # Считаем, что есть разница между чаями с разницей более чем 3 рубля за грамм
    # if abs(pricePerGramm1 - pricePerGramm2) > 3:
    #     dif += 1

    # Считаем, что есть разница между чаями с разницей весов более 20 грамм
    if abs(vec1.min_age - vec2.min_age) != 0:
        dif += 1

    if abs(vec1.min_participants - vec2.min_participants) != 0:
        dif += 1

    if abs(vec1.popularity - vec2.popularity) != 0:
        dif += 1

    if vec1.olympic != vec2.olympic:
        dif += 1

    # if vec1.leafForm != vec2.leafForm:
    #     dif += 1

    return dif

## Близость по дереву [0;5]
def prox(node1, node2):
    pars1 = []
    pars2 = []

    tmp = node1
    while tmp != None:
        pars1.append(tmp)
        tmp = tmp.parent

    tmp = node2
    while tmp != None:
        pars2.append(tmp)
        tmp = tmp.parent

    for i in range(1, len(pars1)):
        for j in range(1, len(pars2)):
            if pars1[i] == pars2[j]:
                return max(i, j)

## Корреляция
min_ages = []
min_participants = []
popularity = []
olympic = []
# ferments = []
# leafForms = []

for i in range(1, len(sportArr)):
    min_ages.append(sportArr[i].props.min_age)
    min_participants.append(sportArr[i].props.min_participants)
    popularity.append(sportArr[i].props.popularity)
    olympic.append(sportArr[i].props.olympic)
    # ferments.append(sportArr[i].props.ferment)
    # leafForms.append(sportArr[i].props.leafForm)

cars = {'min_age': min_ages,
        'min_participants': min_participants,
        'popularity': popularity,
        'olympic': olympic,
        # 'ferment': ferments,
        # 'leafForm': leafForms
        }

df = pd.DataFrame(cars, columns = ['min_age', 'min_participants', 'popularity', 'olympic'])
df.corr()

## Составление коллекции мер близости
dictObj = {}


class Measure:
    first = None
    second = None
    euclid = None
    diffs = None
    treeProx = None

    def __init__(self, first, second, euclid, diffs, treeProx):
        self.first = first
        self.second = second
        self.euclid = euclid
        self.diffs = diffs
        self.treeProx = treeProx

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=False, indent=4, ensure_ascii=False)

class Pairs:
    first = None
    second = None
    def __init__(self, f, s):
        self.first = f
        self.second = s


jsonArr = "["

for i in range(len(sportArr) - 2):
    for j in range(i + 1, len(sportArr) - 1):
        eucl = euclid(sportArr[i].props, sportArr[j].props)
        diffsAtAll = diffs(sportArr[i].props, sportArr[j].props)
        treeProx = prox(sportArr[i], sportArr[j])

        meas = Measure(sportArr[i].name, sportArr[j].name, float("{0:.3f}".format(eucl)), diffsAtAll, treeProx)
        jsonArr += meas.toJSON()
        jsonArr += ","

jsonArr += "]"
print(jsonArr)

with open("measures.json", "w", encoding="utf-8") as outfile:
    json.dump(jsonArr, outfile, ensure_ascii=False)
