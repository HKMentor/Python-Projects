import chainlit as cl 

# Jab chat start ho to welcome message aur terms bhejo
@cl.on_chat_start
async def start():
    await cl.Message(
        content="👋 Assalamu Alaikum! Welcome to **HK Chatbot**! 😊\n\n"
                "**💡 Aap mujh se in topics par baat kar sakte hain:**\n"
                "- Salam aur greetings 🤝\n"
                "- Aap ki hal chal / How are you? 😊\n"
                "- Mujhe kisne banaya? 👩‍💻\n"
                "- Alvida kehna (Goodbye) 👋\n\n"
                "**🚫 Avoid in this  topics par baat na karein:**\n"
                "- Ghaliz alfaaz ya badtameezi 🚫\n"
                "- Ghair zaroori sawal ya spam ⚠️\n\n"
                "Mujh se Urdu aur English dono mein baat kar sakte hain. Try it now! 🚀"
    ).send()

# Jab user koi message bheje to chatbot jawab dega
@cl.on_message
async def chat(message: cl.Message):
    user_input = message.content.lower()

    if any(word in user_input for word in ["salam", "hello", "hi", "assalamu alaikum"]):
        response = "🤗 Walaikum Assalam! Aap kaise hain? / How are you?"

    elif any(word in user_input for word in ["kase ho", "kesi ho", "kese hain", "ap kese hain"]):
        response = "Main theek hoon, aap batao? 😊"

    elif any(word in user_input for word in ["yes i am fine", "me bhi thik hun", "shukar hai allah ka", "thik hun yr", "han thik"]):
        response = "Oh that's good to hear! 😊"

    elif any(word in user_input for word in ["how are you", "how r u"]):
        response = "I am fine! What about you? 😊"

    elif any(word in user_input for word in ["tumhe kisne banaya", "apko kisne banaya", "who created you"]):
        response = "Mujhe **Hooria Khan** ne develop kiya hai! 😊"

    elif any(word in user_input for word in ["bye", "allah hafiz", "goodbye"]):
        response = "👋 Allah Hafiz! Phir milenge. / Goodbye! See you soon!"

    elif any(word in user_input for word in ["gali", "badtameezi", "abuse", "bakwas"]):
        response = "🚫 Maaf kijiye, lekin yahan tameez aur izzat zaroori hai. 😊"

    else:
        response = f"🤔 Hmm... {message.content}? Yeh samajh nahi aya! Kya aap kuch aur kehna chahtay hain? 😊"

    await cl.Message(content=response).send()
