import google.generativeai as genai
from langchain.prompts import PromptTemplate
from graph_utils import get_related_nodes

# Configure Google Gemini API with your API key
genai.configure(api_key=" API key")  # Replace with your actual

# Prompt template setup
prompt_template = PromptTemplate(
    input_variables=["host", "services", "vulnerabilities"],
    template="Host {host} has services {services}. Vulnerabilities found: {vulnerabilities}. Provide a security summary."
)

def get_host_info(ip):
    services = get_related_nodes(ip, "exposes")
    vulnerabilities = []
    for service in services:
        vulnerabilities.extend(get_related_nodes(service, "has_vulnerability"))

    services_info = ", ".join(service for service in services)
    vulnerabilities_info = ", ".join(vuln for vuln in vulnerabilities)

    return {
        "host": ip,
        "services": services_info,
        "vulnerabilities": vulnerabilities_info
    }

def generate_response(ip):
    """Generate a response based on the host IP information."""
    data = get_host_info(ip)
    prompt = prompt_template.format(
        host=data["host"],
        services=data["services"],
        vulnerabilities=data["vulnerabilities"]
    )
    
    # Choose a model (you might need to replace the model name with an actual model available in your setup)
    model_name = "text-bison-001"  # Replace with an available model name from `genai.list_models()`

    # Generate the response using the model's predict method
    response = genai.generate_text(model=model_name, prompt=prompt)
    
    # Check the response format and return the content
    return response['candidates'][0]['output']  # Adjust based on actual response structure
