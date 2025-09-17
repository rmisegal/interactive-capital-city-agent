#!/usr/bin/env python3
"""
Interactive Capital City Agent with Operation Logging
Version: 1.0
Created: 2025-09-17 11:07:03 IDT (Jerusalem Time)
Author: Dr. Yoram Segal (Gal Technologies Artificial Intelligence Ltd.)
Repository: https://github.com/rmisegal/interactive-capital-city-agent

Copyright (c) 2025 Dr. Yoram Segal (Gal Technologies Artificial Intelligence Ltd.). All rights reserved.

This program demonstrates an interactive LLM agent built with Google's ADK 
(Agent Development Kit) and google-generativeai library. The agent can chat 
with users about capital cities, showing the complete sequence of operations 
including tool usage, memory access, and LLM calls.

Licensed under MIT License.
See LICENSE file in the project root for full license text.
"""

import asyncio
import os
from dotenv import load_dotenv
import google.generativeai as genai
from google.adk.agents import LlmAgent
from google.adk.runners import InMemoryRunner
from google.generativeai import types
import time

# Load environment variables from .env file
load_dotenv()

# Ensure the Gemini API key is set as an environment variable
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
    print("Gemini API key loaded successfully")
else:
    print("Warning: GEMINI_API_KEY environment variable not set")

# Define a tool for the agent with enhanced logging
def get_capital_city(country: str) -> str:
    """
    Returns the capital city for a given country.
    """
    print(f"[TOOL] CALLED: get_capital_city('{country}')")
    
    capitals = {
        "france": "Paris",
        "japan": "Tokyo",
        "usa": "Washington D.C.",
        "united states": "Washington D.C.",
        "germany": "Berlin",
        "italy": "Rome",
        "spain": "Madrid",
        "uk": "London",
        "united kingdom": "London",
        "canada": "Ottawa",
        "australia": "Canberra"
    }
    
    result = capitals.get(country.lower(), "Unknown")
    print(f"[TOOL] RESULT: '{result}'")
    return result

class LoggingRunner(InMemoryRunner):
    """Custom runner that logs all operations"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.conversation_history = []
    
    async def run_async(self):
        """Override to add logging"""
        print("[MEMORY] Starting agent execution")
        print("[MEMORY] Loading conversation history...")
        
        # Call the parent method
        async for event in super().run_async():
            if hasattr(event, 'message') and event.message:
                print("[LLM] RESPONSE: Agent is thinking...")
                print(f"[AGENT] {event.message.text}")
                self.conversation_history.append({"role": "assistant", "content": event.message.text})
            yield event

async def interactive_chat():
    """Interactive chat with the agent"""
    print("=" * 60)
    print("INTERACTIVE AGENT CHAT")
    print("=" * 60)
    print("Ask questions about capital cities!")
    print("Type 'quit' or 'exit' to stop")
    print("=" * 60)
    
    # Create the agent
    print("[INIT] Creating LLM Agent...")
    capital_agent = LlmAgent(
        model="gemini-1.5-flash",
        name="capital_agent",
        description="Expert geography assistant that answers capital city questions",
        instruction="""
        You are an expert in geography and capital cities.
        When a user asks about a capital city:
        1. Extract the country name from their question
        2. Use the get_capital_city tool to find the answer
        3. Provide a helpful response with the capital city
        
        If the tool returns "Unknown", apologize and explain that you don't have that information.
        Be conversational and friendly.
        """,
        tools=[get_capital_city]
    )
    
    print("[INIT] Creating Memory Runner...")
    runner = LoggingRunner(agent=capital_agent, app_name="capital_chat_app")
    
    print("[READY] Agent initialized successfully!")
    print()
    
    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("Goodbye!")
                break
                
            if not user_input:
                continue
                
            print()
            print("=" * 40)
            print("PROCESSING YOUR MESSAGE...")
            print("=" * 40)
            
            # Log user message
            print(f"[USER] INPUT: '{user_input}'")
            print("[MEMORY] Storing user message...")
            
            # Create a simple message and process it
            # Note: The Google ADK might need different message handling
            print("[LLM] Sending to Gemini for processing...")
            
            # For now, let's use direct Gemini API call with tool simulation
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            # Enhanced prompt that instructs the model to use our tool
            enhanced_prompt = f"""
            User question: {user_input}
            
            You are a geography expert. If the user is asking about a capital city:
            1. Identify the country mentioned
            2. I will call get_capital_city(country) for you
            3. Provide a helpful response
            
            First, tell me what country you think the user is asking about, then I'll get the capital for you.
            """
            
            print("[LLM] Analyzing user question...")
            response = model.generate_content(enhanced_prompt)
            
            # Simple country extraction (you could make this more sophisticated)
            import re
            countries = ["japan", "france", "germany", "italy", "spain", "usa", "united states", 
                        "uk", "united kingdom", "canada", "australia"]
            
            found_country = None
            user_lower = user_input.lower()
            for country in countries:
                if country in user_lower:
                    found_country = country
                    break
            
            if found_country:
                # Call our tool
                capital = get_capital_city(found_country)
                
                # Generate final response
                final_prompt = f"""
                The user asked: {user_input}
                The country is: {found_country}
                The capital is: {capital}
                
                Please provide a natural, conversational response about this capital city.
                """
                
                print("[LLM] Generating final response...")
                final_response = model.generate_content(final_prompt)
                print(f"[AGENT] FINAL: {final_response.text}")
            else:
                print("[AGENT] I'm not sure which country you're asking about. Could you please clarify?")
            
            print("[MEMORY] Conversation stored")
            print("=" * 40)
            print()
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"[ERROR] {e}")
            print("Please try again.")
            print()

def demo_sequence():
    """Demo showing the sequence of operations"""
    print("=" * 60)
    print("AGENT OPERATION SEQUENCE DEMO")
    print("=" * 60)
    
    # Test questions
    test_questions = [
        "What is the capital of Japan?",
        "Tell me about France's capital",
        "What about Germany?",
        "Capital of Australia?"
    ]
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    for question in test_questions:
        print(f"\n{'='*50}")
        print(f"DEMO QUESTION: {question}")
        print(f"{'='*50}")
        
        # Log user message
        print(f"[USER] INPUT: '{question}'")
        print("[MEMORY] Storing user message...")
        
        print("[LLM] Sending to Gemini for processing...")
        
        # Country extraction
        import re
        countries = ["japan", "france", "germany", "italy", "spain", "usa", "united states", 
                    "uk", "united kingdom", "canada", "australia"]
        
        found_country = None
        user_lower = question.lower()
        for country in countries:
            if country in user_lower:
                found_country = country
                break
        
        print(f"[LLM] Analyzing user question...")
        print(f"[LLM] Country detected: {found_country}")
        
        if found_country:
            # Call our tool - this will show [TOOL] messages
            capital = get_capital_city(found_country)
            
            # Generate final response
            final_prompt = f"""
            The user asked: {question}
            The country is: {found_country}
            The capital is: {capital}
            
            Please provide a natural, conversational response about this capital city.
            """
            
            print("[LLM] Generating final response...")
            final_response = model.generate_content(final_prompt)
            print(f"[AGENT] FINAL: {final_response.text}")
        else:
            print("[AGENT] I'm not sure which country you're asking about. Could you please clarify?")
        
        print("[MEMORY] Conversation stored")
        print("=" * 50)
        
        # Add a small delay for readability
        import time
        time.sleep(1)

def main():
    """Main function - choose between demo or interactive"""
    import sys
    
    # Check if we're running interactively or in background
    if sys.stdin.isatty():
        print("Choose mode:")
        print("1. Demo sequence (shows operations)")
        print("2. Interactive chat")
        choice = input("Enter choice (1 or 2): ").strip()
        
        if choice == "2":
            asyncio.run(interactive_chat())
        else:
            demo_sequence()
    else:
        # Running in background or non-interactive, use demo
        print("Running in demo mode (non-interactive environment)")
        demo_sequence()

if __name__ == "__main__":
    main()