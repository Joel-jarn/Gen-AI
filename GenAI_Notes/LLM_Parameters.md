# LLM Generation Parameters: Technical Notes

These parameters control the sampling process of Large Language Models, allowing you to tune the balance between accuracy and creativity.

---

## 1. Temperature (Randomness)
Temperature modifies the probability distribution of the next token.

- **Formula Concept:** $P_i = \frac{\exp(logits_i / T)}{\sum \exp(logits_j / T)}$
- **Low (0.1 - 0.4):** Sharpens the distribution. The model becomes more deterministic and less likely to stray from the "most correct" path.
- **High (0.8+):** Flattens the distribution. The model becomes more diverse, creative, and unpredictable.

---

## 2. Top-P (Nucleus Sampling)
Instead of looking at a fixed number of words, Top-P looks at the cumulative probability mass.

- **Function:** The model only considers tokens that make up the top $P$ percentage of the probability mass.
- **Benefit:** It dynamically adjusts the vocabulary "breadth" based on how confident the model is in that specific context.

---

## 3. Max Tokens (Length Control)
The maximum number of tokens allowed in a single generation.

- **Units:** 1 token $\approx$ 0.75 words.
- **Purpose:** Prevents rambling, manages API latency, and controls costs.

---

## 4. Penalties
These modify the scores of tokens to reduce repetition.

| Parameter | Logic | Use Case |
| :--- | :--- | :--- |
| **Frequency Penalty** | Increases penalty as a word is repeated more often. | Reducing repetitive phrases. |
| **Presence Penalty** | Constant penalty once a word appears. | Forcing the model to move to new topics. |

---

## Quick Reference Table

| Task | Temperature | Top-P | Penalties |
| :--- | :--- | :--- | :--- |
| **Code / Logic** | 0.0 | 1.0 | 0.0 |
| **Chatbot** | 0.7 | 0.9 | 0.1 |
| **Creative Writing** | 0.9 | 1.0 | 0.5 |
