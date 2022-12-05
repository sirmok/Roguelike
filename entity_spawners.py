from entity import Actor
from components.ai import HostileEnemy
from components.fighter import Fighter


player = Actor(char="@", color=(255,255,255), name="Player", ai_cls=HostileEnemy, fighter= Fighter(30, 2, 5))

orc = Actor(char="o", color=(63,127,63), name="Orc", ai_cls=HostileEnemy, fighter= Fighter(10, 0, 2))
troll = Actor(char="T", color=(0,127,0), name="Troll", ai_cls=HostileEnemy, fighter= Fighter(16, 1, 4))