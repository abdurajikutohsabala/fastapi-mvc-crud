from sqlalchemy.orm import Session
from . import models, schemas
from . import schemas 
def get_item(db: Session, item_id: int):
    # query the items table, filter by id, return the first result
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def get_items(db: Session, skip: int = 0, limit: int = 100):
    # offset skips the first 'skip' records, limit restricts how many
    return db.query(models.Item).offset(skip).limit(limit).all()

def create_item(db: Session, item: schemas.ItemCreate):
    # convert Pydantic schema to a dictionary and unpack into a new Item model
    db_item = models.Item(**item.dict())
    db.add(db_item)        # stage the insertion
    db.commit()            # actually run the SQL
    db.refresh(db_item)    # get the new id and any DB defaults
    return db_item

def update_item(db: Session, item_id: int, item: schemas.ItemUpdate):
    db_item = get_item(db, item_id)
    if not db_item:
        return None
    # update the fields with the new data
    update_data = item.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item(db: Session, item_id: int):
    db_item = get_item(db, item_id)
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item