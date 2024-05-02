from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#บรรทัดนี้คือการสร้างไฟล์ใหม่ชื่อ once_again01 จากนั้นเอาใน colab มาใส่ไฟล์ models.py จะได้ไฟล์ใหม่ใน dbeaver ชื่อ once_again01 
SQLALCHEMY_DATABASE_URL = "sqlite:///./backend_cloud/backend_cloud.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args = { "check_same_thread": False,}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()