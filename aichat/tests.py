from django.test import TestCase, Client
from django.urls import reverse


class ChatPageTestCase(TestCase):
    def test_chat_page_loads(self):
        client = Client()
        url = reverse('chat')
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat.html')

    def test_ajax_view_returns_json_response(self):
        client = Client()
        url = reverse('ajax')
        response = client.post(url, {'text': 'Hello'})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'data': 'Response from OpenAI API'})
