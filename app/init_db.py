from .database import SessionLocal, Base, engine
from .models import User
import uuid

Base.metadata.create_all(bind=engine)
db = SessionLocal()

# Add test user
user = User(
    id=str(uuid.uuid4()),
    name="Aditya Tyagi",
    email="aditya@example.com",
    phone="9876543210"
)
db.add(user)
db.commit()
db.close()

print("✅ User created.")
