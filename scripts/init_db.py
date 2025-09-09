from app.database import Base, engine
import app.models as models  

print("Creating tables (via SQLAlchemy metadata)...")
Base.metadata.create_all(bind=engine)
print("Done")
        