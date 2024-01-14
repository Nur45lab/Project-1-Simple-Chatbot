#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class SimpleChatbot:
    def __init__(self):
        self.context = {}

    def greet(self):
        return "Hello! I'm your friendly chatbot. How can I help you today?"

    def farewell(self):
        return "Goodbye! If you have more questions, feel free to ask."

    def respond_to_question(self, question):
        if "how are you" in question:
            return "I'm just a computer program, but thanks for asking!"
        elif "your name" in question:
            return "I'm a chatbot, you can call me Simple Chatbot."
        elif "doing" in question:
            return "I'm here to assist you. What can I do for you today?"
        elif "weather" in question:
            return "I'm afraid I don't have real-time information. You can check a weather website for that."
        elif "tell me a joke" in question:
            return "Sure! Why don't scientists trust atoms? Because they make up everything!"

    def ask_user_questions(self):
        for i in range(3):
            user_response = input("Ask me something: ")
            self.context[f"question_{i+1}"] = user_response
            print(f"Interesting! You said: {user_response}")

    def handle_error(self):
        return "I'm sorry, I didn't quite understand that. Can you please rephrase or ask another question?"

if __name__ == "__main__":
    chatbot = SimpleChatbot()

    print(chatbot.greet())

    for _ in range(5):
        user_input = input("User: ")
        response = chatbot.respond_to_question(user_input)

        if response:
            print(f"Chatbot: {response}")
        else:
            print(f"Chatbot: {chatbot.handle_error()}")

    chatbot.ask_user_questions()

    print(chatbot.farewell())



# In[ ]:




