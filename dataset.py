"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
  - TEST_POSTS: held-out posts the model has never trained on
  - TEST_LABELS: human labels for each post in TEST_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
    "wonderful",
    "fantastic",
    "proud",
    "grateful",
    "hopeful",
    "beautiful",
    "enjoy",
    "nice",
    "excellent",
    "perfect",
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
    "horrible",
    "anxious",
    "worst",
    "annoyed",
    "frustrated",
    "depressed",
    "miserable",
    "disappointing",
    "stuck",
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
    "Lowkey stressed but kind of proud of myself",
    "This is boring and I hate it",
    "Lol that was awesome no cap",
    "I am not sad about leaving actually",
    "Everything feels awful and I am so tired",
    "Had a great day with amazing friends",
    "Meh whatever I guess",
    "I absolutely love getting stuck in traffic",
    "Feeling relaxed and happy for once",
    "This is not bad at all",
]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",   # "I love this class so much"
    "negative",   # "Today was a terrible day"
    "mixed",      # "Feeling tired but kind of hopeful"
    "neutral",    # "This is fine"
    "positive",   # "So excited for the weekend"
    "negative",   # "I am not happy about this"
    "mixed",      # "Lowkey stressed but kind of proud of myself"
    "negative",   # "This is boring and I hate it"
    "positive",   # "Lol that was awesome no cap"
    "positive",   # "I am not sad about leaving actually"
    "negative",   # "Everything feels awful and I am so tired"
    "positive",   # "Had a great day with amazing friends"
    "neutral",    # "Meh whatever I guess"
    "negative",   # "I absolutely love getting stuck in traffic" (sarcasm)
    "positive",   # "Feeling relaxed and happy for once"
    "positive",   # "This is not bad at all"
]

# ---------------------------------------------------------------------
# Held-out test set (never used for training)
# ---------------------------------------------------------------------

# These posts are completely separate from SAMPLE_POSTS. The ML model
# should ONLY train on SAMPLE_POSTS/TRUE_LABELS and then be evaluated
# on TEST_POSTS/TEST_LABELS to measure real generalization.
TEST_POSTS = [
    "What an amazing sunset today",
    "I hate Mondays so much",
    "Not sure how I feel about this",
    "That movie was not great honestly",
    "Super fun hangout with the crew",
    "I am so angry right now",
    "It was okay nothing special",
    "Stressed about exams but excited to be almost done",
    "Oh wow what a great idea said no one ever",
    "Finally feeling good after a rough week",
    "This is the worst thing that has ever happened",
    "I guess it could be worse",
    "Highkey love this song it slaps",
    "Tired and sad and just want to sleep",
    "The food was bad but the company was great",
]

TEST_LABELS = [
    "positive",   # "What an amazing sunset today"
    "negative",   # "I hate Mondays so much"
    "neutral",    # "Not sure how I feel about this"
    "negative",   # "That movie was not great honestly"
    "positive",   # "Super fun hangout with the crew"
    "negative",   # "I am so angry right now"
    "neutral",    # "It was okay nothing special"
    "mixed",      # "Stressed about exams but excited to be almost done"
    "negative",   # "Oh wow what a great idea said no one ever" (sarcasm)
    "positive",   # "Finally feeling good after a rough week"
    "negative",   # "This is the worst thing that has ever happened"
    "neutral",    # "I guess it could be worse"
    "positive",   # "Highkey love this song it slaps"
    "negative",   # "Tired and sad and just want to sleep"
    "mixed",      # "The food was bad but the company was great"
]
