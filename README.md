FanFestClone/
│
├── app.py
├── requirements.txt
├── README.md
│
├── static/
│   ├── css/
│   │      style.css
│   │      responsive.css
│   │      animation.css
│   │
│   ├── js/
│   │      script.js
│   │
│   └── images/
│
├── templates/
│      index.html
│
└── screenshots/md


Code:


Fullstack website by frontend (HTML-5, CSS, Javasript) Backend: Pyhton, database :PostgreSql

routes:
application.py 
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

    

    .env 

DB_USER=postgres
DB_PASSWORD=biltit123
DB_HOST=localhost
DB_PORT=5432
DB_NAME=fanfest_db




app.py  


from flask import Flask,render_template
from flask_cors import CORS

from config import Config
from database import db

from routes.application import application_bp

app = Flask(__name__)

app.config.from_object(Config)

CORS(app)

db.init_app(app)

app.register_blueprint(application_bp)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return   render_template("index.html")
        


if __name__ == "__main__":
    app.run(debug=True)



    config.py


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


database.py  


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



models.py  


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



requriment.txt  


Flask

Flask-SQLAlchemy

Flask-Cors

psycopg2-binary

python-dotenv

Werkzeug




index.html 


<!DOCTYPE html>
<html lang="en">
    <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>FanFest 2026 — Content Creators, Join Us</title>
    <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&amp;family=DM+Sans:ital,wght@0,300;0,400;0,600;1,300&amp;display=swap" rel="stylesheet">
    <link rel="stylesheet"
      href="{{ url_for('static', filename='css/style.css') }}">
    
    </head>
    

    <nav>
        <a href="#" class="nav-logo">Fan<span>Fest</span> 2026</a>
        <a href="#apply" class="nav-cta">Apply Now</a>
    </nav>

  <section class="hero" id="home">
      
      <p class="hero-eyebrow">🎬 Open Applications — Limited Spots</p>
      <h1 class="hero-title">CREATE.<br>
        <span>CONNECT.</span>
        <br>DOMINATE.</h1>
      <p class="hero-sub">FanFest 2026 is calling on creators like you to be part of the biggest fan-powered event of the year. Share your world, grow your audience, and make history.</p>
      <div class="hero-btns">
        <a href="#apply" class="btn-primary">Apply as a Creator</a>
        <a href="#about" class="btn-ghost">Learn More</a>
      </div>
      <div class="hero-date-bar">
         <div class="date-item"><div class="val">AUG 14–16</div><div class="lbl">Event Dates</div></div>
         <div class="date-item"><div class="val">2026</div><div class="lbl">Edition</div></div>
         <div class="date-item"><div class="val">50K+</div><div class="lbl">Expected Fans</div></div>
         <div class="date-item"><div class="val">200+</div><div class="lbl">Creator Spots</div></div>
      </div>
  </section>
<section class="about" id="about">
  <p class="section-tag">What Is FanFest 2026</p>
  <h2 class="section-title">Where Creators<br>Meet Their Fans</h2>
  <p class="section-lead">Three days of panels, activations, live streams, brand collaborations, and unforgettable fan moments — all under one roof.</p>
  <div class="about-grid">
    <div class="about-card">
      <div class="icon">🎤</div>
      <h3>Live Panels &amp; Talks</h3>
      <p>Host your own stage session, Q&amp;A, or join a creator roundtable. Real conversations with your real fans.</p>
    </div>
    <div class="about-card">
      <div class="icon">📸</div>
      <h3>Meet &amp; Greet Booths</h3>
      <p>Dedicated creator booths where fans can interact, take photos, and grab exclusive merchandise.</p>
    </div>
    <div class="about-card">
      <div class="icon">🤝</div>
      <h3>Brand Collaborations</h3>
      <p>Connect with top-tier sponsors looking for authentic creator partnerships during the event.</p>
    </div>
    <div class="about-card">
      <div class="icon">🎮</div>
      <h3>Live Content Challenges</h3>
      <p>Compete in cross-creator content battles, streamed live for the audience and judged by fans.</p>
    </div>
    <div class="about-card">
      <div class="icon">🌐</div>
      <h3>Global Streaming Reach</h3>
      <p>The entire event is live-streamed to millions worldwide — your content extends far beyond the venue.</p>
    </div>
    <div class="about-card">
      <div class="icon">🎉</div>
      <h3>Creator After-Party</h3>
      <p>An exclusive closing night celebration — network, celebrate, and create memories off-camera too.</p>
    </div>
  </div>
</section>
<section id="perks">
  <p class="section-tag">Creator Perks</p>
  <h2 class="section-title">What You Get</h2>
  <p class="section-lead">Every creator who joins FanFest 2026 gets a full support package designed to help you shine.</p>
  <div class="perks-list">
    <div class="perk"><div class="perk-num">01</div><div class="perk-body"><h4>All-Access Badge</h4><p>Backstage, VIP zones, creator lounge, and all event areas throughout the three days.</p></div></div>
    <div class="perk"><div class="perk-num">02</div><div class="perk-body"><h4>Complimentary Accommodation</h4><p>Hotel stay covered for the full duration of the event for verified creators.</p></div></div>
    <div class="perk"><div class="perk-num">03</div><div class="perk-body"><h4>Dedicated Creator Stage</h4><p>Your own scheduled time slot on the creator main stage or breakout rooms.</p></div></div>
    <div class="perk"><div class="perk-num">04</div><div class="perk-body"><h4>Professional Content Crew</h4><p>On-site videographers and photographers available to document your FanFest moments.</p></div></div>
    <div class="perk"><div class="perk-num">05</div><div class="perk-body"><h4>Promotion Package</h4><p>Featured on all official FanFest 2026 social media, website, and email marketing to 500K+ subscribers.</p></div></div>
    <div class="perk"><div class="perk-num">06</div><div class="perk-body"><h4>Exclusive Merch Kit</h4><p>Limited-edition FanFest 2026 creator merchandise kit sent to you before the event.</p></div></div>
  </div>
</section>
       <!-- WHO CAN APPLY -->
       <section class="who" id="who">
  <p class="section-tag">Eligibility</p>
  <h2 class="section-title">Who Can Apply?</h2>
  <p class="section-lead">We welcome creators across every niche, platform, and audience size. If you create — this is for you.</p>
  <div class="who-grid">
    <a href="#apply" class="who-badge"><span class="emoji">📹</span><span>YouTubers</span></a>
    <a href="#apply" class="who-badge"><span class="emoji">🎵</span><span>TikTokers</span></a>
    <a href="#apply" class="who-badge"><span class="emoji">📸</span><span>Instagrammers</span></a>
    <a href="#apply" class="who-badge"><span class="emoji">🎙️</span><span>Podcasters</span></a>
    <a href="#apply" class="who-badge"><span class="emoji">🎮</span><span>Streamers</span></a>
    <a href="#apply" class="who-badge"><span class="emoji">✍️</span><span>Bloggers</span></a>
    <a href="#apply" class="who-badge"><span class="emoji">🎨</span><span>Digital Artists</span></a>
    <a href="#apply" class="who-badge"><span class="emoji">💪</span><span>Fitness Creators</span></a>
    <a href="#apply" class="who-badge"><span class="emoji">🍳</span><span>Food Creators</span></a>
    <a href="#apply" class="who-badge"><span class="emoji">👗</span><span>Fashion Creators</span></a>
  </div>
</section>
<!-- TIMELINE -->
<section id="timeline">
  <p class="section-tag">Key Dates</p>
  <h2 class="section-title">Application Timeline</h2>
  <div class="timeline-list">
    <div class="tl-item">
      <div class="tl-dot">1</div>
      <div class="tl-content">
        <div class="tl-date">May 15 – Jun 30, 2026</div>
        <h4>Applications Open</h4>
        <p>Submit your creator application form with your details and profile links.</p>
      </div>
    </div>
    <div class="tl-item">
      <div class="tl-dot">2</div>
      <div class="tl-content">
        <div class="tl-date">July 1 – July 15, 2026</div>
        <h4>Review &amp; Selection</h4>
        <p>Our team reviews all submissions. Shortlisted creators are contacted directly.</p>
      </div>
    </div>
    <div class="tl-item">
      <div class="tl-dot">3</div>
      <div class="tl-content">
        <div class="tl-date">July 20, 2026</div>
        <h4>Confirmation &amp; Onboarding</h4>
        <p>Selected creators receive official confirmation, event details, and onboarding kit.</p>
      </div>
    </div>
    <div class="tl-item">
      <div class="tl-dot">4</div>
      <div class="tl-content">
        <div class="tl-date">August 14–16, 2026</div>
        <h4>FanFest 2026 — LIVE</h4>
        <p>Three days of content, connection, and unforgettable fan experiences.</p>
      </div>
    </div>
  </div>
</section>
<!-- APPLICATION FORM -->
<section class="form-section" id="apply">
  <div class="form-wrap">
    <h2 class="form-title">Apply as a Creator</h2>
    <p class="form-sub">Fill in the form below and we'll review your application within 5–7 business days.</p>

    <form action="#" method="post" onsubmit="handleSubmit(event)">

      <!-- Personal Info -->
      <p class="section-tag" style="margin-bottom:1.25rem;">Personal Information</p>
      <div class="form-row">
        <div class="form-group">
          <label for="fname">First Name <span>*</span></label>
          <input type="text" id="fname" name="fname" placeholder="e.g. Alex" required="">
        </div>
        <div class="form-group">
          <label for="lname">Last Name <span>*</span></label>
          <input type="text" id="lname" name="lname" placeholder="e.g. Rivera" required="">
        </div>
      </div>
      <div class="form-row">
        <div class="form-group">
          <label for="email">Email Address <span>*</span></label>
          <input type="email" id="email" name="email" placeholder="hello@yoursite.com" required="">
        </div>
        <div class="form-group">
          <label for="phone">Phone Number</label>
          <input type="text" id="phone" name="phone" placeholder="+91 9876543210">
        </div>
      </div>
      <div class="form-row">
        <div class="form-group">
          <label for="country">Country <span>*</span></label>
          <select id="country" name="country" required="">
            <option value="" disabled="" selected="">Select your country</option>
            <option>India</option>
            <option>United States</option>
            <option>United Kingdom</option>
            <option>Canada</option>
            <option>Australia</option>
            <option>Philippines</option>
            <option>Indonesia</option>
            <option>Brazil</option>
            <option>Other</option>
          </select>
        </div>
        <div class="form-group">
          <label for="city">City</label>
          <input type="text" id="city" name="city" placeholder="e.g. Mumbai">
        </div>
      </div>

      <hr class="form-divider">

      <!-- Creator Profile -->
      <p class="section-tag" style="margin-bottom:1.25rem;">Creator Profile</p>
      <div class="form-row">
        <div class="form-group">
          <label for="handle">Primary Creator Handle / Name <span>*</span></label>
          <input type="text" id="handle" name="handle" placeholder="@yourname" required="">
        </div>
        <div class="form-group">
          <label for="niche">Content Niche <span>*</span></label>
          <select id="niche" name="niche" required="">
            <option value="" disabled="" selected="">Select your niche</option>
            <option>Gaming &amp; Esports</option>
            <option>Lifestyle &amp; Vlogging</option>
            <option>Fashion &amp; Beauty</option>
            <option>Food &amp; Cooking</option>
            <option>Fitness &amp; Health</option>
            <option>Tech &amp; Reviews</option>
            <option>Music &amp; Entertainment</option>
            <option>Education &amp; How-to</option>
            <option>Travel</option>
            <option>Art &amp; Design</option>
            <option>Comedy &amp; Skits</option>
            <option>Other</option>
          </select>
        </div>
      </div>

      <div class="form-group">
        <label>Primary Platform(s) <span>*</span></label>
        <div class="checkbox-group">
          <label class="checkbox-item"><input type="checkbox" name="platform" value="youtube"><span>YouTube</span></label>
          <label class="checkbox-item"><input type="checkbox" name="platform" value="instagram"><span>Instagram</span></label>
          <label class="checkbox-item"><input type="checkbox" name="platform" value="tiktok"><span>TikTok</span></label>
          <label class="checkbox-item"><input type="checkbox" name="platform" value="twitch"><span>Twitch</span></label>
          <label class="checkbox-item"><input type="checkbox" name="platform" value="podcast"><span>Podcast</span></label>
          <label class="checkbox-item"><input type="checkbox" name="platform" value="x"><span>X (Twitter)</span></label>
          <label class="checkbox-item"><input type="checkbox" name="platform" value="other"><span>Other</span></label>
        </div>
      </div>

      <div class="form-row">
        <div class="form-group">
          <label for="followers">Total Followers / Subscribers <span>*</span></label>
          <select id="followers" name="followers" required="">
            <option value="" disabled="" selected="">Select range</option>
            <option>1K – 10K</option>
            <option>10K – 50K</option>
            <option>50K – 100K</option>
            <option>100K – 500K</option>
            <option>500K – 1M</option>
            <option>1M+</option>
          </select>
        </div>
        <div class="form-group">
          <label for="avg-views">Average Views per Post</label>
          <select id="avg-views" name="avg_views">
            <option value="" disabled="" selected="">Select range</option>
            <option>Under 1K</option>
            <option>1K – 10K</option>
            <option>10K – 50K</option>
            <option>50K – 100K</option>
            <option>100K – 500K</option>
            <option>500K+</option>
          </select>
        </div>
      </div>

      <div class="form-group">
        <label for="channel-link">Primary Channel / Profile Link <span>*</span></label>
        <input type="url" id="channel-link" name="channel_link" placeholder="https://youtube.com/@yourchannel" required="">
      </div>

      <div class="form-group">
        <label for="other-links">Other Social Media Links</label>
        <input type="text" id="other-links" name="other_links" placeholder="Paste links separated by commas">
      </div>

      <hr class="form-divider">

      <!-- Participation Preferences -->
      <p class="section-tag" style="margin-bottom:1.25rem;">Participation Preferences</p>
      <div class="form-group">
        <label>Interested In (Select all that apply)</label>
        <div class="checkbox-group">
          <label class="checkbox-item"><input type="checkbox" name="interest" value="panel"><span>Hosting a Panel or Talk</span></label>
          <label class="checkbox-item"><input type="checkbox" name="interest" value="meetgreet"><span>Meet &amp; Greet Booth</span></label>
          <label class="checkbox-item"><input type="checkbox" name="interest" value="collab"><span>Creator Collaborations</span></label>
          <label class="checkbox-item"><input type="checkbox" name="interest" value="brand"><span>Brand Sponsorship Opportunities</span></label>
          <label class="checkbox-item"><input type="checkbox" name="interest" value="challenge"><span>Live Content Challenges</span></label>
        </div>
      </div>

      <div class="form-group">
        <label for="bio">Tell Us About Yourself &amp; Why You Want to Join <span>*</span></label>
        <textarea id="bio" name="bio" placeholder="Share a brief intro, what kind of content you create, and why FanFest 2026 excites you…" required=""></textarea>
      </div>

      <div class="form-group">
        <label for="prev-events">Previous Event Experience</label>
        <textarea id="prev-events" name="prev_events" placeholder="Have you attended or participated in fan conventions or creator events before? Tell us about it." style="min-height:80px;"></textarea>
      </div>

      <div class="form-group">
        <label for="referral">How Did You Hear About FanFest 2026?</label>
        <select id="referral" name="referral">
          <option value="" disabled="" selected="">Select one</option>
          <option>Instagram</option>
          <option>YouTube</option>
          <option>TikTok</option>
          <option>From another creator</option>
          <option>Email / Newsletter</option>
          <option>Google Search</option>
          <option>Other</option>
        </select>
      </div>

      <hr class="form-divider">

      <!-- Consent -->
      <div class="form-group">
        <div class="checkbox-group">
          <label class="checkbox-item"><input type="checkbox" name="terms" required=""><span>I agree to FanFest 2026's Terms &amp; Conditions and Creator Code of Conduct. <span style="color:var(--c-accent)">*</span></span></label>
          <label class="checkbox-item"><input type="checkbox" name="media_consent"><span>I consent to photos and videos of me being used in FanFest marketing materials.</span></label>
          <label class="checkbox-item"><input type="checkbox" name="newsletter"><span>Keep me updated with FanFest news and future opportunities.</span></label>
        </div>
      </div>

      <button type="submit" class="submit-btn">Submit My Application →</button>
      <p class="form-disclaimer">Applications close June 30, 2026. We'll respond within 5–7 business days. Limited spots available.</p>
    </form>
  </div>
</section>
<!-- FAQ -->
<section class="who" id="faq">
  <p class="section-tag">Frequently Asked Questions</p>
  <h2 class="section-title">Got Questions?</h2>
  <div class="faq-list">
    <div class="faq-item">
      <div class="faq-q">Is there a minimum follower count to apply?</div>
      <div class="faq-a">There's no hard minimum — we evaluate creators holistically based on content quality, engagement, and audience connection. Even nano-creators with highly engaged communities are welcome.</div>
    </div>
    <div class="faq-item">
      <div class="faq-q">Is travel reimbursement provided?</div>
      <div class="faq-a">We cover accommodation for all selected creators. Travel reimbursement is offered on a case-by-case basis for international creators. Details are shared in your acceptance letter.</div>
    </div>
    <div class="faq-item">
      <div class="faq-q">Can I apply as a team or co-creators?</div>
      <div class="faq-a">Yes! You can apply as a duo or small team. Each member should be listed in the application and all relevant social links included.</div>
    </div>
    <div class="faq-item">
      <div class="faq-q">What is the Creator Code of Conduct?</div>
      <div class="faq-a">FanFest 2026 requires all participating creators to maintain a respectful, inclusive environment for fans and fellow creators. The full CoC is available on our website.</div>
    </div>
    <div class="faq-item">
      <div class="faq-q">Will I be paid to participate?</div>
      <div class="faq-a">Selected creators receive a comprehensive perks package including accommodation, a dedicated stage slot, and promotional exposure. Paid partnerships are available separately through our brand matching program.</div>
    </div>
  </div>
</section>
<!-- FOOTER -->
<footer>
  <p style="font-family:'Bebas Neue',sans-serif; font-size:1.8rem; letter-spacing:0.06em; margin-bottom:0.5rem;">FAN<strong>FEST</strong> 2026</p>
  <p>August 14–16, 2026 &nbsp;·&nbsp; For creators, by creators.</p>
  <p style="margin-top:0.75rem;">© 2026 FanFest. All rights reserved. &nbsp;|&nbsp; <a href="#" style="color:var(--c-accent); text-decoration:none;">Privacy Policy</a> &nbsp;|&nbsp; <a href="#" style="color:var(--c-accent); text-decoration:none;">Contact Us</a></p>
</footer>
<script>
  document.querySelectorAll('.faq-q').forEach(q => {
    q.addEventListener('click', () => {
      const item = q.parentElement;
      const wasOpen = item.classList.contains('open');
      document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));
      if (!wasOpen) item.classList.add('open');
    });
  });

  async function handleSubmit(e) {
    e.preventDefault();
    const btn = e.target.querySelector('.submit-btn');
    const originalText = btn.textContent;
    btn.textContent = 'Submitting...';
    btn.disabled = true;

    const formData = new FormData(e.target);
    
    const mapPlatform = (val) => {
        const map = {
            'youtube': 'YouTube', 'tiktok': 'TikTok', 'twitch': 'Twitch', 
            'instagram': 'Instagram', 'x': 'Twitter/X', 'podcast': 'Podcast', 'other': 'Other'
        };
        return map[val] || 'Other';
    };

    const platforms = formData.getAll('platform').map(mapPlatform);
    if(platforms.length === 0) platforms.push('Other');

    const payload = {
      personalInfo: {
        name: formData.get('fname') + ' ' + formData.get('lname'),
        email: formData.get('email'),
        phone: formData.get('phone') || 'N/A',
        country: formData.get('country'),
        city: formData.get('city') || 'N/A'
      },
      creatorProfile: {
        handle: formData.get('handle'),
        niche: formData.get('niche'),
        platforms: platforms,
        followerCount: formData.get('followers'),
        avgViews: formData.get('avg_views') || 'N/A',
        profileLinks: [formData.get('channel_link'), formData.get('other_links')].filter(Boolean)
      },
      participationPreferences: {
        panel: formData.getAll('interest').includes('panel'),
        meetAndGreet: formData.getAll('interest').includes('meetgreet'),
        collabs: formData.getAll('interest').includes('collab'),
        brandDeals: formData.getAll('interest').includes('brand'),
        liveChallenges: formData.getAll('interest').includes('challenge')
      },
      additionalDetails: {
        bio: formData.get('bio'),
        previousEventExperience: formData.get('prev_events') || '',
        referralSource: formData.get('referral') || ''
      },
      consents: {
        termsAndConditions: formData.get('terms') === 'on',
        mediaConsent: formData.get('media_consent') === 'on',
        newsletter: formData.get('newsletter') === 'on'
      }
    };

    try {
      const response = await fetch('https://fanfest-2026.onrender.com/api/applications', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      const data = await response.json();

      if (response.ok) {
        btn.textContent = '✅ Application Submitted!';
        btn.style.background = '#16a34a';
        e.target.reset(); // Optional: reset form
      } else {
        alert('Error: ' + data.message);
        btn.textContent = originalText;
        btn.disabled = false;
      }
    } catch (err) {
      alert('Network error. Is the backend running?');
      console.error(err);
      btn.textContent = originalText;
      btn.disabled = false;
    }
  }
</script>
  
</body>

   
</html>


style.css 



/* ═══════════════════════════════════════════════════════
   FanFest — Complete Website Styles
   ═══════════════════════════════════════════════════════ */
     
     *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

   :root {
    --ff-display: 'Bebas Neue', sans-serif;
    
    --ff-body: 'DM Sans', sans-serif;
    
    --c-bg: #141832;
    
    --c-surface: #111113;
    
    --c-card: #141832;
    
    --c-border: rgba(255,255,255,0.08);
    
    --c-accent: #152db5;
    
    --c-accent2:  #34d399;
    
    --c-text: #f4f4f5;
    
    --c-muted: #5b7eff;
    
    --c-input-bg: #09090b;
    
    --radius: 12px;
  }

  html { scroll-behavior: smooth; }

  body {
    background: var(--c-bg);
    color: var(--c-text);
    font-family: var(--ff-body);
    font-size: 16px;
    line-height: 1.7;
    overflow-x: hidden;
  }

  /* ── NAV ── */
  nav {
    position: fixed; top: 0; left: 0; right: 0; z-index: 100;
    display: flex; align-items: center; justify-content: space-between;
    padding: 1rem 5vw;
    background: rgba(9,9,11,0.85);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid var(--c-border);
  }
  .nav-logo {
    font-family: var(--ff-display);
    font-size: 1.6rem;
    letter-spacing: 0.04em;
    color: var(--c-text);
    text-decoration: none;
    animation: rotateIn .8s ease forwards;
  }
  .nav-logo span { color: var(--c-accent); }
  .nav-cta {
    background: var(--c-accent);
    color: #fff;
    font-family: var(--ff-body);
    font-size: 0.85rem;
    font-weight: 600;
    padding: 0.5rem 1.25rem;
    border-radius: 999px;
    text-decoration: none;
    letter-spacing: 0.04em;
    transition: opacity .2s;
  }
  .nav-cta:hover { opacity: 0.85; }

  /* ── HERO ── */
  .hero {
    min-height: 100vh;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    text-align: center;
    padding: 6rem 5vw 4rem;
    position: relative;
    overflow: hidden;
     background: linear-gradient(
        135deg,
        #09090b,
        #1f1f23,
        #ff3c3c,
        #ff8c00
    );

    background-size: 300% 300%;

    animation: gradientShift 12s ease infinite;

  }
  .hero::before {
    content: '';
    position: absolute; inset: 0;
    background:
      radial-gradient(ellipse 70% 60% at 50% 0%, rgba(255,60,60,0.18) 0%, transparent 70%),
      radial-gradient(ellipse 40% 40% at 80% 80%, rgba(255,140,0,0.10) 0%, transparent 60%);
    pointer-events: none;
  }
  .hero-eyebrow {
    font-size: 0.8rem;
    font-weight: 600;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--c-accent);
    margin-bottom: 1rem;
    opacity: 0;
    animation: fadeUp .6s .2s forwards;
  }
  .hero-title {
    font-family: var(--ff-display);
    font-size: clamp(4rem, 12vw, 10rem);
    line-height: 0.92;
    letter-spacing: 0.02em;
    color: var(--c-text);
    opacity: 0;
    animation: fadeUp .7s .35s forwards;
  }

  .hero-title span { color: var(--c-accent); }
  .hero-sub {
    font-size: clamp(1rem, 2.5vw, 1.3rem);
    color: #a1a1aa;
    max-width: 560px;
    margin: 1.5rem auto 2.5rem;
    font-weight: 300;
    opacity: 0;
    animation: fadeUp .7s .5s forwards;
  }
  .hero-btns {
    display: flex; gap: 1rem; flex-wrap: wrap; justify-content: center;
    opacity: 0;
    animation: fadeUp .7s .65s forwards;
  }
    
  .btn-primary {
    background: var(--c-accent);
    color: #fff;
    font-family: var(--ff-body);
    font-size: 1rem;
    font-weight: 600;
    padding: 0.85rem 2.2rem;
    border-radius: 999px;
    text-decoration: none;
    transition: transform .2s, box-shadow .2s;
    animation: pulseGlow 2s infinite;
  }
  .btn-primary:hover { transform: translateY(-2px); box-shadow: 0 8px 28px rgba(255,60,60,0.35); }
  .btn-ghost {
    color: var(--c-text);
    font-family: var(--ff-body);
    font-size: 1rem;
    font-weight: 400;
    padding: 0.85rem 2.2rem;
    border-radius: 999px;
    border: 1px solid rgba(255,255,255,0.18);
    text-decoration: none;
    transition: background .2s;
  }
  .btn-ghost:hover { background: rgba(255,255,255,0.06); }
  .hero-date-bar {
    margin-top: 3.5rem;
    display: flex; gap: 2.5rem; justify-content: center; flex-wrap: wrap;
    opacity: 0;
    animation: fadeUp .7s .8s forwards;
  }
  .date-item { text-align: center; }
  .date-item .val {
    font-family: var(--ff-display);
    font-size: 1.8rem;
    letter-spacing: 0.04em;
    color: var(--c-accent2);
  }
  .date-item .lbl { font-size: 0.75rem; color: var(--c-muted); letter-spacing: 0.12em; text-transform: uppercase; }

  /* ── SECTION SHARED ── */
  section { padding: 6rem 5vw; }
  .section-tag {
    display: inline-block;
    font-size: 0.75rem; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase;
    color: var(--c-accent); margin-bottom: 0.75rem;
  }
  .section-title {
    font-family: var(--ff-display);
    font-size: clamp(2.5rem, 5vw, 4rem);
    letter-spacing: 0.02em;
    line-height: 1.05;
    margin-bottom: 1rem;
  }
  .section-lead {
    font-size: 1.05rem; color: #a1a1aa; font-weight: 300;
    max-width: 580px; margin-bottom: 3rem;
  }

  /* ── ABOUT ── */
  .about { background: var(--c-surface); }
  .about-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 1.5rem;
    margin-top: 3rem;
  }
  .about-card {
    background: var(--c-card);
    border: 1px solid var(--c-border);
    border-radius: var(--radius);
    padding: 1.75rem;
    transition: border-color .2s;
  }
  .about-card:hover { border-color: rgba(255,60,60,0.4); }
  .about-card .icon {
    width: 44px; height: 44px; border-radius: 10px;
    background: rgba(255,60,60,0.12);
    display: flex; align-items: center; justify-content: center;
    font-size: 1.4rem; margin-bottom: 1rem;
  }
  .about-card h3 { font-size: 1.05rem; font-weight: 600; margin-bottom: 0.4rem; }
  .about-card p { font-size: 0.9rem; color: #a1a1aa; line-height: 1.6; }

  /* ── PERKS ── */
  .perks-list {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 1.25rem;
    margin-top: 3rem;
  }
  .perk {
    display: flex; align-items: flex-start; gap: 1rem;
    background: var(--c-card);
    border: 1px solid var(--c-border);
    border-radius: var(--radius);
    padding: 1.25rem 1.5rem;
  }
  .perk-num {
    font-family: var(--ff-display);
    font-size: 2rem;
    line-height: 1;
    color: var(--c-accent);
    min-width: 36px;
  }
  .perk-body h4 { font-size: 1rem; font-weight: 600; margin-bottom: 0.25rem; }
  .perk-body p { font-size: 0.875rem; color: #a1a1aa; line-height: 1.55; }

  /* ── WHO CAN APPLY ── */
  .who { background: var(--c-surface); }
  .who-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 1rem;
    margin-top: 3rem;
  }
  .who-badge {
    background: var(--c-card);
    border: 1px solid var(--c-border);
    border-radius: var(--radius);
    padding: 1.5rem 1rem;
    text-align: center;
    text-decoration: none;
    color: var(--c-text);
    display: block;
    cursor: pointer;
    transition: border-color .2s, transform .2s;
  }
  .who-badge:hover {
    border-color: var(--c-accent);
    transform: translateY(-2px);
  }
  .who-badge .emoji { font-size: 2rem; margin-bottom: 0.5rem; display: block; }
  .who-badge span { font-size: 0.9rem; font-weight: 600; }

  /* ── TIMELINE ── */
  .timeline-list {
    position: relative;
    margin-top: 3rem;
    max-width: 700px;
  }
  .timeline-list::before {
    content: '';
    position: absolute;
    left: 16px; top: 8px; bottom: 8px;
    width: 2px;
    background: linear-gradient(to bottom, var(--c-accent), var(--c-accent2));
  }
  .tl-item {
    display: flex; gap: 2rem; align-items: flex-start;
    margin-bottom: 2rem; padding-left: 0;
  }
  .tl-dot {
    width: 34px; height: 34px; border-radius: 50%;
    background: var(--c-accent); flex-shrink: 0;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.75rem; font-weight: 700; color: #fff;
    position: relative; z-index: 1;
  }
  .tl-content h4 { font-weight: 600; font-size: 1rem; margin-bottom: 0.2rem; }
  .tl-content p { font-size: 0.875rem; color: #a1a1aa; }
  .tl-date { font-size: 0.75rem; color: var(--c-accent2); font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; margin-bottom: 0.2rem; }

  /* ── FORM ── */
  .form-section { background: var(--c-bg); }
  .form-wrap {
    max-width: 760px;
    margin: 0 auto;
    background: var(--c-card);
    border: 1px solid var(--c-border);
    border-radius: 20px;
    padding: 3rem 3.5rem;
  }
  .form-title {
    font-family: var(--ff-display);
    font-size: 2.5rem;
    letter-spacing: 0.03em;
    margin-bottom: 0.5rem;
  }
  .form-sub { font-size: 0.95rem; color: #a1a1aa; margin-bottom: 2.5rem; }

  .form-group { margin-bottom: 1.5rem; }
  .form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 1.25rem; }

  label {
    display: block;
    font-size: 0.8rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase;
    color: #a1a1aa; margin-bottom: 0.5rem;
  }
  label span { color: var(--c-accent); }

  input[type="text"],
  input[type="email"],
  input[type="url"],
  input[type="number"],
  select,
  textarea {
    width: 100%;
    background: var(--c-input-bg);
    border: 1px solid var(--c-border);
    border-radius: 8px;
    color: var(--c-text);
    font-family: var(--ff-body);
    font-size: 0.95rem;
    padding: 0.75rem 1rem;
    outline: none;
    transition: border-color .2s;
    -webkit-appearance: none;
    appearance: none;
  }
  input:focus, select:focus, textarea:focus { border-color: var(--c-accent); }
  
  select option { background: #18181c; }
  
  textarea { resize: vertical; min-height: 110px; line-height: 1.6; }

  .checkbox-group { display: flex; flex-direction: column; gap: 0.6rem; margin-top: 0.5rem; }
  
  .checkbox-item { display: flex; align-items: center; gap: 0.75rem; cursor: pointer; }
  
  .checkbox-item input[type="checkbox"] {
    width: 18px; height: 18px; accent-color: var(--c-accent); cursor: pointer; flex-shrink: 0;
  }
  .checkbox-item span { font-size: 0.9rem; }

  .form-divider { border: none; border-top: 1px solid var(--c-border); margin: 2rem 0; }

  .submit-btn {
  
    width: 100%;
    
    background: var(--c-accent);
    
    color: #fff;
    
    font-family: var(--ff-body);
    
    font-size: 1.05rem;
    
    font-weight: 700;
    
    letter-spacing: 0.05em;
    
    padding: 1rem;
    
    border: none;
    
    border-radius: 999px;
  } 
  @keyframes fadeUp {
  
    from {
        opacity: 0;
        transform: translateY(40px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
} 
@keyframes fadeIn {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
} 
@keyframes scaleUp {
    from {
        opacity: 0;
        transform: scale(0.9);
    }
    to {
        opacity: 1;
        transform: scale(1);
    }
}
  @keyframes slideLeft {
    from {
        opacity: 0;
        transform: translateX(80px);
    }

    to {
        opacity: 1;
        transform: translateX(0);
    }
}
.card-right {
    animation: slideLeft 1s ease forwards;
}
@keyframes slideRight {
    from {
        opacity: 0;
        transform: translateX(-80px);
    }

    to {
        opacity: 1;
        transform: translateX(0);
    }
}
.card-left {
    animation: slideRight 1s ease forwards;
}

@keyframes pulseGlow {

    0% {
        box-shadow: 0 0 0 rgba(255, 60, 60, 0);
    }

    50% {
        box-shadow:
            0 0 20px rgba(255, 60, 60, 0.6),
            0 0 40px rgba(255, 60, 60, 0.3);
    }

    100% {
        box-shadow: 0 0 0 rgba(255, 60, 60, 0);
    }

} 
@keyframes floating {

    0% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(-15px);
    }

    100% {
        transform: translateY(0px);
    }

} 
@keyframes rotateIn {

    from {
        opacity: 0;
        transform: rotate(-10deg) scale(.9);
    }

    to {
        opacity: 1;
        transform: rotate(0deg) scale(1);
    }

}

Out put 


<img width="940" height="529" alt="image" src="https://github.com/user-attachments/assets/abda9b82-28f2-46d6-8154-3d8db7a60771" />






<img width="940" height="529" alt="image" src="https://github.com/user-attachments/assets/23a7bcbf-981a-4b64-8000-14ee0ce68e6b" />







<img width="940" height="529" alt="image" src="https://github.com/user-attachments/assets/53f5931e-3b73-4e90-b561-1c59c3d87231" />







<img width="940" height="529" alt="image" src="https://github.com/user-attachments/assets/3efc195d-4674-4660-9be6-19aed457e81c" />




<img width="940" height="529" alt="image" src="https://github.com/user-attachments/assets/4b7d0341-afe9-40ff-955b-86579c2a02cb" />





<img width="940" height="529" alt="image" src="https://github.com/user-attachments/assets/7933f4b6-5029-4bcf-a76c-42897a4bbf79" />




<img width="940" height="529" alt="image" src="https://github.com/user-attachments/assets/6f558a4f-afea-4668-979e-f26140b32307" />




<img width="940" height="529" alt="image" src="https://github.com/user-attachments/assets/4ea261f6-74c4-4385-8600-36ac6bac7f7c" />




<img width="940" height="529" alt="image" src="https://github.com/user-attachments/assets/96ad1322-666e-4e82-83b2-b340b869f07a" />




<img width="940" height="529" alt="image" src="https://github.com/user-attachments/assets/8271ee6c-e74d-4e2e-9746-f0b110108a0c" />





