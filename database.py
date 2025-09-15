from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Înlocuiește parola cu cea reală din Supabase
DATABASE_URL = "postgresql://postgres:Adriangrila24$@db.nczdzhjhekabliwiryvc.supabase.co:5432/postgres?sslmode=require"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
