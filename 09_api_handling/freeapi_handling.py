# https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa0E1aml0ckZOaWttWE9mbHRYMm1NQjlfMDlvUXxBQ3Jtc0trTGcwRFdVYzNlYU9nZzVnbUlYbmJqTDhJNUpFRmlEUW93ZlFBMFM3Tlg4VUFRZXUxcmh2THFMdVVXNlU1ZVlISTBVdnBQMU5tem9Gcjd0QXdDNVVyTEtWWENfZFhSbWRFUlY5Wmp0ZFZtM2plams1WQ&q=https%3A%2F%2Ffreeapi.app%2F&v=g33-tYIs7zU
import requests
import json

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers"
    response = requests.get(url)
    data_json = response.json()
    
    if data_json['success'] == True and 'data' in data_json:
        data = data_json['data']
        user_data = data['data']
        for value in user_data:
            yield value
    else:
        raise Exception("Failed to fetch user data!")

def main():
    data = fetch_random_user()
    for i in data:
        user = i['name']
        country_item = i['location']
        print(f"User : {user['first']} {user['last']} from {country_item['country']}")
        # pass

if __name__ == "__main__":
    main()

    
