import unittest
from unittest.mock import patch
from flask import Flask

class MockApplicationTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = Flask(__name__)
        cls.app.config['TESTING'] = True
        cls.client = cls.app.test_client()

    def setUp(self):
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    @patch('flask.Flask.test_client')
    def test_home_redirect(self, mock_test_client):
        mock_test_client().get.return_value.status_code = 200
        mock_test_client().get.return_value.data = b'Login'
        response = mock_test_client().get('/home')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)

    @patch('flask.Flask.test_client')
    def test_dashboard_access_denied_without_login(self, mock_test_client):
        mock_test_client().get.return_value.status_code = 302
        response = mock_test_client().get('/dashboard')
        self.assertEqual(response.status_code, 302)

    @patch('flask.Flask.test_client')
    def test_about_page(self, mock_test_client):
        mock_test_client().get.return_value.status_code = 200
        mock_test_client().get.return_value.data = b'About'
        response = mock_test_client().get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About', response.data)

    @patch('flask.Flask.test_client')
    def test_registration_page(self, mock_test_client):
        mock_test_client().get.return_value.status_code = 200
        mock_test_client().get.return_value.data = b'Register'
        response = mock_test_client().get('/register')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Register', response.data)

    @patch('flask.Flask.test_client')
    def test_login_page(self, mock_test_client):
        mock_test_client().get.return_value.status_code = 200
        mock_test_client().get.return_value.data = b'Login'
        response = mock_test_client().get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)

    @patch('flask.Flask.test_client')
    def test_dummy_page(self, mock_test_client):
        mock_test_client().get.return_value.status_code = 200
        mock_test_client().get.return_value.data = b'Page Under Maintenance'
        response = mock_test_client().get('/dummy')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Page Under Maintenance', response.data)

    @patch('flask.Flask.test_client')
    def test_reset_password_invalid_token(self, mock_test_client):
        mock_test_client().get.return_value.status_code = 200
        mock_test_client().get.return_value.data = b'Invalid password reset link.'
        response = mock_test_client().get('/resetPassword/invalidtoken')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid password reset link.', response.data)
        
#this are the new test cases
    @patch('flask.Flask.test_client')
    def test_fetch_tasks(self, mock_test_client):
        mock_test_client().get.return_value.status_code = 200
        response = mock_test_client().get('/fetchTasks')
        self.assertEqual(response.status_code, 200)

    @patch('flask.Flask.test_client')
    def test_gpt_endpoint(self, mock_test_client):
        mock_test_client().get.return_value.status_code = 200
        mock_test_client().get.return_value.data = b'GPT Response'
        response = mock_test_client().get('/gpt')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'GPT Response', response.data)

    @patch('flask.Flask.test_client')
    def test_activity_log(self, mock_test_client):
        mock_test_client().get.return_value.status_code = 200
        response = mock_test_client().get('/activity')
        self.assertEqual(response.status_code, 200)

    @patch('flask.Flask.test_client')
    def test_settings_page(self, mock_test_client):
        mock_test_client().get.return_value.status_code = 200
        response = mock_test_client().get('/settings')
        self.assertEqual(response.status_code, 200)

    @patch('flask.Flask.test_client')
    def test_contact_submission(self, mock_test_client):
        mock_test_client().post.return_value.status_code = 200
        mock_test_client().post.return_value.data = b'Contact Submitted'
        response = mock_test_client().post('/contact', data={'message': 'Help needed'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Contact Submitted', response.data)

    @patch('flask.Flask.test_client')
    def test_reminders_scheduled(self, mock_test_client):
        mock_test_client().get.return_value.status_code = 200
        response = mock_test_client().get('/reminderscheduled')
        self.assertEqual(response.status_code, 200)

    @patch('flask.Flask.test_client')
    def test_profile_update(self, mock_test_client):
        mock_test_client().post.return_value.status_code = 200
        response = mock_test_client().post('/profile', data={'name': 'New Name'})
        self.assertEqual(response.status_code, 200)

    @patch('flask.Flask.test_client')
    def test_post_submission(self, mock_test_client):
        mock_test_client().post.return_value.status_code = 201
        response = mock_test_client().post('/post', data={'content': 'New post content'})
        self.assertEqual(response.status_code, 201)

    @patch('flask.Flask.test_client')
    def test_update_task_status(self, mock_test_client):
        mock_test_client().post.return_value.status_code = 200
        response = mock_test_client().post('/update_task_status', data={'task_id': '123', 'status': 'completed'})
        self.assertEqual(response.status_code, 200)

    @patch('flask.Flask.test_client')
    def test_recommendations_page(self, mock_test_client):
        mock_test_client().get.return_value.status_code = 200
        response = mock_test_client().get('/recommend')
        self.assertEqual(response.status_code, 200)

    @patch('flask.Flask.test_client')
    def test_edit_profile(self, mock_test_client):
        mock_test_client().post.return_value.status_code = 200
        response = mock_test_client().post('/editProfile', data={'bio': 'Updated bio'})
        self.assertEqual(response.status_code, 200)

    @patch('flask.Flask.test_client')
    def test_change_password(self, mock_test_client):
        mock_test_client().post.return_value.status_code = 200
        response = mock_test_client().post('/changePassword', data={'password': 'newpassword'})
        self.assertEqual(response.status_code, 200)

    @patch('flask.Flask.test_client')
    def test_notifications_page(self, mock_test_client):
        mock_test_client().get.return_value.status_code = 200
        response = mock_test_client().get('/notifications')
        self.assertEqual(response.status_code, 200)

    @patch('flask.Flask.test_client')
    def test_search_function(self, mock_test_client):
        mock_test_client().get.return_value.status_code = 200
        response = mock_test_client().get('/search', query_string={'query': 'test'})
        self.assertEqual(response.status_code, 200)

    @patch('flask.Flask.test_client')
    def test_task_details_page(self, mock_test_client):
        mock_test_client().get.return_value.status_code = 200
        response = mock_test_client().get('/task/1')
        self.assertEqual(response.status_code, 200)

    @patch('flask.Flask.test_client')
    def test_submit_feedback(self, mock_test_client):
        mock_test_client().post.return_value.status_code = 200
        response = mock_test_client().post('/feedback', data={'message': 'Great app!'})
        self.assertEqual(response.status_code, 200)

    @patch('flask.Flask.test_client')
    def test_task_deletion(self, mock_test_client):
        mock_test_client().post.return_value.status_code = 200
        response = mock_test_client().post('/delete_task', data={'task_id': '123'})
        self.assertEqual(response.status_code, 200)

    @patch('flask.Flask.test_client')
    def test_favorites_page(self, mock_test_client):
        mock_test_client().get.return_value.status_code = 200
        response = mock_test_client().get('/favorites')
        self.assertEqual(response.status_code, 200)

    @patch('flask.Flask.test_client')
    def test_save_draft(self, mock_test_client):
        mock_test_client().post.return_value.status_code = 201
        response = mock_test_client().post('/saveDraft', data={'content': 'Draft content'})
        self.assertEqual(response.status_code, 201)

    @patch('flask.Flask.test_client')
    def test_get_drafts(self, mock_test_client):
        mock_test_client().get.return_value.status_code = 200
        response = mock_test_client().get('/drafts')
        self.assertEqual(response.status_code, 200)

    #Test cases for dark mode feature
        @patch('flask.Flask.test_client')
    def test_theme_toggle_button_presence(self, mock_test_client):
        """Verify that the theme toggle button is present in the rendered HTML."""
        mock_test_client().get.return_value.status_code = 200
        mock_test_client().get.return_value.data = b'<button id="themeToggleButton" class="btn btn-primary">'
        response = mock_test_client().get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<button id="themeToggleButton" class="btn btn-primary">', response.data)

    @patch('flask.Flask.test_client')
    def test_theme_initial_load_light(self, mock_test_client):
        """Ensure light theme is applied when 'theme' in localStorage is 'light'."""
        mock_test_client().get.return_value.status_code = 200
        mock_test_client().get.return_value.data = b'main.css'
        response = mock_test_client().get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'main.css', response.data)

    @patch('flask.Flask.test_client')
    def test_theme_initial_load_dark(self, mock_test_client):
        """Ensure dark theme is applied when 'theme' in localStorage is 'dark'."""
        mock_test_client().get.return_value.status_code = 200
        mock_test_client().get.return_value.data = b'maindark.css'
        response = mock_test_client().get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'maindark.css', response.data)

    @patch('flask.Flask.test_client')
    def test_toggle_theme_to_dark(self, mock_test_client):
        """Simulate toggling the theme to dark mode and verify the changes."""
        mock_test_client().post.return_value.status_code = 200
        mock_test_client().post.return_value.data = b'maindark.css'
        response = mock_test_client().post('/toggle_theme', data={'currentTheme': 'light'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'maindark.css', response.data)

    @patch('flask.Flask.test_client')
    def test_toggle_theme_to_light(self, mock_test_client):
        """Simulate toggling the theme to light mode and verify the changes."""
        mock_test_client().post.return_value.status_code = 200
        mock_test_client().post.return_value.data = b'main.css'
        response = mock_test_client().post('/toggle_theme', data={'currentTheme': 'dark'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'main.css', response.data)

    @patch('flask.Flask.test_client')
    def test_icon_change_to_moon_on_dark(self, mock_test_client):
        """Ensure the theme icon updates to 'moon' when toggling to dark mode."""
        mock_test_client().post.return_value.status_code = 200
        mock_test_client().post.return_value.data = b'fa-moon'
        response = mock_test_client().post('/toggle_theme', data={'currentTheme': 'light'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'fa-moon', response.data)

    @patch('flask.Flask.test_client')
    def test_icon_change_to_sun_on_light(self, mock_test_client):
        """Ensure the theme icon updates to 'sun' when toggling to light mode."""
        mock_test_client().post.return_value.status_code = 200
        mock_test_client().post.return_value.data = b'fa-sun'
        response = mock_test_client().post('/toggle_theme', data={'currentTheme': 'dark'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'fa-sun', response.data)

if __name__ == '__main__':
    unittest.main()
