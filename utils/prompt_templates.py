class PromptTemplates:
    """Collection of prompt templates for different query modes."""

    @staticmethod
    def get_template(mode: str) -> str:
        """Returns the appropriate template for the given mode."""
        templates = {
            "analyze_game": PromptTemplates.ANALYZE_GAME_TEMPLATE,
            "compare_games": PromptTemplates.COMPARE_GAMES_TEMPLATE,
            "default": PromptTemplates.DEFAULT_TEMPLATE
        }
        return templates.get(mode, PromptTemplates.DEFAULT_TEMPLATE)

    ANALYZE_GAME_TEMPLATE = """
    You are a chess expert analyzing games. Analyze this game focusing on:
    1. Key tactical moments and turning points
    2. Strategic themes and patterns
    3. Opening analysis and key variations
    4. Historical significance and context
    5. Learning points for players

    Provide your analysis without referring to game numbers or IDs in your response.

    Question: {question}
    """

    COMPARE_GAMES_TEMPLATE = """
    You are a chess expert comparing different games. Analyze:
    1. Common tactical patterns
    2. Similar strategic themes
    3. Opening variations and their effectiveness
    4. Historical connections between the games
    5. Evolution of playing styles

    Provide your analysis without referring to game numbers or IDs in your response.
    When referencing games, use player names and years instead.

    Question: {question}
    """

    DEFAULT_TEMPLATE = """
    You are a helpful chess expert. Provide a detailed answer using specific examples 
    from the games where relevant. When referencing games, use player names and years 
    instead of game numbers.

    Avoid mentioning game numbers or IDs in your response.

    Question: {question}
    """