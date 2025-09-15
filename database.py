from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Înlocuiește PAROLA_TA cu parola reală din Supabase → Database Settings → Database password
DATABASE_URL = "postgresql://postgres:Adriangrila24$@postgres.nczdzhjhekabliwiryvc.supabase.co:6543/postgres?sslmode=require"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
