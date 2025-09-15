from sqlalchemy import Column, Integer, String, Numeric
from database import Base

class Firma(Base):
    __tablename__ = "firms"

    id = Column(Integer, primary_key=True, index=True)
    cui = Column(String, unique=True, index=True)
    denumire = Column(String)
    adr_judet = Column(String)
    cifra_afaceri = Column(Numeric)
