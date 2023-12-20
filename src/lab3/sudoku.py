import pathlib
import typing as tp
from random import randint

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """ Прочитать Судоку из указанного файла """
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку """
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    return 'Удобный вид'


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов
    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    return [[values.pop(0) for _ in range(n)] for _ in range(len(values) // n)]


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера строки, указанной в pos
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    return grid[pos[0]]


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    res = []
    for col in grid:
        res.append(col[pos[1]])
    return res


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения из квадрата, в который попадает позиция pos
    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    three_quadrant = [grid[index] for index in range(3)] if pos[0] < 3 else [grid[index] for index in range(3, 6)] if \
    pos[0] < 6 else [grid[index] for index in range(6, 9)]
    res = [col[:3] for col in three_quadrant] if pos[1] < 3 else [col[3:6] for col in three_quadrant] if pos[
                                                                                                             1] < 6 else [
        col[6:] for col in three_quadrant]
    return [*res[0], *res[1], *res[2]]


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for i in range(len(grid[0])):
        row = i
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                return (row, j)
    return 'End'


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """Вернуть множество возможных значения для указанной позиции
    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    """
    occupied_numbers = {}
    row_numbers = {elem for elem in get_row(grid, (pos[0], 0)) if elem != '.'}
    col_numbers = {elem for elem in get_col(grid, (0, pos[1])) if elem != '.'}
    block_numbers = {elem for elem in get_block(grid, pos) if elem != '.'}
    occupied_numbers = {*row_numbers, *col_numbers, *block_numbers}
    res = {'1', '2', '3', '4', '5', '6', '7', '8', '9'} - occupied_numbers
    return set(sorted(res))


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """ Решение пазла, заданного в grid """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла
    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    empty_exists = find_empty_positions(grid)
    if empty_exists == 'End':
        return grid
    else:
        for i in find_possible_values(grid, pos=empty_exists):
            grid[empty_exists[0]][empty_exists[1]] = str(i)
            if isinstance(solve(grid), list):
                return grid
            grid[empty_exists[0]][empty_exists[1]] = '.'


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False """
    # TODO: Add doctests with bad puzzles
    for row in range(len(solution)):
        for col in range(len(solution[row])):
            if (get_col(solution, (row, col)).count(solution[row][col]) == 1) and (
                    get_row(solution, (row, col)).count(solution[row][col]) == 1) and (
                    get_block(solution, (row, col)).count(solution[row][col]) == 1) and (solution[row][col] != '.'):
                pass
            else:
                return False
    return True


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """Генерация судоку заполненного на N элементов
    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """
    # generate empty sudoku place
    sudoku = [['.' for i in range(9)] for i in range(9)]
    # receiving the random positions in sukodu place for possibility make random sudoku in next step(generate
    # solution sudoku)
    list_pos = [(randint(0, 8), randint(0, 8)) for i in range(randint(3, 5))]
    for pos in list_pos:
        sudoku[pos[0]][pos[1]] = str(randint(1, 9))
    # generate solution sudoku
    sudoku = solve(sudoku)
    list_pos = [(x, y) for x in range(0, 9) for y in range(0, 9)]
    count = 80
    # filling dots in random places
    for i in range(81 - N):
        pos_number = randint(0, count)
        sudoku[list_pos[pos_number][0]][list_pos.pop(pos_number)[1]] = '.'
        count -= 1

    return sudoku


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        fname = f"{fname}"
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
            print(':(')
        else:
            display(solution)
