from typing import List, Dict, Optional
from llama_index.core import VectorStoreIndex, ServiceContext
from llama_index.llms.openai import OpenAI
from models.chess_game import ChessGame
from services.document_service import DocumentService
from utils.prompt_templates import PromptTemplates


class RAGService:
    """Handles all RAG-related operations."""

    def __init__(self, model_name: str = "gpt-4o"):
        """Initialize the RAG system."""
        self.llm = OpenAI(model=model_name)
        self.service_context = ServiceContext.from_defaults(llm=self.llm)
        self.games: List[ChessGame] = []
        self.index: Optional[VectorStoreIndex] = None
        self.document_service = DocumentService()

    def ingest_games(self, games: List[ChessGame]) -> None:
        """Ingest chess games into the RAG system."""
        self.games = games
        documents = [self.document_service.create_document(game) for game in games]
        self.index = VectorStoreIndex.from_documents(
            documents,
            service_context=self.service_context
        )

    def query(self, question: str, mode: str = "default") -> Dict:
        """Query the RAG system."""
        if not self.index:
            return {"error": "No games have been ingested yet"}

        prompt_template = PromptTemplates.get_template(mode)
        query_engine = self.index.as_query_engine(
            service_context=self.service_context,
            streaming=True
        )

        response = query_engine.query(prompt_template.format(question=question))

        return self._process_response(response)

    def _process_response(self, response) -> Dict:
        """Process the RAG response and extract sources."""
        sources = []
        for node in response.source_nodes:
            metadata = node.metadata
            sources.append({
                "players": f"{metadata['white_player']} vs {metadata['black_player']}",
                "event": metadata['event'],
                "year": metadata['year']
            })

        return {
            "answer": str(response),
            "sources": sources
        }

    def analyze_game(self, game_id: str) -> Dict:
        """Analyze a specific game in detail."""
        game = self._find_game(game_id)
        if not game:
            return {"error": "Game not found"}

        query = self._create_game_analysis_query(game)
        return self.query(query, mode="analyze_game")

    def compare_openings(self, opening_name: str) -> Dict:
        """Compare different games with the same opening."""
        query = f"Compare and analyze different games that use the {opening_name} opening. What are the key variations and strategies?"
        return self.query(query, mode="compare_games")

    def _find_game(self, game_id: str) -> Optional[ChessGame]:
        """Find a game by its ID."""
        return next((g for g in self.games if g.game_id == game_id), None)

    def _create_game_analysis_query(self, game: ChessGame) -> str:
        """Create a query string for game analysis."""
        return f"""
        Analyze this specific game:
        White: {game.white_player}
        Black: {game.black_player}
        Event: {game.event}
        Year: {game.year}
        Opening: {game.opening}
        Moves: {game.moves}
        """