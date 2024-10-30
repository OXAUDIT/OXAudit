import requests
import sys

def audit_check():
    # Replace with your server URL
    url = 'https://google.com/'
    
    try:
        response = requests.get(url)  # Change to POST if you need to send data
        response.raise_for_status()  # Raises an error for bad responses (4xx or 5xx)

        # Process the response (assuming it's JSON)
        data = response.json()
        print("Response from server:", data)

    except requests.RequestException as e:
        print("Error occurred:", e)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'AuditCheck':
        audit_check()
    else:
        print("Usage: oxaudit AuditCheck")
