from user_query import UserQuery
from transformers import pipeline

class QueryParser:
    def __init__(self):
        # Initialize the pipeline with the API key
        self.nlp = pipeline("text-generation", model="gpt2", use_auth_token="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")

    def parseQuery(self, user_query: UserQuery) -> str:
        prompt = user_query.get_query()
        result = self.nlp(prompt, max_length=50)[0]
        refined_query = result['generated_text'].strip()
        return refined_query