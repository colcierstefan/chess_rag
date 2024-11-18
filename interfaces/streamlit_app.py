import streamlit as st
from typing import List
from services.rag_service import RAGService
from utils.display import DisplayManager
from data.chess_data import GAMES
import os
from dotenv import load_dotenv


class ChessRAGUI:
    def __init__(self):
        """Initialize the Streamlit UI components."""
        self.set_page_config()
        self.initialize_session_state()
        self.rag_service = self.get_rag_service()
        self.display = DisplayManager()

    @staticmethod
    def set_page_config():
        """Configure the Streamlit page."""
        st.set_page_config(
            page_title="Chess Master Analysis ♟️",
            page_icon="♟️",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        # Add minimal required CSS
        st.markdown("""
            <style>
                footer {visibility: hidden;}
                .block-container {padding-top: 1rem; padding-bottom: 1rem;}
            </style>
            """, unsafe_allow_html=True)


    @staticmethod
    def initialize_session_state():
        """Initialize session state variables."""
        if 'initialized' not in st.session_state:
            st.session_state.initialized = False
            st.session_state.games_loaded = False
            st.session_state.rag_service = None
            st.session_state.current_context = None
            st.session_state.analysis_done = False
            st.session_state.chat_history = []
            st.session_state.current_analysis_type = None
            st.session_state.should_clear_input = False

    def get_rag_service(self) -> RAGService:
        """Get or create RAG service instance."""
        if not st.session_state.initialized:
            load_dotenv()
            st.session_state.rag_service = RAGService()
            st.session_state.initialized = True
        return st.session_state.rag_service

    def load_games(self):
        """Load games into the RAG service."""
        if not st.session_state.games_loaded and self.rag_service:
            with st.spinner("♟️ Loading chess games..."):
                self.rag_service.ingest_games(GAMES)
                st.session_state.games_loaded = True

    def add_to_chat_history(self, role: str, content: str, sources: List = None):
        """Add a message to the chat history."""
        message = {
            'role': role,
            'content': content,
            'sources': sources if sources else []
        }
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []
        st.session_state.chat_history.append(message)

    def display_chat_history(self):
        """Display the chat history."""
        for message in st.session_state.chat_history:
            if message['role'] == 'user':
                st.markdown("🧑‍💻 **You:**")
                st.markdown(message['content'])
            else:
                st.markdown("🤖 **Assistant:**")
                st.markdown(message['content'])
                if message.get('sources'):
                    st.markdown("📚 **Referenced Games:**")
                    for source in message['sources']:
                        event = source['event'].split(',')[0].strip().split('Game')[0].strip()
                        st.markdown(f"♟️ {source['players']} ({source['year']}, {event})")
            st.markdown("---")

    def render_chat_interface(self):
        """Render the chat interface."""
        # Header container with padding
        header_container = st.container()
        # Main chat container
        main_container = st.container()
        # Input container
        input_container = st.container()

        # Header
        with header_container:
            st.markdown("#")  # Add some spacing
            st.markdown("### Chess Analysis Chat")
            st.markdown("---")

        # Input area container at the bottom
        with input_container:
            st.markdown("---")
            col1, col2, col3 = st.columns([3, 1, 1])

            with col1:
                if st.session_state.should_clear_input:
                    st.session_state.query_input = ""
                    st.session_state.should_clear_input = False

                query = st.text_area(
                    "Your question",
                    key="query_input",
                    placeholder="Ask your question here...",
                    height=100,
                    label_visibility="collapsed"
                )

            with col2:
                submit = st.button("Ask Question 🎯", use_container_width=True)
            with col3:
                clear = st.button("Clear Chat 🗑️", use_container_width=True)

            if submit and query:
                self.process_query(query)
                st.session_state.should_clear_input = True
                st.rerun()

            if clear:
                st.session_state.chat_history = []
                st.session_state.should_clear_input = True
                st.rerun()

        # Display chat history in the main container
        with main_container:
            if st.session_state.chat_history:
                for message in st.session_state.chat_history:
                    if message['role'] == 'user':
                        st.markdown("🧑‍💻 **You:**")
                        st.markdown(message['content'])
                    else:
                        st.markdown("🤖 **Assistant:**")
                        st.markdown(message['content'])
                        if message.get('sources'):
                            st.markdown("📚 **Referenced Games:**")
                            for source in message['sources']:
                                event = source['event'].split(',')[0].strip().split('Game')[0].strip()
                                st.markdown(f"♟️ {source['players']} ({source['year']}, {event})")
                    st.markdown("---")
            else:
                st.markdown("Start a conversation by selecting an analysis type from the sidebar!")

    def process_query(self, query: str):
        """Process the user's query."""
        if not query:
            st.warning("⚠️ Please enter a question")
            return

        self.add_to_chat_history('user', query)

        try:
            with st.spinner("🤔 Analyzing..."):
                if st.session_state.current_context:
                    context = st.session_state.current_context
                    if context['type'] == 'game':
                        query = f"Regarding the game {context['game_info']}: {query}"
                    else:
                        query = f"Regarding the {context['opening']} opening: {query}"

                response = self.rag_service.query(query)
                self.add_to_chat_history(
                    'assistant',
                    response["answer"],
                    response.get("sources", [])
                )

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    def display_welcome(self):
        """Display welcome message and app description."""
        st.sidebar.title("♟️ Chess Master Analysis")
        st.sidebar.markdown("#### AI-powered chess insights")

        st.sidebar.markdown("""
        Welcome! This tool helps you:
        * 🔍 Analyze famous games
        * 📚 Study openings
        * 🎯 Learn from grandmasters
        * 💡 Discover patterns
        """)

    def render_game_selector(self):
        """Render the game selector in sidebar."""
        st.sidebar.markdown("### 🎮 Select Game")
        games_info = {
            f"🏆 {game.white_player} vs {game.black_player} ({game.year}, {game.event})": game.game_id
            for game in GAMES
        }

        selected_game = st.sidebar.selectbox(
            "Choose a historical game",
            options=list(games_info.keys())
        )

        if st.sidebar.button("Analyze Selected Game"):
            game_id = games_info[selected_game]
            st.session_state.current_context = {
                'type': 'game',
                'game_id': game_id,
                'game_info': selected_game
            }
            st.session_state.chat_history = []
            self.handle_game_analysis(game_id)
            st.rerun()

    def render_opening_selector(self):
        """Render the opening selector in sidebar."""
        st.sidebar.markdown("### 📚 Select Opening")
        openings = sorted(set(game.opening for game in GAMES))
        selected_opening = st.sidebar.selectbox(
            "Choose an opening",
            options=[f"♟️ {opening}" for opening in openings]
        )

        if st.sidebar.button("Analyze Selected Opening"):
            opening = selected_opening.replace("♟️ ", "")
            st.session_state.current_context = {
                'type': 'opening',
                'opening': opening
            }
            st.session_state.chat_history = []
            self.handle_opening_analysis(opening)
            st.rerun()

    def render_analysis_type_selector(self):
        """Render the analysis type selector."""
        st.sidebar.markdown("### 📊 Analysis Type")
        analysis_type = st.sidebar.selectbox(
            "Select your analysis type",
            ["General Query 🔍", "Game Analysis 🎮", "Opening Analysis 📚"],
            key="analysis_type"
        )

        if analysis_type != st.session_state.current_analysis_type:
            st.session_state.current_analysis_type = analysis_type
            st.session_state.current_context = None
            st.session_state.chat_history = []
            st.session_state.analysis_done = False

        if "Game Analysis" in analysis_type:
            self.render_game_selector()
        elif "Opening Analysis" in analysis_type:
            self.render_opening_selector()

    def handle_game_analysis(self, game_id: str):
        """Handle game analysis submission."""
        try:
            with st.spinner("♟️ Analyzing game..."):
                response = self.rag_service.analyze_game(game_id)
                self.add_to_chat_history(
                    'assistant',
                    response["answer"],
                    response.get("sources", [])
                )
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.error("Please try again or refresh the page.")

    def handle_opening_analysis(self, opening: str):
        """Handle opening analysis submission."""
        try:
            with st.spinner("📚 Analyzing opening..."):
                response = self.rag_service.compare_openings(opening)
                self.add_to_chat_history(
                    'assistant',
                    response["answer"],
                    response.get("sources", [])
                )
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.error("Please try again or refresh the page.")

    def run(self):
        """Run the Streamlit application."""
        if not os.getenv("OPENAI_API_KEY"):
            st.error("🔑 Please set OPENAI_API_KEY environment variable")
            return

        try:
            # Sidebar
            self.display_welcome()
            self.load_games()
            self.render_analysis_type_selector()

            # Main chat interface
            self.render_chat_interface()

        except Exception as e:
            st.error(f"An error occurred during initialization: {str(e)}")
            st.error("Please refresh the page and try again.")
