# AI-Powered-Role-Based RAG Chatbot

A secure enterprise-style Retrieval-Augmented Generation (RAG) chatbot built using FastAPI, Streamlit, OpenAI APIs, and Pinecone vector search.

This project demonstrates how AI assistants can securely interact with internal company data by combining semantic retrieval, structured data querying, authentication, and role-based access control.

---

# Project Overview

Most AI chatbots return the same information to every user. This project was designed to explore how internal AI systems can securely provide different responses depending on user roles, permissions, and data access policies.

The chatbot combines:

* Semantic document retrieval
* Structured data access
* Role-based access control (RBAC)
* Query routing
* Metadata-filtered vector search
* Grounded LLM response generation

The system simulates how enterprise AI assistants can securely interact with internal company knowledge systems.

---

# Key Features

## Role-Based Access Control

Users can only retrieve information they are authorised to access.

Examples:

* Employees can access only department-relevant information
* Different roles can retrieve different document categories
* Metadata filtering restricts unauthorised retrieval

---

## Hybrid Retrieval Architecture

The chatbot dynamically routes queries between:

* Structured data retrieval
* Semantic document retrieval
* Hybrid retrieval depending on the query type

---

## Semantic Search with Metadata Filtering

Internal documents are chunked, embedded, and stored in the vector database with metadata such as:

* department
* category
* allowed_roles
* source
* chunk_index

This enables secure semantic retrieval using metadata-based filtering.

---

## Query Routing

A routing layer classifies user queries and decides which retrieval pipeline to use:

* Structured retrieval
* Vector search retrieval
* Hybrid retrieval

---

## Grounded AI Responses

The LLM generates answers only from retrieved authorised context.

Guardrails are implemented to:

* Prevent hallucinations
* Prevent unauthorised responses
* Restrict responses to retrieved context only

---

# System Workflow

```text id="nsgx8q"
User Login
   ↓
Authentication Layer
   ↓
Identify User Role
   ↓
User Query
   ↓
Query Router
   ↓
Structured Retrieval / Vector Retrieval / Hybrid Retrieval
   ↓
Access Control Validation
   ↓
Context Retrieval
   ↓
Prompt Builder
   ↓
LLM Response Generation
   ↓
Guardrail Validation
   ↓
Final Response
```

---

# Project Architecture

The system is divided into modular components for scalability and maintainability.

## Workflow Phases

1. Data ingestion and chunking
2. Embedding generation
3. Vector database indexing
4. User authentication
5. Query routing
6. Retrieval and filtering
7. Prompt generation
8. LLM response generation
9. Guardrail validation
10. Final response delivery

---

# Project Structure

```text id="x1e6yi"
CODEBASICS_PROJECT/
│
├── app/
│   ├── services/
│   │   ├── chunk.py
│   │   ├── data_store.py
│   │   ├── embedder.py
│   │   ├── llm.py
│   │   ├── parse.py
│   │   ├── prompts.py
│   │   ├── query.py
│   │   ├── router.py
│   │   └── vectordb.py
│   │
│   ├── api.py
│   ├── orch.py
│   ├── rough.py
│   └── test.py
│
├── frontend/
│   └── ui.py
│
├── resources/
│   └── data/
│       ├── engineering/
│       ├── finance/
│       ├── general/
│       ├── hr/
│       └── marketing/
│
├── requirements.txt
├── .env
└── README.md
```

---

# Folder Description

## app/services/

Contains the core business logic of the RAG pipeline:

* Document chunking
* Embedding generation
* Query routing
* Prompt handling
* Vector database operations
* LLM interaction
* Data retrieval

---

## frontend/

Contains the Streamlit-based user interface for interacting with the chatbot.

---

## resources/data/

Stores department-wise internal documents and knowledge sources used for semantic retrieval.

---

## api.py

Handles backend API endpoints and request processing.

---

## orch.py

Acts as the orchestration layer connecting routing, retrieval, prompts, and response generation.

---

## vectordb.py

Manages vector database indexing and semantic search operations.

---

## router.py

Classifies queries and routes them to the appropriate retrieval pipeline.

---

## prompts.py

Stores reusable prompts and system instructions for the LLM.

---

## embedder.py

Generates vector embeddings from document chunks.

---

## chunk.py

Splits documents into semantic chunks for efficient retrieval.

---

# Tech Stack

## Backend

* Python
* FastAPI

## Frontend

* Streamlit

## AI & Retrieval

* OpenAI API
* Retrieval-Augmented Generation (RAG)
* Pinecone / ChromaDB
* Semantic Search
* Vector Embeddings

## Data & Security

* Metadata Filtering
* Role-Based Access Control (RBAC)
* Authentication & Authorization

---

# Example Use Cases

## HR Knowledge Assistant

Employees can query:

* HR policies
* Leave policies
* Internal guidelines
* Company procedures

while preventing unauthorised document access.

---

## Department Knowledge Retrieval

Different departments can retrieve relevant:

* Engineering documents
* Finance policies
* Marketing information
* Internal operational procedures

based on their role permissions.

---

# Why I Built This

I wanted to explore how AI systems move beyond simple chat interfaces into practical internal business tools.

The focus of this project was not just building a chatbot, but designing:

* Secure AI retrieval systems
* Enterprise-style access control
* AI workflow orchestration
* Hybrid retrieval pipelines
* Scalable modular architecture

This project reflects how modern organisations may integrate AI assistants into real operational environments while maintaining security and data governance.

---

# Future Improvements

* JWT authentication
* Database-backed user management
* LangChain / LangGraph orchestration
* Conversation memory
* Multi-agent workflows
* Audit logging
* Admin dashboard
* Real-time document ingestion
* Docker deployment

---

# Installation

## Clone Repository

```bash id="dz74ej"
git clone <your-repository-url>
cd CODEBASICS_PROJECT
```

---

## Create Virtual Environment

```bash id="ek4j6z"
python -m venv venv
```

---

## Activate Environment

### Windows

```bash id="ffy35f"
venv\\Scripts\\activate
```

### Mac/Linux

```bash id="vcw3gi"
source venv/bin/activate
```

---

## Install Dependencies

```bash id="zq7i7u"
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file:

```env id="ez61v1"
OPENAI_API_KEY=your_api_key
PINECONE_API_KEY=your_api_key
```

---

# Run Application

## Start Backend

```bash id="5v5y1j"
uvicorn app.api:app --reload
```

---

## Start Frontend

```bash id="1ljc71"
streamlit run frontend/ui.py
```

---

# Demo

Demo Video:
[Insert Loom / YouTube Link]

Architecture Workflow:


---

# Skills Demonstrated

Python, FastAPI, Streamlit, OpenAI API, Retrieval-Augmented Generation (RAG), Pinecone, Vector Databases, Semantic Search, Embeddings, Metadata Filtering, Role-Based Access Control (RBAC), Prompt Engineering, LLM Integration, API Development, Authentication & Authorization, Query Routing, Hybrid Search, AI Workflow Automation, Backend Development, Enterprise AI Systems, Information Retrieval, Modular System Design

---

# Project Goal

This project demonstrates how Retrieval-Augmented Generation (RAG) systems can evolve from basic chatbots into secure enterprise-grade AI assistants capable of handling real-world business workflows, access control, and internal knowledge retrieval.
