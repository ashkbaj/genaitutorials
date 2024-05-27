from datetime import datetime
from api.models import Post
from api import db, app

current_date = datetime.today().date()
posts = []
new_post = Post(title="Flipkart System Design", description="system design blog from Flipkart", created_at=current_date)
with app.app_context():
    db.session.add(new_post)
    db.session.commit()