from .database import SessionLocal, Base, engine
from .models import User

Base.metadata.create_all(bind=engine)
db = SessionLocal()

# Use a fixed UUID so it's easy to reference in README or testing
user = User(
    id="1111-2222-3333-4444",  # ✅ Hardcoded user ID
    name="Aditya Tyagi",
    email="aditya@example.com",
    phone="9876543210"
)

# Avoid duplicates if script is run multiple times
existing = db.query(User).filter_by(id=user.id).first()
if not existing:
    db.add(user)
    db.commit()
    print("✅ Test user created with ID: 1111-2222-3333-4444")
else:
    print("ℹ️ User already exists with ID: 1111-2222-3333-4444")

db.close()

