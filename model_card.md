# Model Card: Mood Machine

This model card is for the Mood Machine project, which includes **two** versions of a mood classifier:

1. A **rule based model** implemented in `mood_analyzer.py`
2. A **machine learning model** implemented in `ml_experiments.py` using scikit learn

## 1. Model Overview

**Model type:**
I compared both models: the rule based model and the ML (logistic regression) model.

**Intended purpose:**
Classify short text messages (social media style posts) into mood labels: positive, negative, neutral, or mixed.

**How it works (brief):**
The rule based model tokenizes text, looks up each word in positive/negative word lists, and sums a score (+1 per positive word, -1 per negative word). It also handles negation: if a word like "not" or "never" appears before a sentiment word, the polarity flips. The final score maps to a label (positive if > 0, negative if < 0, neutral if 0).

The ML model uses scikit-learn's CountVectorizer to convert each post into a bag-of-words vector, then trains a logistic regression classifier on the labeled examples to learn the mapping from word counts to mood labels.

## 2. Data

**Dataset description:**
The dataset contains 16 short posts in `SAMPLE_POSTS`, each with a human-assigned label in `TRUE_LABELS`. The original starter had 6 posts; 10 new posts were added covering slang, sarcasm, negation, and mixed feelings.

**Labeling process:**
Labels were chosen based on the overall emotional tone a human reader would perceive. Some posts were intentionally hard to label:
- "Feeling tired but kind of hopeful" could be negative or mixed depending on the reader.
- "I absolutely love getting stuck in traffic" is sarcastic, so the true intent is negative despite positive words.
- "This is not bad at all" uses double negation to express a mildly positive sentiment.

**Important characteristics of your dataset:**
- Contains negated phrases ("not happy", "not sad", "not bad")
- Includes sarcasm ("I absolutely love getting stuck in traffic")
- Some posts express mixed feelings ("tired but hopeful", "stressed but proud")
- Contains slang ("lowkey", "no cap", "meh")
- Posts are short (5-10 words), similar to social media messages

**Possible issues with the dataset:**
- The dataset is very small (16 examples), making it easy for ML models to memorize rather than generalize.
- Label distribution is skewed: more positive and negative examples than neutral or mixed.
- Only English text is represented; no multilingual or dialect variation.
- Sarcasm is underrepresented (only 1 example).

## 3. How the Rule Based Model Works (if used)

**Your scoring rules:**
- Each positive word adds +1, each negative word subtracts 1 from the score.
- Negation handling: if a negation word ("not", "no", "never", "dont", etc.) appears immediately before a sentiment word, the polarity flips (e.g., "not happy" scores -1 instead of +1).
- Preprocessing strips punctuation and normalizes repeated characters ("soooo" becomes "soo").
- Label thresholds: score > 0 is positive, score < 0 is negative, score == 0 is neutral.

**Strengths of this approach:**
- Transparent and explainable: you can see exactly which words drove the prediction.
- Handles simple negation correctly ("not happy" -> negative, "not bad" -> positive).
- No training data required; works immediately with handcrafted word lists.
- Fast and deterministic.

**Weaknesses of this approach:**
- Cannot detect sarcasm ("I love getting stuck in traffic" is predicted as positive).
- Cannot predict "mixed" labels because it only looks at the net score, not whether both positive and negative words are present.
- Limited vocabulary: words not in the word lists are invisible to the model.
- Negation only works for immediately adjacent words; "I don't think this is good" would not be caught.

## 4. How the ML Model Works (if used)

**Features used:**
Bag of words using CountVectorizer. Each post is represented as a vector of word counts.

**Training data:**
The model trained on all 16 posts in `SAMPLE_POSTS` with their corresponding `TRUE_LABELS`.

**Training behavior:**
The model achieved 100% accuracy on the training data. This is expected with only 16 examples and a model with enough capacity to memorize them all. With the original 6 examples, the model also achieved 100%. Adding more examples did not reduce training accuracy.

**Strengths and weaknesses:**
Strengths: The ML model can learn patterns that the rule based model cannot, such as predicting "mixed" for posts with conflicting signals, and correctly labeling the sarcastic post. It automatically learns which word combinations map to which labels.

Weaknesses: The 100% training accuracy is misleading. The model has likely memorized the training data rather than learning generalizable patterns. With only 16 examples, it would probably fail on new, unseen posts. It also cannot explain its reasoning as transparently as the rule based model.

## 5. Evaluation

**How you evaluated the model:**
Both models were evaluated on the same 16 labeled posts from `dataset.py`.
- Rule based model accuracy: **81%** (13/16 correct)
- ML model training accuracy: **100%** (16/16 correct)

**Examples of correct predictions:**
- "I am not happy about this" -> both models correctly predicted **negative**. The rule based model handled the negation of "happy".
- "This is not bad at all" -> both models correctly predicted **positive**. The negation of "bad" flipped the score.
- "Had a great day with amazing friends" -> both predicted **positive**. Multiple positive words made this straightforward.

**Examples of incorrect predictions:**
- "I absolutely love getting stuck in traffic" -> rule based predicted **positive** (true: negative). The model saw "love" and scored it positively, missing the sarcasm entirely. The ML model got this right because it memorized this specific example.
- "Feeling tired but kind of hopeful" -> rule based predicted **negative** (true: mixed). The model only saw "tired" (negative) and had no mechanism to output "mixed". The ML model got this right.
- "Lowkey stressed but kind of proud of myself" -> rule based predicted **negative** (true: mixed). Same issue: "stressed" triggered negative, and "proud" is not in the word list.

## 6. Limitations

- The dataset is very small (16 posts). Neither model would generalize well to real-world text.
- The rule based model cannot detect sarcasm, irony, or implied meaning.
- The rule based model has no "mixed" label logic; it can only output positive, negative, or neutral.
- The ML model's 100% accuracy is on training data only. Without a separate test set, we cannot measure true generalization.
- Both models only work on short English text. Longer passages, other languages, or code-switching would break them.
- The word lists are limited; common sentiment words like "wonderful", "horrible", "anxious", or "proud" are missing.

## 7. Ethical Considerations

- **Misclassifying distress:** If used in a real application, predicting "neutral" or "positive" for a message expressing distress (e.g., sarcastic cries for help) could mean someone who needs support is overlooked.
- **Cultural and linguistic bias:** The word lists and training data reflect a narrow slice of English. Slang, AAVE, regional dialects, or non-English text may be systematically misclassified, leading to unfair treatment of certain communities.
- **Privacy:** Analyzing personal messages for mood raises significant privacy concerns. Users should consent to and understand how their text is being classified.
- **Overconfidence:** Both models output a single label with no confidence score. In practice, users of the model might trust a "positive" label without knowing the model was uncertain.

## 8. Ideas for Improvement

- **Add more labeled data** from diverse sources to improve generalization.
- **Use TF-IDF** instead of CountVectorizer to give less weight to common words.
- **Add a "mixed" detection rule** to the rule based model: if both positive and negative words appear, output "mixed".
- **Expand the word lists** with more sentiment words, slang, and emoji mappings.
- **Create a separate test set** so ML accuracy reflects real generalization, not memorization.
- **Use a pretrained model** (e.g., a small transformer or sentiment-specific model) that understands context, sarcasm, and nuance.
- **Add confidence scores** so users know when the model is uncertain.
- **Improve negation handling** to work across longer phrases, not just adjacent words.
