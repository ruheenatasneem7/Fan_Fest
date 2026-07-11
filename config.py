import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("DB_PORT"))      # <-- temporary
print(os.getenv("DB_USER"))      # <-- temporary
print(os.getenv("DB_NAME"))      # <-- temporary



class Config:

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{os.getenv('DB_USER')}:"
        f"{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('DB_HOST')}:"
        f"{os.getenv('DB_PORT')}/"
        f"{os.getenv('DB_NAME')}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False