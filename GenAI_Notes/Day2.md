
# Day2
---

## **I. Prompting Fundamentals**
Large Language Models (LLMs) are **probabilistic systems**, not deterministic programs. This means the same prompt can yield different results. To ensure consistency, prompts should be treated like code.

### **The 5 Components of a Strong Prompt**
1.  **Role:** Define who the AI is (e.g., "You are a senior developer").
2.  **Task:** Specifically what needs to be done.
3.  **Context:** Provide all necessary background information.
4.  **Format:** Define how the output should look (List, JSON, etc.).
5.  **Constraints:** Set clear boundaries and safety limitations.

---

## **II. Core Prompting Techniques**
Different levels of guidance help the model recognize patterns and logic.

* **Zero-Shot:** Asking for a task **without examples**. Best for simple, general tasks.
* **One-Shot:** Providing **one example** to demonstrate the expected pattern or format.
* **Few-Shot:** Providing **multiple examples** (Input + Expected Output). This significantly improves accuracy and pattern recognition.
* **Chain-of-Thought (CoT):** Encouraging the model to **"think step-by-step"** before giving a final answer. This reduces mistakes in complex reasoning or math.

---

## **III. Advanced Controls & System Prompts**
**System Prompts** establish the "ground rules" before any user interaction occurs. They define:
* **AI Role & Expertise**
* **Tone & Style** (Formal vs. Casual)
* **Safety Restrictions**
* **Output Structure**

---

## **IV. Structured Data & Reliable Outputs**
* **JSON Formatting:** Using JSON (JavaScript Object Notation) ensures that AI outputs are machine-readable and strictly organized, making it easier to integrate AI responses into professional software and databases.
* **Project Goal:** The aim of these techniques is to design prompts that produce **structured and reliable** responses for building real-world AI assistants.
