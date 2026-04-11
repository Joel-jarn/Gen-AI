# Internship Project: RAG-Based Learning Assistant

## Week 1: Ingestion Pipeline & Vector Database Setup
- [ ] **Project Initialization**
    - [ ] Initialize GitHub repository with a clean `.gitignore`.
    - [ ] Set up FastAPI project structure and `.env` file for API keys.
- [ ] **Data Ingestion Script**
    - [ ] Implement PDF parsing using `PyPDF2`.
    - [ ] Configure `RecursiveCharacterTextSplitter` for optimal text chunking.
- [ ] **Vector Database Integration**
    - [ ] Generate embeddings via OpenAI embedding models.
    - [ ] Set up and upsert vectors into Pinecone or ChromaDB.

## Week 2: Retrieval-Augmented Generation (RAG) Implementation
- [ ] **Retrieval Logic**
    - [ ] Build the retrieval endpoint in FastAPI.
    - [ ] Implement query embedding and Top-K similarity search.
- [ ] **Prompt Engineering & Completion**
    - [ ] Construct a strict "Expert Tutor" prompt template.
    - [ ] Integrate the LLM to generate responses based *only* on retrieved context.
- [ ] **Citations**
    - [ ] Ensure the API returns source document citations alongside the response.

## Week 3: Conversational Memory & Adaptive Quizzes
- [ ] **Session Management**
    - [ ] Implement `ConversationBufferMemory` for multi-turn dialogue.
    - [ ] Ensure the system maintains context across a single session.
- [ ] **Structured Output Generation**
    - [ ] Create a dedicated endpoint for quiz generation.
    - [ ] Use LLM structured output (JSON) to generate 5 multiple-choice questions per topic.

## Week 4: UI Integration, Streaming, & Evaluation
- [ ] **Frontend & UX**
    - [ ] Wire the FastAPI backend to the chat-based UI.
    - [ ] Implement Server-Sent Events (SSE) for real-time token streaming.
- [ ] **Finalization & Security**
    - [ ] Secure all sensitive credentials in the `.env` file.
    - [ ] Complete the `README.md` with a detailed RAG architecture diagram.
    - [ ] Perform final repository cleanup and documentation.
