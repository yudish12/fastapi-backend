from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from ..dependecies import get_db
from ..models import productModel
from ..PydanticSchema.productSchema import productBase
import cloudinary
import cloudinary.uploader

cloudinary.config( 
    cloud_name = "diz30a185", 
    api_key = "243714934632878", 
    api_secret = "lQpoPYiQ8kRDMxGqKI2kCyN6yKw" 
    )

router = APIRouter(    
    prefix="/product",
    tags=["items"],
    responses={404: {"description": "Not found"}}
    )

@router.get("/")
def get_product(db: Session = Depends(get_db)):
    db_products = db.query(productModel.Product).all()
    return {"data":db_products}


@router.post("/")
async def create_product(payload:productBase,db: Session = Depends(get_db)):
    mainImage = cloudinary.uploader.upload(payload.mainImage, public_id = payload.name)
    print(mainImage["url"])
    updatedProduct = payload.model_copy(update={"mainImage": mainImage["url"]})
    newProduct = dict(updatedProduct)
    db_product = productModel.Product(**newProduct)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return {"data":db_product}



@router.get("/{id}")
def get_product(id:int,db: Session = Depends(get_db)):
    db_products = db.query(productModel.Product).get(id)
    return {"data":db_products}


    
@router.delete("/{id}")
def delete_product(id:int,db:Session = Depends(get_db)):
    db.query(productModel.Product).filter(productModel.Product.id==id).delete()
    db.commit()
    return {"data":"deleted"}


@router.put("/{id}")
def update_product(id:int,payload:productBase,db:Session = Depends(get_db)):
    pass