import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Agar environment mein DATABASE_URL hai toh wo use hoga, warna fallback Neon URL use hoga
# "YAHAN_APNA_NEON_URL_RAKHEIN" ki jagah apna pichla Neon DB string paste rakhein
SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://neondb_owner:npg_2BSZIFh8tzqk@ep-snowy-poetry-ap4d7021.c-7.us-east-1.aws.neon.tech/neondb?sslmode=require"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
