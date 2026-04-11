# Internship Project: Multi-Agent PRD/Memo Generator

## Week 1: Prompt Engineering & System Prompts
- [ ] **Architecture Design**
    - [ ] Define the system architecture for the dual-agent workflow.
- [ ] **Agent Persona Development**
    - [ ] Design strict system prompts for **The Writer** (Generation).
    - [ ] Design strict system prompts for **The Critic** (Evaluation).
- [ ] **Prompt Optimization**
    - [ ] Implement **few-shot prompting** with high-quality PRD/Memo examples.
    - [ ] Test and validate basic API calls and tone consistency in Jupyter Notebooks.

## Week 2: Implementing the Multi-Agent Graph
- [ ] **Workflow Orchestration**
    - [ ] Set up the state management using **LangGraph** (or CrewAI).
- [ ] **Node & Edge Logic**
    - [ ] Code the **Writer Node** for document generation.
    - [ ] Code the **Critic Node** for document evaluation.
- [ ] **Conditional Routing**
    - [ ] Implement a conditional edge to loop the process if the Critic's score is below the threshold.

## Week 3: Structured Output & Tool Calling
- [ ] **Robust Data Extraction**
    - [ ] Implement **Function Calling/Tool Use** for agent communication.
- [ ] **JSON Schema Enforcement**
    - [ ] Force the LLM to output reviews in a strict JSON format (e.g., `status`, `feedback`).
    - [ ] Test parsing logic to ensure the backend handles outputs without regex errors.

## Week 4: Human-in-the-Loop & API Wrapping
- [ ] **FastAPI Integration**
    - [ ] Wrap the LangGraph workflow in a FastAPI backend.
- [ ] **Human-in-the-Loop (HITL)**
    - [ ] Implement a workflow "pause" for manual human approval before finalization.
    - [ ] Create an API endpoint to resume/approve the pending state.
- [ ] **Final Delivery**
    - [ ] Finalize the GitHub repository with a detailed architecture guide.
    - [ ] Document the agent graph logic and state transitions in the README.
