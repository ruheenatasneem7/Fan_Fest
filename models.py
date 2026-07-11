from database import db


class CreatorApplication(db.Model):

    __tablename__ = "creator_applications"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(200))
    email = db.Column(db.String(200), unique=True)
    phone = db.Column(db.String(30))

    country = db.Column(db.String(100))
    city = db.Column(db.String(100))

    handle = db.Column(db.String(100))
    niche = db.Column(db.String(100))

    platforms = db.Column(db.Text)

    followers = db.Column(db.String(50))
    avg_views = db.Column(db.String(50))

    profile_links = db.Column(db.Text)

    panel = db.Column(db.Boolean)
    meet_and_greet = db.Column(db.Boolean)
    collabs = db.Column(db.Boolean)
    brand_deals = db.Column(db.Boolean)
    live_challenges = db.Column(db.Boolean)

    bio = db.Column(db.Text)
    previous_event = db.Column(db.Text)

    referral = db.Column(db.String(100))

    terms = db.Column(db.Boolean)
    media = db.Column(db.Boolean)
    newsletter = db.Column(db.Boolean)