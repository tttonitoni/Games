import curses
import random
import time

SHAPES = {
    'I': [['....',
           '####',
           '....',
           '....'],
          ['..#.',
           '..#.',
           '..#.',
           '..#.']],
    'O': [['.##.',
           '.##.',
           '....',
           '....']],
    'T': [['....',
           '.###',
           '..#.',
           '....'],
          ['..#.',
           '.##.',
           '..#.',
           '....'],
          ['..#.',
           '.###',
           '....',
           '....'],
          ['..#.',
           '..##',
           '..#.',
           '....']],
    'S': [['....',
           '..##',
           '.##.',
           '....'],
          ['..#.',
           '..##',
           '...#',
           '....']],
    'Z': [['....',
           '.##.',
           '..##',
           '....'],
          ['..#.',
           '.##.',
           '.#..',
           '....']],
    'J': [['.#..',
           '.###',
           '....',
           '....'],
          ['..##',
           '..#.',
           '..#.',
           '....'],
          ['....',
           '.###',
           '...#',
           '....'],
          ['..#.',
           '..#.',
           '.##.',
           '....']],
    'L': [['...#',
           '.###',
           '....',
           '....'],
          ['..#.',
           '..#.',
           '..##',
           '....'],
          ['....',
           '.###',
           '.#..',
           '....'],
          ['.##.',
           '..#.',
           '..#.',
           '....']]
}

FIELD_WIDTH = 10
FIELD_HEIGHT = 20

def create_field():
    return [[' ' for _ in range(FIELD_WIDTH)] for _ in range(FIELD_HEIGHT)]

def collision(field, shape, x, y):
    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell == '#':
                if x + j < 0 or x + j >= FIELD_WIDTH or y + i >= FIELD_HEIGHT:
                    return True
                if y + i >= 0 and field[y + i][x + j] != ' ':
                    return True
    return False

def place_shape(field, shape, x, y):
    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell == '#':
                if 0 <= y + i < FIELD_HEIGHT and 0 <= x + j < FIELD_WIDTH:
                    field[y + i][x + j] = '#'

def clear_lines(field):
    new_field = [row for row in field if any(cell == ' ' for cell in row)]
    lines_cleared = FIELD_HEIGHT - len(new_field)
    while len(new_field) < FIELD_HEIGHT:
        new_field.insert(0, [' ' for _ in range(FIELD_WIDTH)])
    return new_field, lines_cleared

def draw_field(stdscr, field, score):
    for y, row in enumerate(field):
        for x, cell in enumerate(row):
            stdscr.addch(y, x*2, cell)
            stdscr.addch(y, x*2 + 1, cell)
    stdscr.addstr(0, FIELD_WIDTH * 2 + 2, f'Score: {score}')

def tetris(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(200)

    if curses.LINES < 22 or curses.COLS < 25:
        stdscr.addstr(0, 0, "Terminal zu klein! Bitte vergroessern.")
        stdscr.refresh()
        time.sleep(3)
        return

    field = create_field()
    score = 0

    current_shape_name = random.choice(list(SHAPES))
    current_shape = SHAPES[current_shape_name][0]
    rotation_index = 0
    x, y = 3, 0

    while True:
        stdscr.clear()

        for i, row in enumerate(current_shape):
            for j, cell in enumerate(row):
                if cell == '#' and y + i >= 0:
                    if 0 <= y + i < curses.LINES and 0 <= (x + j) * 2 + 1 < curses.COLS:
                        stdscr.addch(y + i, (x + j) * 2, '#')
                        stdscr.addch(y + i, (x + j) * 2 + 1, '#')

        draw_field(stdscr, field, score)
        stdscr.refresh()

        key = stdscr.getch()
        if key == ord('q'):
            break
        elif key == curses.KEY_LEFT and not collision(field, current_shape, x - 1, y):
            x -= 1
        elif key == curses.KEY_RIGHT and not collision(field, current_shape, x + 1, y):
            x += 1
        elif key == curses.KEY_DOWN and not collision(field, current_shape, x, y + 1):
            y += 1
        elif key == curses.KEY_UP:
            next_rotation = (rotation_index + 1) % len(SHAPES[current_shape_name])
            rotated = SHAPES[current_shape_name][next_rotation]
            if not collision(field, rotated, x, y):
                current_shape = rotated
                rotation_index = next_rotation

        if not collision(field, current_shape, x, y + 1):
            y += 1
        else:
            place_shape(field, current_shape, x, y)
            field, cleared = clear_lines(field)
            score += cleared * 100
            current_shape_name = random.choice(list(SHAPES))
            current_shape = SHAPES[current_shape_name][0]
            rotation_index = 0
            x, y = 3, 0
            if collision(field, current_shape, x, y):
                stdscr.addstr(10, 0, "Game Over!")
                stdscr.refresh()
                time.sleep(2)
                break

if __name__ == "__main__":
    curses.wrapper(tetris)