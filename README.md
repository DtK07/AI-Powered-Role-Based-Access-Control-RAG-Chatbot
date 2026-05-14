# Role-Based RAG Chatbot

A secure enterprise-style Retrieval-Augmented Generation (RAG) chatbot built using FastAPI, Streamlit, OpenAI APIs, and Pinecone vector search.

This project demonstrates how AI assistants can securely interact with internal company data by combining semantic retrieval, structured data querying, authentication, and role-based access control.

---

# Project Overview

Most AI chatbots return the same information to every user. This project was designed to explore how internal AI systems can securely provide different responses depending on user roles, permissions, and data access policies.

The chatbot combines:

* Semantic document retrieval
* Structured HR data access
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

* Employees can access only their own HR-related information
* Managers can access team-level data
* HR/Admin roles can access broader organisational information

---

## Hybrid Retrieval Architecture

The chatbot dynamically routes queries between:

* Structured HR datasets (Pandas / SQL-style retrieval)
* Semantic document retrieval (Pinecone vector search)
* Or both depending on the query

---

## Semantic Search with Metadata Filtering

Internal documents are chunked, embedded, and stored in Pinecone with metadata such as:

* allowed_roles
* department
* document_type
* employee_id

This enables secure semantic retrieval using metadata-based filtering.

---

## Query Routing

A routing layer classifies user queries and decides which retrieval pipeline to use:

* Structured data retrieval
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

```text
User Login
   ↓
Authentication Layer
   ↓
Identify Role & Employee ID
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

# Tech Stack

## Backend

* Python
* FastAPI

## Frontend

* Streamlit

## AI & Retrieval

* OpenAI API
* Retrieval-Augmented Generation (RAG)
* Pinecone Vector Database
* Semantic Search
* Vector Embeddings

## Data & Security

* Pandas
* Metadata Filtering
* Role-Based Access Control (RBAC)
* Authentication & Authorization

---

# Project Structure

```text
rag_chatbot/
│
├── app/
│   ├── main.py
│   ├── auth.py
│   ├── router.py
│   ├── rag.py
│   ├── dataframe_agent.py
│   ├── prompts.py
│   ├── schemas.py
│   └── config.py
│
├── frontend/
│   └── streamlit_app.py
│
├── data/
│   ├── hr_data.csv
│   └── documents/
│
├── requirements.txt
├── .env
└── README.md
```

---

# Example Use Cases

## HR Assistant

Employees can query:

* Leave balances
* Internal HR policies
* Employee handbook information

while preventing access to other employees’ sensitive data.

---

## Internal Knowledge Assistant

Teams can retrieve:

* Company policies
* Operational procedures
* Department-specific documentation
* Internal knowledge-base content

based on their access level.

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
* LangChain/LlamaIndex orchestration
* Conversation memory
* Multi-agent workflows
* Audit logging
* Admin dashboard
* Real-time document ingestion

---


---

# Skills Demonstrated

Python, FastAPI, Streamlit, OpenAI API, Retrieval-Augmented Generation (RAG), Pinecone, Vector Databases, Semantic Search, Embeddings, Metadata Filtering, Role-Based Access Control (RBAC), Prompt Engineering, LLM Integration, API Development, Authentication & Authorization, Query Routing, Hybrid Search, Pandas, AI Workflow Automation, Backend Development, Enterprise AI Systems, Information Retrieval, Modular System Design
