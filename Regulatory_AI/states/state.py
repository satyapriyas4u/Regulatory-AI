# state.py
import reflex as rx
import requests

# Update the URL to match your actual server endpoint:
API_URL = "http://narmada.merai.cloud:6565/query/"

class QueryState(rx.State):
    """
    Stores user inputs (category, test_type, query_text) and the response from the backend.
    """
    category: str = ""
    test_type: str = ""
    query_text: str = ""
    response: str = ""

    def generate_response(self):
        """
        Called when user clicks 'Generate' on the page.
        Sends data to the Narmada server (LightRAG backend) and updates self.response.
        """
        if not self.test_type or not self.query_text:
            self.response = "Please select a test type and enter a query."
            return

        payload = {
            "category": self.category,
            "test": self.test_type,
            "query_text": self.query_text
        }

        try:
            r = requests.post(API_URL, json=payload)
            if r.status_code == 200:
                # Expecting JSON with a "response" key
                self.response = r.json().get("response", "No response received.")
            else:
                self.response = f"Server error: status code {r.status_code}"
        except Exception as e:
            self.response = f"Error connecting to server: {str(e)}"
