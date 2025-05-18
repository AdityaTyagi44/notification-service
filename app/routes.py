from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import uuid4
import json
import aio_pika

from .database import SessionLocal
from .models import User, Notification, NotificationStatus
from .schemas import NotificationCreate, NotificationOut, UserOut

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/notifications", response_model=NotificationOut)
async def send_notification(payload: NotificationCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == payload.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    notif_id = str(uuid4())
    notification = Notification(
        id=notif_id,
        user_id=payload.user_id,
        type=payload.type,
        content=payload.content,
        status=NotificationStatus.pending
    )
    db.add(notification)
    db.commit()
    db.refresh(notification)

    connection = await aio_pika.connect_robust("amqp://guest:guest@localhost/")
    channel = await connection.channel()
    await channel.default_exchange.publish(
        aio_pika.Message(body=json.dumps({"notification_id": notif_id}).encode()),
        routing_key="notifications"
    )
    await connection.close()

    return notification

@router.get("/users/{user_id}/notifications", response_model=UserOut)
def get_user_notifications(user_id: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
 
