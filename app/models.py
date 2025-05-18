from sqlalchemy import Column, String, Enum, ForeignKey, Text, DateTime
from sqlalchemy.dialects.sqlite import INTEGER
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from .database import Base

class NotificationType(str, enum.Enum):
    email = "email"
    sms = "sms"
    inapp = "inapp"

class NotificationStatus(str, enum.Enum):
    pending = "pending"
    sent = "sent"
    failed = "failed"

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    notifications = relationship("Notification", back_populates="user")

class Notification(Base):
    __tablename__ = "notifications"
    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"))
    type = Column(Enum(NotificationType))
    content = Column(Text)
    status = Column(Enum(NotificationStatus), default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)
    sent_at = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="notifications")

