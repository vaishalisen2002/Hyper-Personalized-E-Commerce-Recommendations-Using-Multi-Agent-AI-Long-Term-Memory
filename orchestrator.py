from crewai import Crew, Process
from agents import ProfileAgent, ProductAgent
from query_parser import QueryParser
from results_processor import ResultsProcessor
from user_query import UserQuery
from sqlite_memory import SQLiteMemory

class Orchestrator:
    def __init__(self):
        self.db = SQLiteMemory()
        self.profile_agent = ProfileAgent(self.db)
        self.product_agent = ProductAgent(self.db)
        self.query_parser = QueryParser()
        self.results_processor = ResultsProcessor()

    def process_query(self, user_query: UserQuery) -> dict:
        # Create a crew for processing the query
        crew = Crew(
            agents=[self.profile_agent.agent, self.product_agent.agent],
            process=Process.sequential
        )

        # Parse the query
        refined_query = self.query_parser.parseQuery(user_query)

        # Get user context
        user_context = self.profile_agent.getUserContext()

        # Get relevant products
        products = self.product_agent.getProducts(refined_query)

        # Process results
        response = self.results_processor.generateResponse(products, user_context)

        return response 