from config import gameplay_cfg

# FIXME: No idea where to put these things, so i made this class, maybe i can add more stuff or the core of the game here
class Game:
    def __init__(self) -> None:
        self.last_card_id = None
        self.attempts_left = gameplay_cfg.MAX_ATTEMPTS
