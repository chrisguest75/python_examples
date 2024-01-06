import os
import json

class Document:
    def __init__(self, path: str):
        """Initializes the document with the given path."""
        self.path = path
        self.doc = self.load_json(self.path)
        self.words = self.extract_words(self.doc)


    def load_json(self, path: str):
        """Loads the words from the document."""
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")
        
        with open(path, "r") as f:
            text = f.read()
            doc = json.loads(text)

        return doc

    def extract_words(self, doc: dict):
        """Extracts the words from the document."""
        words = []
        for word in doc["results"]:
            alternatives = word["alternatives"]
            highest_confidence = max(alternatives, key=lambda x: x["confidence"])
            item = {}
            item["word"] = highest_confidence["content"]
            item["start_time"] = word["start_time"]
            item["end_time"] = word["end_time"]
            words.append(item)

        return words
