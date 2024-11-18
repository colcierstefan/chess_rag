from typing import List, Dict
from models.chess_game import ChessGame

class DisplayManager:
    """Handles all display-related functionality."""

    @staticmethod
    def display_sources(sources: List[Dict]) -> None:
        """Displays source references in a clean format."""
        if sources:
            print("\nBased on games:")
            for source in sources:
                event = DisplayManager._clean_event_name(source['event'])
                print(f"• {source['players']} ({source['year']}, {event})")

    @staticmethod
    def _clean_event_name(event: str) -> str:
        """Cleans event name by removing redundant game references."""
        event = event.split(',')[0].strip()
        event = event.split('Game')[0].strip()
        return event

    @staticmethod
    def display_available_games(games: List[ChessGame]) -> None:
        """Displays list of available games."""
        print("\nAvailable games:")
        for game in games:
            print(f"{game.game_id}. {game.get_players_display()} ({game.year})")

    @staticmethod
    def display_available_openings(games: List[ChessGame]) -> None:
        """Displays list of available openings."""
        print("\nAvailable openings:")
        openings = sorted(set(game.opening for game in games))
        for opening in openings:
            print(f"• {opening}")

    @staticmethod
    def display_menu() -> None:
        """Displays the main menu."""
        print("\nAvailable modes:")
        print("1. General query - Ask any question about the chess games")
        print("2. Game analysis - Analyze a specific game")
        print("3. Opening comparison - Compare games with the same opening")
        print("4. Exit")