import asyncio
import json
from aio_pika import connect_robust, IncomingMessage
from .database import SessionLocal
from .models import Notification, NotificationStatus
from .utils.email_sender import send_email
from .utils.sms_sender import send_sms
from .utils.inapp_sender import send_inapp
from datetime import datetime

async def handle_message(message: IncomingMessage):
    async with message.process():
        data = json.loads(message.body)
        db = SessionLocal()
        notification = db.query(Notification).filter_by(id=data['notification_id']).first()
        if not notification:
            return
        try:
            success = False
            if notification.type == "email":
                success = send_email(notification.content, notification.user.email)
            elif notification.type == "sms":
                success = send_sms(notification.content, notification.user.phone)
            elif notification.type == "inapp":
                success = send_inapp(notification.content, notification.user_id)

            if success:
                notification.status = NotificationStatus.sent
                notification.sent_at = datetime.utcnow()  
            else:
                notification.status = NotificationStatus.failed
            db.commit()
        finally:
            db.close()

async def main():
    connection = await connect_robust("amqp://guest:guest@localhost/")
    channel = await connection.channel()
    queue = await channel.declare_queue("notifications")
    await queue.consume(handle_message)
    print(" [*] Worker started. Waiting for messages.")
    await asyncio.Future()  # Run forever
