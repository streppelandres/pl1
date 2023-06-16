from entities.card import Card


def create_board_with_cards(screen, cards: list[Card]) -> list:
    rows = int(len(cards) ** 0.5)
    columns = len(cards) // rows

    board, index = [], 0
    for i in range(rows):
        row = []
        for j in range(columns):
            card: Card = cards[index]
            card.set_position(i * card.surface.get_width(),
                              j * card.surface.get_height())
            card.face_toogle(screen, False)
            card.draw(screen)
            row.append(card)
            index += 1
        board.append(row)

    return board
