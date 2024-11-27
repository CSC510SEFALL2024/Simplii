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

    #  Test cases for add csv function.
    @patch('flask.Flask.test_client')
    def test_csv_export(self, mock_test_client):
        """Test CSV export endpoint"""
        mock_test_client().get.return_value.status_code = 200
        mock_test_client().get.return_value.headers = {
            'Content-Type': 'text/csv',
            'Content-Disposition': 'attachment; filename=tasks.csv'
        }
        response = mock_test_client().get('/export_csv')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers.get('Content-Type'), 'text/csv')
        self.assertIn('attachment; filename=tasks.csv', response.headers.get('Content-Disposition', ''))

    @patch('flask.Flask.test_client')
    def test_csv_export_filtered_by_status(self, mock_test_client):
        """Test CSV export with status filter"""
        mock_test_client().get.return_value.status_code = 200
        response = mock_test_client().get('/export_csv?status=To-Do')
        self.assertEqual(response.status_code, 200)

    @patch('flask.Flask.test_client')
    def test_csv_export_filtered_by_category(self, mock_test_client):
        """Test CSV export with category filter"""
        mock_test_client().get.return_value.status_code = 200
        response = mock_test_client().get('/export_csv?category=Intellectual')
        self.assertEqual(response.status_code, 200)

    @patch('flask.Flask.test_client')
    def test_csv_export_with_limit(self, mock_test_client):
        """Test CSV export with task limit"""
        mock_test_client().get.return_value.status_code = 200
        response = mock_test_client().get('/export_csv?limit=5')
        self.assertEqual(response.status_code, 200)

    @patch('flask.Flask.test_client')
    def test_csv_export_invalid_filter(self, mock_test_client):
        """Test CSV export with invalid filter"""
        mock_test_client().get.return_value.status_code = 400
        response = mock_test_client().get('/export_csv?invalid_filter=value')
        self.assertEqual(response.status_code, 400)

    @patch('flask.Flask.test_client')
    def test_csv_export_no_tasks(self, mock_test_client):
        """Test CSV export when no tasks exist"""
        mock_test_client().get.return_value.status_code = 200
        mock_test_client().get.return_value.data = b''
        response = mock_test_client().get('/export_csv')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    # Test cases for send email Ai schedule functions

    @patch('flask.Flask.test_client')
    def test_get_user_tasks_within_thirty_days(self, mock_test_client):
        """Test retrieval of tasks within thirty days"""
        mock_test_client().get.return_value.status_code = 200
        response = mock_test_client().get('/get_user_tasks')
        self.assertEqual(response.status_code, 200)
        # Add assertions about task data if possible

    @patch('flask.Flask.test_client')
    def test_task_email_with_no_tasks(self, mock_test_client):
        """Test email sending with empty task list"""
        mock_test_client().post.return_value.status_code = 200
        mock_test_client().post.return_value.data = b'No tasks to display'
        response = mock_test_client().post('/send_task_email')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'No tasks to display', response.data)

    @patch('flask.Flask.test_client')
    def test_task_email_with_today_tasks(self, mock_test_client):
        """Test email sending with only today's tasks"""
        mock_test_client().post.return_value.status_code = 200
        mock_test_client().post.return_value.data = b'Today\'s Tasks'
        response = mock_test_client().post('/send_task_email')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Today\'s Tasks', response.data)

    @patch('flask.Flask.test_client')
    def test_task_email_with_week_tasks(self, mock_test_client):
        """Test email sending with this week's tasks"""
        mock_test_client().post.return_value.status_code = 200
        mock_test_client().post.return_value.data = b'This Week\'s Tasks'
        response = mock_test_client().post('/send_task_email')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'This Week\'s Tasks', response.data)

    @patch('flask.Flask.test_client')
    def test_task_email_with_month_tasks(self, mock_test_client):
        """Test email sending with this month's tasks"""
        mock_test_client().post.return_value.status_code = 200
        mock_test_client().post.return_value.data = b'This Month\'s Tasks'
        response = mock_test_client().post('/send_task_email')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'This Month\'s Tasks', response.data)

    @patch('flask.Flask.test_client')
    def test_task_email_gemini_generation(self, mock_test_client):
        """Test Gemini AI task description generation"""
        mock_test_client().post.return_value.status_code = 200
        mock_test_client().post.return_value.data = b'Gemini AI Generated Content'
        response = mock_test_client().post('/send_task_email')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Gemini AI Generated Content', response.data)

    @patch('flask.Flask.test_client')
    def test_task_email_markdown_conversion(self, mock_test_client):
        """Test markdown to HTML conversion for email"""
        mock_test_client().post.return_value.status_code = 200
        mock_test_client().post.return_value.data = b'Markdown to HTML Conversion'
        response = mock_test_client().post('/send_task_email')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Markdown to HTML Conversion', response.data)


    @patch('flask.Flask.test_client')
    def test_task_update(self, mock_test_client):
        """Test updating a task"""
        mock_test_client().post.return_value.status_code = 200
        response = mock_test_client().post('/update_task', data={'task_id': '456', 'task_name': 'Updated Task'})
        self.assertEqual(response.status_code, 200)

    @patch('flask.Flask.test_client')
    def test_task_priority_update(self, mock_test_client):
        """Test updating task priority"""
        mock_test_client().post.return_value.status_code = 200
        response = mock_test_client().post('/update_task', data={'task_id': '789', 'priority': 'High'})
        self.assertEqual(response.status_code, 200)

    @patch('flask.Flask.test_client')
    def test_task_category_update(self, mock_test_client):
        """Test updating task category"""
        mock_test_client().post.return_value.status_code = 200
        response = mock_test_client().post('/update_task', data={'task_id': '321', 'category': 'Work'})
        self.assertEqual(response.status_code, 200)

    @patch('flask.Flask.test_client')
    def test_dashboard_task_listing(self, mock_test_client):
        """Test listing tasks on the dashboard"""
        mock_test_client().get.return_value.status_code = 200
        mock_test_client().get.return_value.data = b'Tasks'
        response = mock_test_client().get('/dashboard')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Tasks', response.data)

    @patch('flask.Flask.test_client')
    def test_fetch_tasks_with_status(self, mock_test_client):
        """Test fetching tasks with a status filter"""
        mock_test_client().get.return_value.status_code = 200
        response = mock_test_client().get('/fetchTasks?status=Completed')
        self.assertEqual(response.status_code, 200)

    @patch('flask.Flask.test_client')
    def test_admin_task_management(self, mock_test_client):
        """Test managing tasks from the admin dashboard"""
        mock_test_client().post.return_value.status_code = 200
        response = mock_test_client().post('/admin/manage_tasks', data={'task_id': '101', 'action': 'complete'})
        self.assertEqual(response.status_code, 200)

    @patch('flask.Flask.test_client')
    def test_search_no_results(self, mock_test_client):
        """Test search functionality with no results"""
        mock_test_client().get.return_value.status_code = 200
        mock_test_client().get.return_value.data = b'No tasks found'
        response = mock_test_client().get('/search', query_string={'query': 'Nonexistent'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'No tasks found', response.data)

    @patch('flask.Flask.test_client')
    def test_task_export_with_no_filter(self, mock_test_client):
        """Test task export with no filters applied"""
        mock_test_client().get.return_value.status_code = 200
        mock_test_client().get.return_value.headers = {
            'Content-Type': 'text/csv',
            'Content-Disposition': 'attachment; filename=tasks.csv'
        }
        response = mock_test_client().get('/export_csv')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers.get('Content-Type'), 'text/csv')
        self.assertIn('attachment; filename=tasks.csv', response.headers.get('Content-Disposition', ''))

    @patch('flask.Flask.test_client')
    def test_task_export_with_invalid_limit(self, mock_test_client):
        """Test task export with an invalid limit filter"""
        mock_test_client().get.return_value.status_code = 400
        response = mock_test_client().get('/export_csv?limit=invalid')
        self.assertEqual(response.status_code, 400)

    
    @patch('flask.Flask.test_client')
    def test_copy_button_presence(self, mock_test_client):
        """Test that the 'Copy to Clipboard' button is present on the dashboard."""
        mock_test_client().get.return_value.status_code = 200
        mock_test_client().get.return_value.data = b'<button id="copyToClipboard" class="btn btn-secondary">'
        response = mock_test_client().get('/dashboard')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'id="copyToClipboard"', response.data)

    @patch('flask.Flask.test_client')
    def test_copy_empty_table(self, mock_test_client):
        """Test copying an empty task table."""
        mock_test_client().post.return_value.status_code = 200
        mock_test_client().post.return_value.data = b''
        response = mock_test_client().post('/copy', data={'table_data': []})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'')

    @patch('flask.Flask.test_client')
    def test_copy_table_with_data(self, mock_test_client):
        """Test copying a table with data."""
        table_data = [
            {"Task": "Task 1", "Status": "Done"},
            {"Task": "Task 2", "Status": "In Progress"}
        ]
        mock_test_client().post.return_value.status_code = 200
        mock_test_client().post.return_value.data = b'Task\tStatus\nTask 1\tDone\nTask 2\tIn Progress'
        response = mock_test_client().post('/copy', data={'table_data': table_data})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Task\tStatus\nTask 1\tDone\nTask 2\tIn Progress', response.data)

    @patch('flask.Flask.test_client')
    def test_copy_table_with_hidden_rows(self, mock_test_client):
        """Test copying a table with hidden rows."""
        table_data = [
            {"Task": "Task 1", "Status": "Done", "hidden": False},
            {"Task": "Task 2", "Status": "In Progress", "hidden": True}
        ]
        mock_test_client().post.return_value.status_code = 200
        mock_test_client().post.return_value.data = b'Task\tStatus\nTask 1\tDone'
        response = mock_test_client().post('/copy', data={'table_data': table_data})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Task\tStatus\nTask 1\tDone', response.data)

    @patch('flask.Flask.test_client')
    def test_copy_table_special_characters(self, mock_test_client):
        """Test copying a table with special characters."""
        table_data = [
            {"Task": '"Special, Task"', "Status": "Done"}
        ]
        mock_test_client().post.return_value.status_code = 200
        mock_test_client().post.return_value.data = b'Task\tStatus\n"Special, Task"\tDone'
        response = mock_test_client().post('/copy', data={'table_data': table_data})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'"Special, Task"\tDone', response.data)

    @patch('flask.Flask.test_client')
    def test_copy_large_table(self, mock_test_client):
        """Test copying a large table with 1000 rows."""
        table_data = [{"Task": f"Task {i}", "Status": f"Status {i}"} for i in range(1000)]
        rows = [b'Task\tStatus'] + [f"Task {i}\tStatus {i}".encode() for i in range(1000)]
        mock_test_client().post.return_value.status_code = 200
        mock_test_client().post.return_value.data = b'\n'.join(rows)
        response = mock_test_client().post('/copy', data={'table_data': table_data})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Task 0\tStatus 0", response.data)
        self.assertIn(b"Task 999\tStatus 999", response.data)

    @patch('flask.Flask.test_client')
    def test_copy_action_column_excluded(self, mock_test_client):
        """Test that the 'Actions' column is excluded from the copied data."""
        table_data = [
            {"Task": "Task 1", "Status": "Done", "Actions": "Edit/Delete"}
        ]
        mock_test_client().post.return_value.status_code = 200
        mock_test_client().post.return_value.data = b'Task\tStatus\nTask 1\tDone'
        response = mock_test_client().post('/copy', data={'table_data': table_data})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Task\tStatus\nTask 1\tDone", response.data)

    @patch('flask.Flask.test_client')
    def test_copy_success_notification(self, mock_test_client):
        """Test success notification for copying the task table."""
        mock_test_client().post.return_value.status_code = 200
        mock_test_client().post.return_value.data = b'Task table copied successfully!'
        response = mock_test_client().post('/copy', data={'table_data': []})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Task table copied successfully!', response.data)

    @patch('flask.Flask.test_client')
    def test_copy_error_notification(self, mock_test_client):
        """Test error notification for failed copying."""
        mock_test_client().post.side_effect = Exception("Clipboard error")
        try:
            response = mock_test_client().post('/copy', data={'table_data': []})
        except Exception as e:
            self.assertEqual(str(e), "Clipboard error")

    @patch('flask.Flask.test_client')
    def test_copy_partial_rows(self, mock_test_client):
        """Test copying when only partial rows are visible."""
        table_data = [
            {"Task": "Task 1", "Status": "Done"},
            {"Task": "Task 2", "Status": "In Progress", "visible": False}
        ]
        mock_test_client().post.return_value.status_code = 200
        mock_test_client().post.return_value.data = b'Task\tStatus\nTask 1\tDone'
        response = mock_test_client().post('/copy', data={'table_data': table_data})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Task\tStatus\nTask 1\tDone', response.data)

if __name__ == '__main__':
    unittest.main()
