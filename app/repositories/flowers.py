from sqlalchemy.orm import Session
from app.models import Flower
from app.schemas import FlowerCreate

class FlowersRepository:
    @staticmethod
    def create_flower(db: Session, flower_data: FlowerCreate) -> Flower:
        db_flower = Flower(
            name=flower_data.name,
            description=flower_data.description,
            price=flower_data.price
        )
        db.add(db_flower)
        db.commit()
        db.refresh(db_flower)
        return db_flower

    @staticmethod
    def get_flowers(db: Session) -> list[Flower]:
        return db.query(Flower).all()

    @staticmethod
    def get_flower_by_id(db: Session, flower_id: int) -> Flower | None:
        return db.query(Flower).filter(Flower.id == flower_id).first()

    @staticmethod
    def update_flower(db: Session, flower_id: int, data: dict) -> Flower | None:
        flower = db.query(Flower).filter(Flower.id == flower_id).first()
        if not flower:
            return None
        for key, value in data.items():
            setattr(flower, key, value)
        db.commit()
        db.refresh(flower)
        return flower

    @staticmethod
    def delete_flower(db: Session, flower_id: int) -> bool:
        flower = db.query(Flower).filter(Flower.id == flower_id).first()
        if not flower:
            return False
        db.delete(flower)
        db.commit()
        return True
