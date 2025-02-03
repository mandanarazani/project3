import streamlit as st
import requests
from bs4 import BeautifulSoup
from groq import Groq
 
# Add images for branding
st.image("assets/Untitled17_20250113001924.png", width=400)
st.sidebar.image("assets/reshot-icon-flowers-in-the-branch-QXUYA35D8W.svg", width=180)
 
# Sidebar navigation
page = st.sidebar.radio("", ["About", "Shop", "ChatBot"])
 
if page == "About":
    st.title("SAKURA Online Shop")
    st.write("Welcome to our world!")
 
elif page == "Shop":
    st.title("Shop Page")
    st.write("Welcome to our Shop! Choose a category:")

    # Category selection
    category = st.selectbox("", ["Lipstick", "Sunscreen", "Perfume"])

    if category == "Lipstick":
        st.subheader("Lipstick Collection")
        st.write("Explore our range of high-quality lipsticks!")

        # Static lipstick products
        products = [
            {"name": "Rouge Dior Ultra Rouge", "price": "$37", "image": "assets/lipstick1.png"},
            {"name": "Dior Addict Lipstick", "price": "$35", "image": "assets/lipstick2.png"},
            {"name": "Diorific Lipstick", "price": "$40", "image": "assets/lipstick3.png"},
        ]

        # Display lipstick products
        for product in products:
            st.image(product["image"], width=200)
            st.write(f"**{product['name']}**")
            st.write(f"Price: {product['price']}")
            st.markdown("---")

    elif category == "Sunscreen":
        st.subheader("Sunscreen Collection")
        st.write("Choose from a variety of sunscreens for perfect protection!")

        # Static sunscreen products
        products = [
            {"name": "Ultra Defense SPF 50+", "price": "$25", "image": "assets/sunscreen1.png"},
            {"name": "Mineral Sunscreen SPF 30", "price": "$20", "image": "assets/sunscreen2.png"},
            {"name": "Sheer Face Sunscreen SPF 60", "price": "$30", "image": "assets/sunscreen3.png"},
        ]

        # Display sunscreen products
        for product in products:
            st.image(product["image"], width=200)
            st.write(f"**{product['name']}**")
            st.write(f"Price: {product['price']}")
            st.markdown("---")

    elif category == "Perfume":
        st.subheader("Perfume Collection")
        st.write("Discover our fragrant perfumes for every occasion!")

        # Static perfume products
        products = [
            {"name": "Jasmine Bliss", "price": "$50", "image": "assets/perfume1.png"},
            {"name": "Rose Elegance", "price": "$60", "image": "assets/perfume2.png"},
            {"name": "Citrus Zest", "price": "$45", "image": "assets/perfume3.png"},
        ]

        # Display perfume products
        for product in products:
            st.image(product["image"], width=200)
            st.write(f"**{product['name']}**")
            st.write(f"Price: {product['price']}")
            st.markdown("---")


        
elif page == "ChatBot":
    st.title("ChatBot Page")
    st.write("Chat with the bot here!")



    # Initialize Groq client
    client = Groq(api_key="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")

    # Default model - update this with the correct model name
    model = "gemma2-9b-it"

    # Initialize conversation history if not in session state
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

    # Display the chat history
    st.title("ChatBot Page")
    st.write("Chat with the bot here!")

    # Display existing chat messages
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    # Handle user input
    if prompt := st.chat_input("Ask something..."):
        # Add user message to session state
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)  # Display user message

        # Send the conversation history to the Groq API
