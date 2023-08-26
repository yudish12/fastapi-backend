from ..database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Numeric,ARRAY

class Product(Base):
    __tablename__ = "Products"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(30))
    description = Column(String)
    category = Column(String)
    price = Column(Integer)
    inStock = Column(Boolean)
    Images = Column(ARRAY(String))
    mainImage = Column(String)
    quantity = Column(Integer)
    discount = Column(Numeric)
