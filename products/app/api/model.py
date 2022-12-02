from typing import List
from pydantic import BaseModel
from uuid import uuid4
from datetime import datetime

class ProductRequest(BaseModel):
    id: str = str(uuid4())
    nickname: str
    productType: str
    gender: List[str]
    name: str
    storyHtml: str
    releaseYear: str
    details: str
    sku: str
    color: str
    brandName: str
    silhouette: str
    slug: str
    imageList: List[str]
    mainPictureUrl: str
    productId: str
    sellerEmail: str
    size: str
    price: int
    productListedOnSite: bool
    customerOrdered: bool
    productReceivedOnSite: bool
    authenticityCheck: bool
    productShippedToCustomer: bool
    productDelivered: bool
    rejectProduct: bool
    sold: bool
    isActive: bool = True
    isDelete: bool = False
    createdAt: str = datetime.utcnow().isoformat()
    updatedAt: str = datetime.utcnow().isoformat()