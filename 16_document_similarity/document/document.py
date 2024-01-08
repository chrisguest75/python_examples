import os
import json

class Document:
    def __init__(self, name: str = "memory", base: str = "memory"):
        self.name = name
        self.base = base
        self.path = ""
        self.doc = []
        self.words = []
        self.sentences = []

    def process_file(self, path: str):
        """Initializes the document with the given path."""
        self.base = path
        self.path = path
        self.doc = self.load_json(self.path)
        self.words = self.extract_words(self.doc)
        self.sentences = self.extract_sentences(self.words)

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
            item["speaker"] = highest_confidence["speaker"]
            item["type"] = word["type"]
            item["start_time"] = word["start_time"]
            item["end_time"] = word["end_time"]
            words.append(item)

        return words

    def extract_sentences(self, words: list):
        """Extracts the sentences from the document."""
        sentences = []
        sentence = []
        current_speaker = None
        for word in words:
            if current_speaker == None:
                current_speaker = word["speaker"]
            if word["speaker"] != current_speaker:
                current_speaker = word["speaker"]
                sentences.append(sentence)
                sentence = [word]
            elif word["word"] == ".":
                current_speaker = word["speaker"]
                current_speaker = None
                sentence.append(word)
                sentences.append(sentence)
                sentence = []
            else:
                sentence.append(word)

        sentences.append(sentence)
        return sentences

    @staticmethod
    def sentence_to_line(sentence: list, include_time=True) -> str:
        if len(sentence) == 0:
            return ""

        line = ""
        if include_time:
            start_time = sentence[0]["start_time"]
            end_time = sentence[-1]["end_time"]
            speaker = sentence[0]["speaker"]
            line = f"{start_time:0>9.3f} - {end_time:0>9.3f} {speaker} "

        start = ""
        for word in sentence:
            if word["type"] == "punctuation":
                line += word["word"]
            else:
                line += f"{start}{word['word']}"
            start = " "
        return line

    @staticmethod
    def sentence_by_sentence(document, add_headers=True, include_time=True) -> list:
        output = []
        if add_headers:
            output.append(f"Name: {document.name}")
            output.append(f"Base: {document.base}")
            output.append(f"File: {document.path}")

        for sentence in document.sentences:
            if len(sentence) == 0:
                continue
            line = Document.sentence_to_line(sentence, include_time)
            output.append(line)
        
        return output