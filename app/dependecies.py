from .database import SessionLocal, engine
from .models import productModel          

productModel.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
