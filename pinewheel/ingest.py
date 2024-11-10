from pymongo import MongoClient
from graph_utils import add_host, add_service, add_vulnerability

# Connect to MongoDB (replace 'localhost' with your Atlas connection string if needed)
client = MongoClient("mongodb://localhost:27017/")
db = client["cybersecurity_db"]

def ingest_data():
    """Ingest data from MongoDB and update the graph."""
    hosts = db.hosts.find()  # Retrieve all documents in the 'hosts' collection
    
    for host in hosts:
        # Add host node
        host_node = add_host(host["ip"], host["domain"])

        for service in host.get("services", []):
            # Add service node and connect it to the host
            service_node = add_service(host["ip"], service["name"], service["port"], service["status"])

            for vuln in service.get("vulnerabilities", []):
                # Add vulnerability node and connect it to the service
                add_vulnerability(service_node, vuln["id"], vuln["description"], vuln["severity"])

# Run ingestion to populate the graph
ingest_data()
