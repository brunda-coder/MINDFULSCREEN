class NLPProcessor:
    """
    Natural language understanding + generation system.
    """

    def process_text(self, text):
        return {"intent": "unknown", "entities": {}, "raw_text": text}

    def generate_response(self, context):
        return "Etherea is thinking... vruuu 🌀"
