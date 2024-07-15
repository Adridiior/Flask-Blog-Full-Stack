from app import create_app, db
from app.models import User, Post

app = create_app()
app.app_context().push()

# Aggiungi un utente
u = User(username='testuser', email='test@example.com')
u.set_password('password')
db.session.add(u)

# Aggiungi un post
p = Post(title='First Post', body='This is the body of the first post.', author=u)
db.session.add(p)

# Committa le modifiche
db.session.commit()

print("Database popolato con dati di esempio.")
