from fastapi import FastAPI, HTTPException

app = FastAPI(title="Product Write Into CMC API", version="1.0.0")

def make_pyodbc_conn(driver: str, server: str, database: str, uid: str, pwd: str) -> str:
    return (
        f"Driver={{{driver}}};"
        f"Server={server};"
        f"Database={database};"
        f"UID={uid};"
        f"PWD={pwd};"
    )

@app.get("/get-connection-string")
def get_connection_string(apikey: str):
    if apikey == "CMWEBAPIKEY":
        driver = "ODBC Driver 17 for SQL Server"
        server = "192.168.1.28,1510"
        database = "CalcmenuWeb_DemoEN"
        uid = "egs.marion"
        pwd = "36&%2%zCD4gLTRXkku"
    elif apikey == "CMCAPIKEY":
        driver = "ODBC Driver 17 for SQL Server"
        server = "192.168.1.28,1510"
        database = "CMC_2025"
        uid = "egs.marion"
        pwd = "36&%2%zCD4gLTRXkku"
    else:
        raise HTTPException(status_code=401, detail="Invalid API key")

    return make_pyodbc_conn(driver, server, database, uid, pwd)
