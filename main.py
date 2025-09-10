from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from database import SessionLocal
from models import Firm, Financial, Activitate

app = FastAPI()

# CORS pentru Streamlit
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔍 Endpoint: căutare firmă
@app.get("/firme")
def cauta_firma(q: str):
    db = SessionLocal()
    results = db.query(Firm).filter(
        (Firm.cui == q) | (Firm.denumire.ilike(f"%{q}%"))
    ).all()

    if not results:
        db.close()
        return JSONResponse(status_code=404, content={"detail": "Firma nu a fost găsită"})

    response = []
    for f in results:
        cifra = (
            db.query(Financial)
            .filter(Financial.cui == f.cui, Financial.an == 2024)
            .first()
        )
        response.append({
            "cui": f.cui,
            "denumire": f.denumire,
            "adr_judet": f.adr_judet,
            "adr_localitate": f.adr_localitate,
            "numar_licente": f.numar_licente,
            "cifra_afaceri": cifra.cifra_afaceri if cifra else 0
        })

    db.close()
    return response

# 📥 Model pentru activitate
class ActivitateInput(BaseModel):
    cui: str
    data: str  # format YYYY-MM-DD
    scor: int
    comentariu: str

# ✅ Endpoint: salvare activitate
@app.post("/agenda")
def adauga_activitate(act: ActivitateInput):
    db = SessionLocal()
    try:
        activitate = Activitate(
            cui=act.cui,
            data=act.data,
            scor=act.scor,
            comentariu=act.comentariu
        )
        db.add(activitate)
        db.commit()
        return {"status": "ok"}
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"detail": str(e)})
    finally:
        db.close()
