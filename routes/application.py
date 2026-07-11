from flask import Blueprint
from flask import request
from flask import jsonify

from database import db
from models import CreatorApplication

import json

application_bp = Blueprint("application", __name__)


@application_bp.route("/api/applications", methods=["POST"])
def submit_application():

    data = request.json

    application = CreatorApplication(

        name=data["personalInfo"]["name"],
        email=data["personalInfo"]["email"],
        phone=data["personalInfo"]["phone"],

        country=data["personalInfo"]["country"],
        city=data["personalInfo"]["city"],

        handle=data["creatorProfile"]["handle"],
        niche=data["creatorProfile"]["niche"],

        platforms=json.dumps(data["creatorProfile"]["platforms"]),

        followers=data["creatorProfile"]["followerCount"],
        avg_views=data["creatorProfile"]["avgViews"],

        profile_links=json.dumps(
            data["creatorProfile"]["profileLinks"]
        ),

        panel=data["participationPreferences"]["panel"],

        meet_and_greet=data["participationPreferences"]["meetAndGreet"],

        collabs=data["participationPreferences"]["collabs"],

        brand_deals=data["participationPreferences"]["brandDeals"],

        live_challenges=data["participationPreferences"]["liveChallenges"],

        bio=data["additionalDetails"]["bio"],

        previous_event=data["additionalDetails"]["previousEventExperience"],

        referral=data["additionalDetails"]["referralSource"],

        terms=data["consents"]["termsAndConditions"],

        media=data["consents"]["mediaConsent"],

        newsletter=data["consents"]["newsletter"]

    )

    db.session.add(application)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Application Submitted Successfully"
    }), 201