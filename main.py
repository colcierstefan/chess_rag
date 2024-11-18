import os
import streamlit as st
from dotenv import load_dotenv
from interfaces.streamlit_app import ChessRAGUI

def main():
    """
    Main entry point for the Chess RAG Streamlit application.
    """
    # Load environment variables
    load_dotenv()

    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        st.error("🔑 Please set OPENAI_API_KEY environment variable")
        st.stop()

    try:
        # Initialize and run the Streamlit UI
        ui = ChessRAGUI()
        ui.run()
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.error("Please check your configuration and try again.")

if __name__ == "__main__":
    main()