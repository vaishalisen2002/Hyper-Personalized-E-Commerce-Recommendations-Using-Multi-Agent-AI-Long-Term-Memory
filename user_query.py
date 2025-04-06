class UserQuery:
    def __init__(self, query: str):
        self.query = query

    def get_query(self) -> str:
        return self.query 