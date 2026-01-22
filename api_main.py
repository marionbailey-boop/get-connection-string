from fastapi import FastAPI

app = FastAPI(
    title="Product Write Into CMC API",
    version="1.0.0"
)

def clean_connection_string(conn_str: str) -> str:
    return " ".join(line.strip() for line in conn_str.strip().splitlines())


@app.post("/get-connection-string")
def get_connection_string(apikey: str) -> str:
    try:
        match apikey:
            case "CMWEBAPIKEY":
                connection_string = """
                    Server=192.168.1.28,1510;
                    Database Name=CalcmenuWeb_DemoEN;
                    User Id=egs.marion;
                    Password=36&%2%zCD4gLTRXkku;
                    Database Driver=ODBC Driver 17 for SQL Server;
                """
            case "CMCAPIKEY":
                connection_string = """
                    Server=192.168.1.28,1510;
                    Database Name=CMC_2025;
                    User Id=egs.marion;
                    Password=36&%2%zCD4gLTRXkku;
                    Database Driver=ODBC Driver 17 for SQL Server;
                """
            case _:
                raise ValueError("Invalid API Key") # To be Implemented

        response = clean_connection_string(connection_string)
    
    except Exception as e:
        raise ValueError(f"Error determining connection string: {str(e)}")
    
    return response
    


