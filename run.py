# Définition du Swagger
""" 
    SWAGGER
    C'est l'interface Web qui manifeste toute la configuration du Back-End :
    L'instance "app" est l'objet du Routeur principal (Classe FasAPI),
    le Point de départ de toute l'application.

    Les 4 façons de tester l'application via Swagger : 

    1. http://127.0.0.1:8001/
    2. http://127.0.0.1:8001/index/
    3. http://127.0.0.1:8001/docs/
    4. http://127.0.0.1:8001/Redoc/

"""
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="127.0.0.1", port=8001, reload=True)