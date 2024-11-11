from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.models.base import Base


class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    sale = Column(Integer)
    description = Column(String(100), nullable=False)
    count = Column(Integer)
    category_id = Column(Integer, ForeignKey('category.id', ondelete='CASCADE'), nullable=False)

    category = relationship('Category', back_populates='products')
