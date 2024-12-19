from fastapi import FastAPI, HTTPException, Query
from iracingdataapi.client import irDataClient

# Inicializa o FastAPI
app = FastAPI(title="iRacing API Wrapper")

# Função para criar o cliente com as credenciais fornecidas
def create_iracing_client(username: str, password: str):
    try:
        # Cria o cliente com os dados fornecidos
        idc = irDataClient(username=username, password=password)
        return idc
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao conectar ao iRacing: {str(e)}")


# Endpoint: Resumo do Membro
@app.get("/member_summary")
def get_member_summary(username: str, password: str):
    try:
        idc = create_iracing_client(username, password)
        data = idc.stats_member_summary()
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint: Corridas Recentes
@app.get("/recent_races")
def get_recent_races(username: str, password: str):
    try:
        idc = create_iracing_client(username, password)
        data = idc.stats_member_recent_races()
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint: Estatísticas Anuais
@app.get("/yearly_stats")
def get_yearly_stats(username: str, password: str):
    try:
        idc = create_iracing_client(username, password)
        data = idc.stats_member_yearly()
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint: Recapitulativo
@app.get("/member_recap")
def get_member_recap(username: str, password: str):
    try:
        idc = create_iracing_client(username, password)
        data = idc.stats_member_recap()
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint: Resumo de Temporadas
@app.get("/season_summary")
def get_season_summary(username: str, password: str):
    try:
        idc = create_iracing_client(username, password)
        data = idc.time_attack_member_season_results()
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Rota de Saúde
@app.get("/")
def health_check():
    return {"status": "API funcionando!", "endpoints": ["/member_summary", "/recent_races", "/yearly_stats", "/member_recap", "/season_summary"]}
