import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import User, Post


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Home Page', response.data)

    def test_register(self):
        response = self.client.post('/auth/register', data={
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'password123',
            'confirm_password': 'password123'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'This field is required.', response.data)
        self.assertNotIn(b'Invalid', response.data)
        with self.app.app_context():
            user = User.query.filter_by(username='newuser').first()
            self.assertIsNotNone(user)
            self.assertEqual(user.email, 'newuser@example.com')

    def test_login(self):
        with self.app.app_context():
            user = User(username='testuser', email='test@example.com')
            user.set_password('password123')
            db.session.add(user)
            db.session.commit()

        response = self.client.post('/auth/login', data={
            'username': 'testuser',
            'password': 'password123'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/')
        self.assertIn(b'Logout', response.data)

    def test_create_post(self):
        with self.app.app_context():
            user = User(username='testuser', email='test@example.com')
            user.set_password('password123')
            db.session.add(user)
            db.session.commit()

        self.client.post('/auth/login', data={
            'username': 'testuser',
            'password': 'password123'
        })

        response = self.client.post('/posts/post/new', data={
            'title': 'New Post',
            'content': 'This is a new post.'
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Your post has been created!', response.data)
        with self.app.app_context():
            post = Post.query.filter_by(title='New Post').first()
            self.assertIsNotNone(post)
            self.assertEqual(post.content, 'This is a new post.')


if __name__ == '__main__':
    unittest.main()
