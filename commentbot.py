import requests

# Replace {access_token} with a valid access token
# Replace {post_id} with the ID of the post
# Replace {message} with the comment you want to post

url = f'https://graph.facebook.com/{post_id}/comments'

payload = {'access_token': '{access_token}', 'message': '{message}'}

response = requests.post(url, data=payload)

if response.status_code == 200:
    print('Comment posted successfully')
else:
    print('Error posting comment')
    print(response.json())
