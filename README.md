# Advanced RAG-Enabled Transformer Embedding System
### Intelligent Knowledge Discovery from Excel Datasets  
AI-Powered Data Querying • Semantic Search • Explainable Insights

![image_alt](https://github.com/Devadharshani13/RAG-Enabled-Transformer-Embedding-System-for-Intelligent-Knowledge-Discovery-from-Excel-Datasets/blob/main/Screenshots%20of%20working/Login%20Page.png?raw=true)


---

## 📌 Project Overview

This project presents an **AI-driven knowledge discovery system** that enables users to interact with Excel datasets using **natural language queries**.

The system integrates **Retrieval-Augmented Generation (RAG)** with **Transformer-based embeddings** to retrieve relevant dataset rows and generate accurate responses.

The platform converts spreadsheet rows into **vector embeddings**, stores them in a **FAISS vector database**, and retrieves relevant information using **semantic similarity search**.

A modern **React dashboard** allows users to upload datasets and query them interactively.

### Mission
Transform static spreadsheet data into an intelligent conversational data exploration system.

---

# 🎯 Problem Statement

Many organizations store valuable information in Excel files, but extracting insights from these datasets is difficult.

Key problems include:

- Large datasets are difficult to search manually
- Non-technical users cannot write complex queries
- Traditional filtering methods are time-consuming
- Data insights remain hidden inside spreadsheets

---

# 💡 Solution

This system provides an AI-powered interface that allows users to query Excel datasets using natural language.

Key features include:

- Upload Excel datasets (.xlsx / .csv)
- Convert dataset rows into semantic embeddings
- Store embeddings using FAISS vector database
- Natural language query interface
- Retrieval-Augmented Generation (RAG) pipeline
- Similarity-based data retrieval
- Explainable AI results with supporting rows

---

# 🧠 System Architecture

```

User
↓
Frontend Interface (React Dashboard)
↓
API Requests (FastAPI Backend)
↓
Embedding Generation
↓
Vector Database (FAISS)
↓
Retrieval-Augmented Generation
↓
Response Generation
↓
Frontend Visualization

```

---

# 🔐 Key Features

✔ Excel dataset ingestion  
✔ Semantic search using vector embeddings  
✔ Retrieval-Augmented Generation pipeline  
✔ Explainable AI responses  
✔ Similarity scoring  
✔ Interactive dashboard interface  

---

# 🧰 Tech Stack

## Frontend
- React.js (Vite)
- Tailwind CSS
- Axios
- Recharts

## Backend
- Python
- FastAPI
- RESTful API

## Database
- PostgreSQL (metadata storage)
- FAISS (vector database)

## AI / NLP
- Sentence Transformers
- Transformer Embeddings
- Retrieval-Augmented Generation (RAG)

---

# 📊 System Workflow

1. User uploads an Excel dataset.
2. Dataset rows are converted into textual format.
3. Transformer model generates semantic embeddings.
4. Embeddings are stored in FAISS vector database.
5. User submits a natural language query.
6. Query is converted into an embedding vector.
7. FAISS retrieves the most relevant dataset rows.
8. Retrieved rows are passed as context to the language model.
9. AI generates a response based on retrieved data.
10. Results are displayed in the dashboard.

---

# 📈 Example Query

![image_alt](https://github.com/Devadharshani13/RAG-Enabled-Transformer-Embedding-System-for-Intelligent-Knowledge-Discovery-from-Excel-Datasets/blob/main/Screenshots%20of%20working/upload%20multiple%20files%20and%20comparing%20of%20it.png?raw=true)

### User Query

```

Which employee has the highest salary?

```

### System Response

```

Mary has the highest salary of 75000.

```

Supporting dataset rows and similarity scores are also displayed.

---

# ⚠ Challenges Faced

### Large Dataset Processing
Embedding generation for large datasets required significant computational resources.

**Solution:**  
Batch embedding generation was implemented to improve processing efficiency.

### Retrieval Accuracy
Initial vector search sometimes returned less relevant results.

**Solution:**  
Hybrid retrieval and cross-encoder reranking improved search accuracy.

### Frontend-Backend Integration
Integrating the React frontend with FastAPI APIs required handling asynchronous API requests.

**Solution:**  
Axios was used for API communication with proper error handling.

### Deployment Challenges
Attempts were made to deploy the backend on Render and the frontend on Vercel, but configuration issues prevented successful deployment.

**Solution:**  
The system was successfully demonstrated by running both frontend and backend locally using **Visual Studio Code**.

---

# 🌍 Applications

This system can be used in various domains including:

- Business analytics
- Financial reporting
- Human resource management
- Research data analysis
- Enterprise knowledge retrieval

---

# 📊 Future Improvements

Future enhancements may include:

- Multi-dataset querying
- Integration with advanced vector databases (Pinecone, Weaviate)
- Real-time data ingestion
- Cloud deployment optimization
- Advanced analytics dashboards

---

# 📂 Project Structure

```

excel-rag-system
│
├── backend
│   ├── app
│   │   ├── ingestion
│   │   ├── embeddings
│   │   ├── retrieval
│   │   ├── generation
│   │   └── vector_store
│   │
│   ├── api
│   └── requirements.txt
│
├── frontend
│   ├── src
│   │   ├── pages
│   │   ├── components
│   │   ├── services
│   │   └── utils
│
└── README.md

````

---

# 🚀 Installation

## Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend will run at:

```
http://127.0.0.1:8000
```

---

## Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend will run at:

```
http://localhost:5173
```

---

# 👨‍💻 Developer

Intern – Bits N' Bytes Cybersecurity Education, USA

Trainer: **Vidhya**

---

⭐ Transforming spreadsheet data into intelligent conversational insights.
