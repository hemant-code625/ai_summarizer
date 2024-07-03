# Install necessary libraries
# !pip install torch
# !pip install tensorflow
# !pip install tf-keras

# Verify TensorFlow installation
import tensorflow as tf
print(f"TensorFlow version: {tf.__version__}")

# Verify PyTorch installation
import torch
print(f"PyTorch version: {torch.__version__}")

# Import pipeline from transformers
from transformers import pipeline

# Create summarization pipeline
summarizer = pipeline('summarization', model="facebook/bart-large-cnn")

# Test the summarizer
text = "What is an Access Token? An access token is a credential used to access protected resources on behalf of a user. It is typically a short-lived token, containing information about the user and the permissions they have. When a user logs into an application, they receive an access token, which is then used to authenticate their requests to the server. What is a Refresh Token? A refresh token is a credential used to obtain a new access token without requiring the user to re-authenticate or login again. It is typically long-lived and is stored encrypted in the database. When an access token expires, the client can use the refresh token to generate new session from the server. How I use these tokens in my project?First, I created a register controller. Once a user registers, they are redirected to a login endpoint. The login controller checks if the registered user exists in the database and if the password is correct. If everything is fine, it generates a refresh token and an access token using JWT (jsonWebToken). These tokens are securely stored in the client’s cookies, with only the refresh token saved in the database. When the access token expires, the user doesn’t need to log in again manually. Instead, an endpoint uses the details from the cookies to query the database and check if the refresh Token matches the one stored in the cookies. If they match, a new access Token and refresh Token are generated. The new refresh Token is saved in the database, and the cookies are updated.  For accessing protected endpoints, the access Token is decoded using the jwt.verify(). The user ID and roles/privileges are already included in the token, eliminating the need for an additional database query to check the user’s privileges. This makes the process more efficient and reduces unnecessary database queries. Feel free to share your thoughts or ask any questions in the comments below!"

summary = summarizer(text)
print(summary)
