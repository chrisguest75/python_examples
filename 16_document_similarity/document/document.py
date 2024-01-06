import os
import json

class Document:
    def __init__(self, path: str):
        """Initializes the document with the given path."""
        self.path = path
        self.doc = self.load_json(self.path)
        self.words = []


    def load_json(self, path: str):
        """Loads the words from the document."""
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")
        
        with open(path, "r") as f:
            text = f.read()
            doc = json.loads(text)


        pass    