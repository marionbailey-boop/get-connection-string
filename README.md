# Connection String Provider API (FastAPI)

A small FastAPI service that returns a SQL Server (pyodbc) connection string based on a provided API key.
Clients can call this API to obtain the correct DB connection string for either CMWeb or CMC.

### What this API does

**Exposes:** GET /get-connection-string

**Input:** apikey (query parameter)

**Output:** a pyodbc-formatted SQL Server connection string:

    Driver={...};Server=...;Database=...;UID=...;PWD=...;


If the API key is invalid, returns **401 Unauthorized**

**Endpoint**

    GET /get-connection-string

**Query parameter**

    apikey (string, required)

**Success response**

    200 OK

**Body:** plain text connection string

**Error response**

    401 Unauthorized

    { "detail": "Invalid API key" }

**Example usage**

    CURL
    curl "http://127.0.0.1:8000/get-connection-string?apikey=CMWEBAPIKEY"

**Python (client example)**
    import requests
    import pyodbc

    url = "http://127.0.0.1:8000/get-connection-string"
    resp = requests.get(url, params={"apikey": "CMWEBAPIKEY"})
    resp.raise_for_status()

    conn_str = resp.text
    conn = pyodbc.connect(conn_str)

**Running locally**
1. Install dependencies
    
    pip install fastapi uvicorn

2. Start the server

    uvicorn app:app --reload --host 127.0.0.1 --port 8000

3. Docs

    Swagger UI: http://127.0.0.1:8000/docs

**Configuration in code (current behavior)**

**Your code currently hardcodes:**

- API keys

- DB server/database

- DB credentials (UID/PWD)

Based on the API key, it selects one of two DB targets:

- CMWEBAPIKEY → CalcmenuWeb_DemoEN

- CMCAPIKEY → CMC_2025

**Security warnings (important)**

- This service returns database credentials to whoever can call it successfully. That means:

- Anyone who gets the API key can potentially access the DB directly.

- Traffic must be protected (TLS).

- The endpoint should be internal-only (VPN/private network) or behind a secure gateway.

- Keys must be rotated and never committed in source control.

