import time
from Robot_Q_table import Q_table
from Maze import Maze
import matplotlib as mpl
import matplotlib.pyplot as plt

old_BOARD = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W   B     B     B    B             C       C W",
    "W     B     B      B   B      WDD    C     C W",
    "W                     R       WDD         C  W",
    "W              R  R           W         C    W",
    "W       R            WW                 WWWWWW",
    "W         R    R R   WW                      W",
    "W      R                                     W",
    "W           YYYYDD        WW    R    S       W",
    "W           YXXYDD        WW C               W",
    "W   C C     YXXYWWWW                  B      W",
    "W    R      YYYY       R     YYYY            W",
    "W  C    C       WW           YXXY        C   W",
    "W               WW  C        YXXY            W",
    "W      WW    C   C       C   YYYY     C   B  W",
    "W      WW      R   R         WWDD    C  R    W",
    "W            C   C       R    WWDD     C     W",
    "W                   R                        W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]
BOARD = []
for i in old_BOARD:
    BOARD.append(list(i))

EPISODE_MAX = 3000
STEP_MAX = 1000
LEARNING_RATE = 0.01
DISCOUNT_RATE = 0.95
SLEEP_TIME = 0.00001
maze = Maze(BOARD)
q_learn = Q_table(maze)
x = []
y = []
for episode in range(EPISODE_MAX):
    step = 0
    BOARD = []
    for i in old_BOARD:
        BOARD.append(list(i))
    q_learn.from_start(BOARD, episode)
    random_rate = 0.01 + 0.9 / (1 + episode)
    # print(q_learn.get_maze())
    while step < STEP_MAX:
        q_learn.step(LEARNING_RATE, DISCOUNT_RATE, random_rate)
        if episode <= 20:
            maze.draw()
        step += 1
        time.sleep(SLEEP_TIME)
    print("\x1b[K")
    point = q_learn.get_result()
    print(f"episode : {episode} point:{point}")
    x.append(episode)
    y.append(point)

plt.title("Q table")
plt.xlabel("episode")
plt.ylabel("point")
plt.plot(x, y, "b-")
plt.show()
