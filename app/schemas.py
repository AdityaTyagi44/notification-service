from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from .models import NotificationType, NotificationStatus

class NotificationCreate(BaseModel):
    user_id: str
    type: NotificationType
    content: str

class NotificationOut(BaseModel):
    id: str
    user_id: str
    type: NotificationType
    content: str
    status: NotificationStatus
    created_at: datetime
    sent_at: Optional[datetime]

    class Config:
        orm_mode = True

class UserOut(BaseModel):
    id: str
    name: str
    email: str
    phone: str
    notifications: List[NotificationOut] = []

    class Config:
        orm_mode = True
 
