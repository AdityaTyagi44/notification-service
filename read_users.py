from app.database import SessionLocal
from app.models import User

db = SessionLocal()
users = db.query(User).all()
for user in users:
    print(f"Name: {user.name}, ID: {user.id}")
db.close()
