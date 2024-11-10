import networkx as nx

# Initialize a directed graph
graph = nx.DiGraph()

def add_host(ip, domain):
    """Add a host node to the graph."""
    graph.add_node(ip, type="Host", domain=domain)
    return ip

def add_service(host_ip, name, port, status):
    """Add a service node and connect it to a host."""
    service_id = f"{host_ip}:{port}"
    graph.add_node(service_id, type="Service", name=name, port=port, status=status)
    graph.add_edge(host_ip, service_id, relationship="exposes")
    return service_id

def add_vulnerability(service_id, vuln_id, description, severity):
    """Add a vulnerability node and connect it to a service."""
    graph.add_node(vuln_id, type="Vulnerability", description=description, severity=severity)
    graph.add_edge(service_id, vuln_id, relationship="has_vulnerability")
    return vuln_id

def get_related_nodes(node, relationship_type):
    """Retrieve related nodes based on relationship type."""
    return [
        target for _, target, data in graph.edges(node, data=True)
        if data.get("relationship") == relationship_type
    ]
