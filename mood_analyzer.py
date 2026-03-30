# mood_analyzer.py
"""
Rule based mood analyzer for short text snippets.

This class starts with very simple logic:
  - Preprocess the text
  - Look for positive and negative words
  - Compute a numeric score
  - Convert that score into a mood label
"""

from typing import List, Dict, Tuple, Optional

from dataset import POSITIVE_WORDS, NEGATIVE_WORDS


class MoodAnalyzer:
    """
    A very simple, rule based mood classifier.
    """

    def __init__(
        self,
        positive_words: Optional[List[str]] = None,
        negative_words: Optional[List[str]] = None,
    ) -> None:
        # Use the default lists from dataset.py if none are provided.
        positive_words = positive_words if positive_words is not None else POSITIVE_WORDS
        negative_words = negative_words if negative_words is not None else NEGATIVE_WORDS

        # Store as sets for faster lookup.
        self.positive_words = set(w.lower() for w in positive_words)
        self.negative_words = set(w.lower() for w in negative_words)

    # ---------------------------------------------------------------------
    # Preprocessing
    # ---------------------------------------------------------------------

    def preprocess(self, text: str) -> List[str]:
        """
        Convert raw text into a list of tokens the model can work with.

        TODO: Improve this method.

        Right now, it does the minimum:
          - Strips leading and trailing whitespace
          - Converts everything to lowercase
          - Splits on spaces

        Ideas to improve:
          - Remove punctuation
          - Handle simple emojis separately (":)", ":-(", "🥲", "😂")
          - Normalize repeated characters ("soooo" -> "soo")
        """
        cleaned = text.strip().lower()

        # Remove common punctuation from the text (but preserve emoji-like tokens)
        import re
        cleaned = re.sub(r"[.,!?;:\"'()\[\]{}]", " ", cleaned)

        # Normalize repeated characters ("soooo" -> "soo")
        cleaned = re.sub(r"(.)\1{2,}", r"\1\1", cleaned)

        tokens = cleaned.split()

        return tokens

    # ---------------------------------------------------------------------
    # Scoring logic
    # ---------------------------------------------------------------------

    def score_text(self, text: str) -> int:
        """
        Compute a numeric "mood score" for the given text.

        Positive words increase the score.
        Negative words decrease the score.

        TODO: You must choose AT LEAST ONE modeling improvement to implement.
        For example:
          - Handle simple negation such as "not happy" or "not bad"
          - Count how many times each word appears instead of just presence
          - Give some words higher weights than others (for example "hate" < "annoyed")
          - Treat emojis or slang (":)", "lol", "💀") as strong signals
        """
        tokens = self.preprocess(text)
        score = 0
        negation_words = {"not", "no", "never", "dont", "doesn", "isn", "wasn", "aren", "won"}

        for i, token in enumerate(tokens):
            # Check if the previous word is a negation word
            is_negated = i > 0 and tokens[i - 1] in negation_words

            if token in self.positive_words:
                score += -1 if is_negated else 1
            if token in self.negative_words:
                score += 1 if is_negated else -1

        return score

    # ---------------------------------------------------------------------
    # Label prediction
    # ---------------------------------------------------------------------

    def predict_label(self, text: str) -> str:
        """
        Turn the numeric score for a piece of text into a mood label.

        Logic:
          - If both positive and negative words appear -> "mixed"
          - score > 0  -> "positive"
          - score < 0  -> "negative"
          - score == 0 -> "neutral"
        """
        tokens = self.preprocess(text)
        score = self.score_text(text)

        has_positive = any(t in self.positive_words for t in tokens)
        has_negative = any(t in self.negative_words for t in tokens)

        if has_positive and has_negative:
            return "mixed"
        elif score > 0:
            return "positive"
        elif score < 0:
            return "negative"
        else:
            return "neutral"

    # ---------------------------------------------------------------------
    # Explanations (optional but recommended)
    # ---------------------------------------------------------------------

    def explain(self, text: str) -> str:
        """
        Return a short string explaining WHY the model chose its label.

        Shows which words were detected as positive or negative (including
        negation flips) and the final score and predicted label.
        """
        tokens = self.preprocess(text)
        negation_words = {"not", "no", "never", "dont", "doesn", "isn", "wasn", "aren", "won"}

        positive_hits: List[str] = []
        negative_hits: List[str] = []
        score = 0

        for i, token in enumerate(tokens):
            is_negated = i > 0 and tokens[i - 1] in negation_words

            if token in self.positive_words:
                if is_negated:
                    negative_hits.append(f"not {token}")
                    score -= 1
                else:
                    positive_hits.append(token)
                    score += 1
            if token in self.negative_words:
                if is_negated:
                    positive_hits.append(f"not {token}")
                    score += 1
                else:
                    negative_hits.append(token)
                    score -= 1

        label = self.predict_label(text)
        return (
            f"Score = {score}, Label = {label} "
            f"(positive: {positive_hits or '[]'}, "
            f"negative: {negative_hits or '[]'})"
        )
