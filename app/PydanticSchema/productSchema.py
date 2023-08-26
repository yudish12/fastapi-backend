from pydantic import BaseModel

class productBase(BaseModel):
    name:str|None = None
    description:str|None = None
    category:str|None = None
    price:float|None = None
    inStock:bool|None = None
    Images:list|None = None
    mainImage:str|None = None
    quantity:int|None = None
    discount:int|None = None