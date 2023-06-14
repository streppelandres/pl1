from entities import card_helper


def init_board(screen, cards: list) -> any:
    rows = int(len(cards) ** 0.5)
    columns = len(cards) // rows
    print(f'[create_board] rows: {rows}, columns: {columns}')

    board = []
    index = 0
    for i in range(rows):
        row = []
        
        for j in range(columns):
            row.append(cards[index])
            card_helper.draw_card(screen, cards[index], i, j)
            index += 1
        
        board.append(row)

    return board
