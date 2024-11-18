from typing import Dict
from llama_index.core import Document
from models.chess_game import ChessGame


class DocumentService:
    """Handles document creation and formatting for the RAG system."""

    @staticmethod
    def create_document(game: ChessGame) -> Document:
        """Converts a chess game to a LlamaIndex Document."""
        text = DocumentService._create_document_text(game)
        metadata = DocumentService._create_metadata(game)
        return Document(text=text, metadata=metadata)

    @staticmethod
    def _create_document_text(game: ChessGame) -> str:
        """Creates the document text from a chess game."""
        return f"""
White Player: {game.white_player}
Black Player: {game.black_player}
Event: {game.event}
Year: {game.year}
Opening: {game.opening}
Result: {game.result}

Moves:
{game.moves}
"""

    @staticmethod
    def _create_metadata(game: ChessGame) -> Dict:
        """Creates metadata dictionary from a chess game."""
        return {
            "game_id": game.game_id,
            "white_player": game.white_player,
            "black_player": game.black_player,
            "opening": game.opening,
            "result": game.result,
            "year": game.year,
            "event": game.event
        }