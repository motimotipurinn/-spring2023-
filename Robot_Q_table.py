import numpy as np


class Q_table:
    def __init__(self, maze):
        self.maze = maze
        row, col = self.maze.board_size()
        self.num_state = row * col * 7
        self.num_action = 4
        self.object_num = 0
        self.point = 0
        self.Q = np.zeros((self.num_state, self.num_action))
        self.state = self.get_state()

    def select_best_action(self):
        return self.Q[self.state, :].argmax()

    def select_action(self, random_rate):
        if np.random.rand() < random_rate:
            return np.random.randint(self.num_action)
        return self.select_best_action()

    def get_state(self):
        _, col = self.maze.board_size()
        x, y = self.maze.get_position()
        z = self.maze.get_object_num()
        # print(z)
        return (x * col + y) * (z + 1)

    def reward(self):
        # print(self.point)
        if self.maze.is_Black() and self.maze.can_get_object:
            self.maze.remove_object()
            self.point += 20
            self.maze.add_object_num()
            return 20
        elif self.maze.is_Red() and self.maze.can_get_object:
            self.maze.remove_object()
            self.point += 10
            self.maze.add_object_num()
            return 10
        elif self.maze.is_Cyan() and self.maze.can_get_object:
            self.maze.remove_object()
            self.maze.add_object_num()
            self.point += 15
            return 15
        elif self.maze.is_X():
            re = -100 * self.maze.get_object_num()
            self.point += int(re // 10)
            self.maze.reset_object_num()
            return re
        elif self.maze.is_Y():
            return -1 * self.maze.get_object_num()
        elif self.maze.is_wall():
            return -3
        elif self.maze.is_Deposit():
            re = 15 * self.maze.get_object_num()
            self.point += int(re)
            self.maze.reset_object_num()
            return re
        else:
            return -3

    def from_start(self, board, step):
        self.point = 0
        self.maze.reset(board, step)
        self.state = self.get_state()

    def get_result(self):
        return self.point

    def get_maze(self):
        return self.maze.board

    def step(self, learning_rate, discount_rate, random_rate):
        action = self.select_action(random_rate)
        self.maze.move(action)
        next_state = self.get_state()
        # print(next_state)
        next_action = self.select_best_action()
        self.Q[self.state][action] += learning_rate * (
            self.reward()
            + discount_rate * self.Q[next_state][next_action]
            - self.Q[self.state][action]
        )
        self.state = next_state
