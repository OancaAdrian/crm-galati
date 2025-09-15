from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Înlocuiește PAROLA_TA cu parola reală din Supabase
DATABASE_URL = "postgresql://postgres.nczdzhjhekabliwiryvc:Adriangrila24$@aws-1-eu-central-1.pooler.supabase.com:6543/postgres?sslmode=require"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
