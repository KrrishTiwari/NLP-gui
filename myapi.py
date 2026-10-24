import os
import nlpcloud
from dotenv import load_dotenv

load_dotenv()


class API:
    def __init__(self):
        api_token = os.getenv("NLPCLOUD_API_KEY")

        if not api_token:
            raise ValueError("NLPCLOUD_API_KEY is not set")

        self.sentiment_client = nlpcloud.Client(
            "distilbert-base-uncased-finetuned-sst-2-english", api_token
        )
        self.emotion_client = nlpcloud.Client(
            "distilbert-base-uncased-emotion", api_token
        )
        self.ner_client = nlpcloud.Client("en_core_web_lg", api_token)

    def _format_scores(self, response):
        return "\n".join(
            f"{item['label']}: {item['score']:.2f}"
            for item in response["scored_labels"]
        )

    def _run(self, text, func):
        if not text:
            return "Please enter some text"
        try:
            return func(text)
        except Exception as e:
            return f"Request failed: {e}"

    def sentiment(self, text):
        return self._run(
            text, lambda t: self._format_scores(self.sentiment_client.sentiment(t))
        )

    def emotion(self, text):
        return self._run(
            text, lambda t: self._format_scores(self.emotion_client.sentiment(t))
        )

    def ner(self, text):
        def work(t):
            entities = self.ner_client.entities(t)["entities"]
            if not entities:
                return "No entities found"
            return "\n".join(f"{e['text']}: {e['type']}" for e in entities)

        return self._run(text, work)



