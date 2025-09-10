from sqlalchemy import Column, String, Integer, Date
from database import Base

class Firm(Base):
    __tablename__ = "firms"

    cui = Column(String, primary_key=True, index=True)
    denumire = Column(String)
    adr_judet = Column(String)
    adr_localitate = Column(String)
    numar_licente = Column(Integer)

class Financial(Base):
    __tablename__ = "financials_annual"

    id = Column(Integer, primary_key=True, index=True)
    cui = Column(String, index=True)
    an = Column(Integer)
    cifra_afaceri = Column(Integer)
    profitul_net = Column(Integer)

class Activitate(Base):
    __tablename__ = "activitati"

    id = Column(Integer, primary_key=True, index=True)
    cui = Column(String, index=True)
    data = Column(Date)
    scor = Column(Integer)
    comentariu = Column(String)
