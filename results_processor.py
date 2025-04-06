from typing import List, Dict, Any
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

class ResultsProcessor:
    def __init__(self):
        self.llm = OpenAI()
        self.prompt_template = PromptTemplate(
            input_variables=["products", "context"],
            template="""
            Based on the user context and available products, generate a personalized response:
            
            User Context:
            {context}
            
            Available Products:
            {products}
            
            Generate a natural and helpful response recommending the most relevant products.
            """
        )

    def generateResponse(self, products: List[Dict[str, Any]], user_context: Dict[str, Any]) -> dict:
        prompt = self.prompt_template.format(
            products=str(products),
            context=str(user_context)
        )
        
        response = self.llm.predict(prompt)
        
        return {
            "response": response,
            "products": products,
            "user_context": user_context
        } 