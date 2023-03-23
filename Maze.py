class Maze:
    """迷路問題"""

    def __init__(self, board):
        self.board = board
        # print(type(self.board[0][0]))
        self.row = len(board)
        self.col = len(board[0])
        self.start_pos = None
        self.goal_pos = None
        self.object_num = 0
        for i in range(self.row):
            for j in range(self.col):
                if self.board[i][j] == "S":
                    self.start_pos = (i, j)
        self.agent_pos = list(self.start_pos)

    def reset(self, board, step):
        """エージェントをスタートに戻す"""
        self.agent_pos = list(self.start_pos)
        self.board = board
        self.object_num = 0
        # print("Done reset", step)

    def get_position(self):
        """エージェントの位置を返す"""
        return tuple(self.agent_pos)

    def board_size(self):
        """盤面のサイズを返す"""
        return self.row, self.col

    def get_object_num(self):
        return self.object_num

    def reset_object_num(self):
        self.object_num = 0

    def add_object_num(self):
        if self.object_num <= 5:
            self.object_num += 1

    def move(self, action: int):
        x, y = self.agent_pos
        if action == 0 and self.board[x - 1][y] != "W":
            self.agent_pos[0] -= 1
        elif action == 1 and self.board[x + 1][y] != "W":
            self.agent_pos[0] += 1
        elif action == 2 and self.board[x][y - 1] != "W":
            self.agent_pos[1] -= 1
        elif action == 3 and self.board[x][y + 1] != "W":
            self.agent_pos[1] += 1

    def can_get_object(self) -> bool:
        return self.object_num <= 5

    def remove_object(self):
        x, y = self.agent_pos
        self.board[x][y] = " "

    def is_Deposit(self):
        x, y = self.agent_pos
        return self.board[x][y] == "D"

    def is_wall(self) -> bool:
        x, y = self.agent_pos
        return self.board[x][y] == "W"

    def is_Black(self) -> bool:
        x, y = self.agent_pos
        return self.board[x][y] == "B"

    def is_Red(self) -> bool:
        x, y = self.agent_pos
        return self.board[x][y] == "R"

    def is_Cyan(self) -> bool:
        x, y = self.agent_pos
        return self.board[x][y] == "C"

    def is_X(self) -> bool:
        x, y = self.agent_pos
        return self.board[x][y] == "X"

    def is_Y(self) -> bool:
        x, y = self.agent_pos
        return self.board[x][y] == "Y"

    def draw(self):
        """盤面を描画"""
        print("\x1b[0;0H")  # 画面クリア
        for i in range(self.row):
            for j in range(self.col):
                print(self.board[i][j] if [i, j] != self.agent_pos else "A", end="")
            print(" ")
