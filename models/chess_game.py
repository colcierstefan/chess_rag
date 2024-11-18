from dataclasses import dataclass

@dataclass
class ChessGame:
    """Represents a chess game with its metadata and moves."""
    game_id: str
    white_player: str
    black_player: str
    moves: str
    opening: str
    result: str
    year: int
    event: str

    def get_players_display(self) -> str:
        """Returns formatted string of players."""
        return f"{self.white_player} vs {self.black_player}"

    def get_summary(self) -> str:
        """Returns a summary of the game."""
        return f"{self.get_players_display()} ({self.year}, {self.event})"