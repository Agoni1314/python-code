'''import pygame
import random
import heapq
from collections import deque

# 初始化pygame
pygame.init()

# 游戏常量
CELL_SIZE = 30
GRID_WIDTH = 20  # 网格列数
GRID_HEIGHT = 15  # 网格行数
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT
FPS = 10  # 游戏帧率

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

# 方向常量
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Snake:
    def __init__(self):
        # 初始位置（中间）
        self.body = deque()
        start_x = GRID_WIDTH // 2
        start_y = GRID_HEIGHT // 2
        self.body.append((start_x, start_y))
        self.body.append((start_x - 1, start_y))
        self.body.append((start_x - 2, start_y))

        self.direction = RIGHT  # 初始方向向右
        self.next_direction = RIGHT  # 预存的下一个方向
        self.grow = False  # 是否需要增长
        self.ai_mode = False  # 是否AI模式

    def update_direction(self):
        """更新移动方向"""
        self.direction = self.next_direction

    def set_direction(self, new_direction):
        """设置新方向（防止180度转向）"""
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.next_direction = new_direction

    def move(self):
        """移动蛇身"""
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)

        # 添加新头部
        self.body.appendleft(new_head)

        # 如果不需要增长，移除尾部
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def check_collision(self):
        """检查是否碰撞（墙壁或自身）"""
        head = self.body[0]
        # 墙壁碰撞
        if (head[0] < 0 or head[0] >= GRID_WIDTH or
                head[1] < 0 or head[1] >= GRID_HEIGHT):
            return True
        # 自身碰撞
        if head in list(self.body)[1:]:
            return True
        return False

    def get_head_position(self):
        """返回头部位置"""
        return self.body[0]

    def get_body_positions(self):
        """返回身体所有位置"""
        return list(self.body)


class Food:
    def __init__(self, snake_body):
        self.position = self.generate_position(snake_body)

    def generate_position(self, snake_body):
        """生成不在蛇身上的食物位置"""
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in snake_body:
                return (x, y)

    def respawn(self, snake_body):
        """重新生成食物位置"""
        self.position = self.generate_position(snake_body)


class AStar:
    @staticmethod
    def manhattan_distance(pos1, pos2):
        """曼哈顿距离（启发函数）"""
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    @staticmethod
    def get_neighbors(pos, grid_width, grid_height, obstacles):
        """获取有效邻居位置"""
        neighbors = []
        x, y = pos
        # 四个方向
        directions = [RIGHT, LEFT, UP, DOWN]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 检查是否在网格内且不是障碍物
            if (0 <= nx < grid_width and 0 <= ny < grid_height and
                    (nx, ny) not in obstacles):
                neighbors.append((nx, ny))
        return neighbors

    @staticmethod
    def find_path(start, end, grid_width, grid_height, obstacles):
        """A*算法寻找路径"""
        # 优先队列：(f_score, g_score, 当前位置, 路径)
        open_heap = []
        heapq.heappush(open_heap, (0, 0, start, [start]))

        # 已访问节点及其最小g_score
        visited = {start: 0}

        while open_heap:
            f_score, g_score, current, path = heapq.heappop(open_heap)

            # 到达目标
            if current == end:
                return path[1:]  # 去掉起点

            # 探索邻居
            for neighbor in AStar.get_neighbors(current, grid_width, grid_height, obstacles):
                new_g = g_score + 1
                # 如果未访问或找到更优路径
                if neighbor not in visited or new_g < visited.get(neighbor, float('inf')):
                    visited[neighbor] = new_g
                    h_score = AStar.manhattan_distance(neighbor, end)
                    f_score = new_g + h_score
                    new_path = path.copy()
                    new_path.append(neighbor)
                    heapq.heappush(open_heap, (f_score, new_g, neighbor, new_path))

        return None  # 找不到路径


def draw_grid(screen):
    """绘制网格线"""
    for x in range(0, SCREEN_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, SCREEN_HEIGHT), 1)
    for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (SCREEN_WIDTH, y), 1)


def draw_snake(screen, snake):
    """绘制蛇"""
    # 绘制身体
    for i, (x, y) in enumerate(snake.get_body_positions()):
        rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1)
        if i == 0:  # 头部
            pygame.draw.rect(screen, BLUE, rect)
        else:  # 身体
            pygame.draw.rect(screen, GREEN, rect)


def draw_food(screen, food):
    """绘制食物"""
    x, y = food.position
    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1)
    pygame.draw.rect(screen, RED, rect)


def draw_info(screen, score, ai_mode):
    """绘制分数和模式信息"""
    font = pygame.font.SysFont(None, 24)
    score_text = font.render(f"分数: {score}", True, WHITE)
    mode_text = font.render(f"模式: {'AI' if ai_mode else '手动'}", True, WHITE)

    screen.blit(score_text, (10, SCREEN_HEIGHT + 10))
    screen.blit(mode_text, (SCREEN_WIDTH - 120, SCREEN_HEIGHT + 10))


def main():
    # 创建游戏窗口（包含信息栏）
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + 40))
    pygame.display.set_caption("贪吃蛇 (A*算法)")
    clock = pygame.time.Clock()

    # 初始化游戏对象
    snake = Snake()
    food = Food(snake.get_body_positions())
    score = 0
    game_over = False
    ai_path = []  # AI路径

    while not game_over:
        # 事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                # 空格键切换AI模式
                if event.key == pygame.K_SPACE:
                    snake.ai_mode = not snake.ai_mode
                    ai_path = []  # 切换模式时清空路径
                # 手动模式下处理方向键
                elif not snake.ai_mode:
                    if event.key == pygame.K_UP:
                        snake.set_direction(UP)
                    elif event.key == pygame.K_DOWN:
                        snake.set_direction(DOWN)
                    elif event.key == pygame.K_LEFT:
                        snake.set_direction(LEFT)
                    elif event.key == pygame.K_RIGHT:
                        snake.set_direction(RIGHT)

        # AI模式下自动寻路
        if snake.ai_mode:
            # 如果没有路径或路径走完，重新计算
            if not ai_path:
                start = snake.get_head_position()
                end = food.position
                obstacles = snake.get_body_positions()[1:]  # 排除头部的身体作为障碍物
                ai_path = AStar.find_path(start, end, GRID_WIDTH, GRID_HEIGHT, obstacles)

            # 按照路径移动
            if ai_path:
                next_pos = ai_path[0]
                head_x, head_y = snake.get_head_position()
                dx = next_pos[0] - head_x
                dy = next_pos[1] - head_y
                snake.set_direction((dx, dy))
                ai_path.pop(0)  # 移除已执行的步骤

        # 更新蛇的方向和位置
        snake.update_direction()
        snake.move()

        # 检查是否吃到食物
        if snake.get_head_position() == food.position:
            snake.grow = True
            score += 10
            food.respawn(snake.get_body_positions())
            ai_path = []  # 食物被吃后重新计算路径

        # 检查碰撞
        if snake.check_collision():
            game_over = True

        # 绘制游戏元素
        screen.fill(BLACK)
        draw_grid(screen)
        draw_snake(screen, snake)
        draw_food(screen, food)
        draw_info(screen, score, snake.ai_mode)
        pygame.display.flip()

        # 控制帧率
        clock.tick(FPS)

    # 游戏结束提示
    font = pygame.font.SysFont(None, 48)
    game_over_text = font.render(f"游戏结束! 分数: {score}", True, RED)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(3000)  # 显示3秒后退出

    pygame.quit()


if __name__ == "__main__":
    main()'''


'''m=input('请输入一个数')
m=int(m)
while True:
    print(f'数字是{m}')
    if m<=0:
        break
    m = m - 1'''


'''for i in range(1,10):
    for j in range(1,i+1):
        print(f'{i}*{j}={i*j}',end=' ')
    print()'''





