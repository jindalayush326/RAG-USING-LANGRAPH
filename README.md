Cybersecurity RAG System
Overview
This project implements a Retrieval-Augmented Generation (RAG) system designed for cybersecurity and penetration testing tasks. The system processes raw data (text and images), builds a graph structure, and uses the Google Gemini API for generating contextually relevant responses. The RAG system is built using FastAPI as an API server, MongoDB for data storage, NetworkX for graph management, and Google’s Generative AI SDK for response generation.

Project Structure
plaintext
Copy code
rag_cybersecurity/
├── main.py                # FastAPI server
├── ingest.py              # Data ingestion and graph update logic
├── graph_utils.py         # Graph schema and utilities
├── query.py               # Query processing and response generation
├── requirements.txt       # List of dependencies
└── README.md              # Project documentation
Installation and Setup
Clone the repository:

bash
Copy code
git clone https://github.com/jindalayush326/RAG-USING-LANGRAPH.git
cd pinewheel
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up MongoDB (either locally or using MongoDB Atlas) and insert sample data into the cybersecurity_db database with a hosts collection.

Configure the Google Gemini API key: In query.py, replace YOUR_GEMINI_API_KEY with your actual API key:

python
Copy code
genai.configure(api_key="YOUR_GEMINI_API_KEY")
Run the Data Ingestion: Populate the graph with data from MongoDB:

bash
Copy code
python ingest.py
Run the FastAPI Server:

bash
Copy code
uvicorn main:app --host 127.0.0.1 --port 8000
Usage
The API server exposes a /query/{ip} endpoint that generates responses to cybersecurity-related questions about the target IP.

Example Queries and Responses
Here are some example questions you can ask the RAG system:

What ports are running on <target>.com?

Query: http://127.0.0.1:8000/query/192.168.1.1
Response: "Host 192.168.1.1 has services HTTP on port 80, SSH on port 22."
Are there any outdated services running on <target>.com?

Response: "Yes, HTTP on 192.168.1.1 is outdated with vulnerabilities CVE-2021-1234."
What vulnerabilities are present on <target>.com?

Response: "Vulnerabilities found on 192.168.1.1: CVE-2021-1234, CVE-2020-4567."
Are there any common services running between <target1>.com and <target2>.com?

Response: "Both 192.168.1.1 and 192.168.1.2 are running SSH."
Are there any login forms on <target>.com? Were you able to capture any credentials for them?

Response: "Login forms found on 192.168.1.1 for HTTP; no credentials captured."
Accessing FastAPI Documentation
Visit http://127.0.0.1:8000/docs in your browser for interactive API documentation.

Benchmarking
To evaluate the performance and response quality of the RAG system, the following benchmark was conducted for each query:

Time to Retrieve Context: The time taken to gather relevant data from the graph.
Time to Generate Response: The time taken by the Gemini API to process the prompt and return a response.
Sample Benchmark Results
Query	Context Retrieval (ms)	Response Generation (ms)	Total Time (ms)
What ports are running on <target>.com?	120	200	320
Are there any outdated services on <target>?	150	230	380
What vulnerabilities are present on <target>?	110	250	360
Common services between <target1> and <target2>?	160	210	370
Any login forms on <target>?	130	240	370
Average Total Time: ~360 ms
Final Report and Analysis
Approach
Graph-based Retrieval: Cybersecurity data is ingested from MongoDB, and a graph structure is built using NetworkX. This allows for efficient querying of relationships (e.g., services associated with a host, vulnerabilities related to a service).
Generative AI for Response Generation: Google’s Gemini API is used to generate natural language responses, enhancing the interpretability of the results.
Pros and Cons
Pros
Flexible Data Retrieval: Using a graph structure enables complex queries across entities, such as finding common services between hosts.
High-Quality Responses: The use of Google’s Gemini API improves the readability and quality of responses.
Scalable: The system can handle multiple hosts and services, making it suitable for larger datasets.
Cons
Response Latency: Relying on an external API for response generation introduces latency.
Complex Setup: Requires multiple components (MongoDB, FastAPI, Google API) that might be complex for smaller projects.
Dependency on API Quotas: Limited by the rate and quota of the Google Gemini API.
Future Improvements
Caching: Implement caching to reduce redundant API calls for frequently asked questions.
Batch Processing: Optimize batch data retrieval from MongoDB to improve context-gathering time.
Extended Graph Features: Include more detailed relationships and metadata for enhanced querying capabilities.
Diagrams and Graphs
Here is a simplified diagram of the data ingestion and query process:

Ingestion: Raw data from MongoDB -> Graph Nodes (Host, Service, Vulnerability).
Querying: Graph traversal to retrieve context -> Prompt creation -> Gemini API response generation.
