# import requests

# def send_to_backend(data):

#     url = "http://localhost:5000/api/add-scholarship"

#     for scholarship in data:

#         response = requests.post(url, json=scholarship)

#         print("Sent:", scholarship["title"], "| Status:", response.status_code)


import requests

def send_to_backend(data):
    url = "http://localhost:50001/api/scholarships/"  # API endpoint
    for scholarship in data:
        try:
            response = requests.post(url, json=scholarship)
            if response.status_code == 201:
                print("Added:", scholarship['title'])
            else:
                print("Failed:", scholarship['title'], response.status_code, response.text)
        except Exception as e:
            print("Error sending:", scholarship['title'], e)