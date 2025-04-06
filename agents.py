from crewai import Agent
from sqlite_memory import SQLiteMemory

class ProfileAgent:
    def __init__(self, db: SQLiteMemory):
        self.db = db
        self.agent = Agent(
            role='Profile Analysis Expert',
            goal='Analyze user context and preferences',
            backstory='An expert at understanding user behavior and context from historical data',
            allow_delegation=False
        )

    def getUserContext(self) -> dict:
        context_data = self.db.executeSQL("SELECT * FROM user_context ORDER BY Customer_ID DESC LIMIT 1")
        return context_data[0] if context_data else {}

class ProductAgent:
    def __init__(self, db: SQLiteMemory):
        self.db = db
        self.agent = Agent(
            role='Product Recommendation Expert',
            goal='Find the most relevant products based on user query and context',
            backstory='An expert at matching products to user needs and preferences',
            allow_delegation=False
        )

    def getProducts(self, refined_query: str) -> list:
        # Adjust the query to use available columns
        products = self.db.executeSQL(f"""
            SELECT * FROM products 
            WHERE Category LIKE '%{refined_query}%' 
            OR Subcategory LIKE '%{refined_query}%'
        """)
        return products 