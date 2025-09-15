from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Firma

app = FastAPI()

# Funcție pentru a obține sesiunea DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta principală (opțională)
@app.get("/")
def home():
    return {"message": "CRM Galați API este activ 🚀"}

# Endpoint pentru căutarea unei firme după CUI
@app.get("/firme")
def cauta_firma(q: str, db: Session = Depends(get_db)):
    firma = db.query(Firma).filter(Firma.cui == q).first()
    if not firma:
        raise HTTPException(status_code=404, detail="Firma nu a fost găsită")
    return {
        "cui": firma.cui,
        "denumire": firma.denumire,
        "adr_judet": firma.adr_judet,
        "cifra_afaceri": float(firma.cifra_afaceri)
    }
