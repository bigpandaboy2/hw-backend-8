from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import FlowerCreate, FlowerOut
from app.repositories.flowers import FlowersRepository
from app.database import get_db

router = APIRouter()

@router.get("/flowers", response_model=list[FlowerOut])
def get_flowers(db: Session = Depends(get_db)):
    return FlowersRepository.get_flowers(db)

@router.post("/flowers", response_model=FlowerOut)
def create_flower(flower_data: FlowerCreate, db: Session = Depends(get_db)):
    return FlowersRepository.create_flower(db, flower_data)

@router.patch("/flowers/{flower_id}", response_model=FlowerOut)
def update_flower(flower_id: int, data: dict, db: Session = Depends(get_db)):
    flower = FlowersRepository.update_flower(db, flower_id, data)
    if not flower:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Flower not found"
        )
    return flower

@router.delete("/flowers/{flower_id}")
def delete_flower(flower_id: int, db: Session = Depends(get_db)):
    success = FlowersRepository.delete_flower(db, flower_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Flower not found"
        )
    return {"message": "Flower deleted successfully"}
