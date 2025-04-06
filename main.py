import os
from dotenv import load_dotenv
from user_query import UserQuery
from orchestrator import Orchestrator

# Load environment variables
load_dotenv('project.env')

def main():
    # Ensure OpenAI API key is set
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("Please set OPENAI_API_KEY in your environment variables")

    # Initialize the orchestrator
    orchestrator = Orchestrator()

    # Example query
    query = UserQuery("I need a comfortable office chair for long working hours")
    
    # Process the query
    result = orchestrator.process_query(query)
    
    # Print the response
    print("Response:", result["response"])
    print("\nRecommended Products:", result["products"])
    print("\nUser Context Used:", result["user_context"])

if __name__ == "__main__":
    main() 