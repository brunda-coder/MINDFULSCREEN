from .model_manager import ModelManager
from .nlp_processor import NLPProcessor

class AICore:
    """
    Main AI engine combining models, NLP, logic, and personalization.
    """

    def __init__(self):
        self.model_manager = ModelManager()
        self.nlp = NLPProcessor()

    def handle_input(self, text):
        analysis = self.nlp.process_text(text)
        response = self.nlp.generate_response(analysis)
        return response
