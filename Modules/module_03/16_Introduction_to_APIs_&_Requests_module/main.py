import requests



# ------------------------------------ Get ----------------------------------- #

response = requests.get("https://jsonplaceholder.typicode.com/posts")

print(response.text)
print("Request completed successfully.")
print(f"Status Code: {response.status_code}")


# ---------------------------------------------------------------------------- #

# ------------------------------------ Post ---------------------------------- #

data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
print(response.text)
print("Post request completed successfully.")


# ---------------------------------------------------------------------------- #

data = [
  {
  "name" : "Shahzad",
  "gmail" : "muhammadshahzad45435@gmail.com"
},
  {
  "name" : "Zahid",
  "gmail" : "zahid@gmail.com"
},

]
response  = requests.post("https://httpbin.org/post", json=data)
print(response.text)
print("Post request completed successfully.")


# ---------------------------------------------------------------------------- #


url = "https://jsonplaceholder.typicode.com/posts"

deta = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}


response = requests.post(url, json=deta)
print(response.status_code)



# ---------------------------------------------------------------------------- #


url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

if  response.status_code == 200:
    print("Request was successful.")
    print(response.json())
else:
    print("Request failed with status code:", response.status_code)


# ---------------------------------------------------------------------------- #



try:
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
    print("Request was successful.")
    print(response.json())
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
