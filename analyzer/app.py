from azure.storage.blob import BlobServiceClient
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from flask import Flask, render_template, request, redirect, url_for, session
import os
import sys
import requests
from PIL import Image
from io import BytesIO
import base64
from base64 import b64encode

app = Flask(__name__)

# Azure Blob Storage configuration
blob_service_connection_string = "DefaultEndpointsProtocol=https;AccountName=storageimages1;AccountKey=ftSkqZcZxy7mZKFVSUpUniMzTicd7pwT5hD6XwOMWODLKQghmBbJPpfid9Gg+Rgi2SETRhsOXNZs+AStmpCdVA==;EndpointSuffix=core.windows.net"
container_name = "images"

# Computer Vision configuration
subscription_key = "cef3c41caa984578bb00418ad772f782"
endpoint = "https://custvision-demo.cognitiveservices.azure.com/"
analyze_url = endpoint + "vision/v3.1/analyze"

# ...

# Helper function to upload image to Azure Blob Storage
def upload_to_blob_storage(image_data, file_name):
    blob_service_client = BlobServiceClient.from_connection_string(blob_service_connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
    blob_client.upload_blob(image_data, overwrite=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the file from the request
        file = request.files['file']

        # Read the image into a byte array
        image_data = file.read()

        # Generate a unique file name or use the original file name
        file_name = file.filename

        # Upload the image to Azure Blob Storage
        upload_to_blob_storage(image_data, file_name)

        # Redirect to the result page with the image file name
        return redirect(url_for('result', file_name=file_name))

    return render_template("index.html")
@app.route("/result")
def result():
    file_name = request.args.get('file_name', '')

    # Download the image from Azure Blob Storage
    blob_service_client = BlobServiceClient.from_connection_string(blob_service_connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
    image_data = blob_client.download_blob().readall()

    # Encode image data in Base64
    encoded_image = b64encode(image_data).decode('utf-8')

    # Analyze the image using Computer Vision
    headers = {'Ocp-Apim-Subscription-Key': subscription_key,
               'Content-Type': 'application/octet-stream'}
    params = {'visualFeatures': 'Categories,Description,Color'}
    response = requests.post(
        analyze_url, headers=headers, params=params, data=image_data)
    response.raise_for_status()

    # The 'analysis' object contains various fields that describe the image.
    analysis = response.json()
    image_caption = analysis["description"]["captions"][0]["text"].capitalize()

    return render_template("result.html", image_caption=image_caption, encoded_image=encoded_image)
# @app.route("/result")
# def result():
#     file_name = request.args.get('file_name', '')

#     # Download the image from Azure Blob Storage
#     blob_service_client = BlobServiceClient.from_connection_string(blob_service_connection_string)
#     blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
#     image_data = blob_client.download_blob().readall()

#     # Analyze the image using Computer Vision
#     headers = {'Ocp-Apim-Subscription-Key': subscription_key,
#                'Content-Type': 'application/octet-stream'}
#     params = {'visualFeatures': 'Categories,Description,Color'}
#     response = requests.post(
#         analyze_url, headers=headers, params=params, data=image_data)
#     response.raise_for_status()

#     # The 'analysis' object contains various fields that describe the image.
#     analysis = response.json()
#     image_caption = analysis["description"]["captions"][0]["text"].capitalize()

#     # Display the image and overlay it with the caption.
#     image = Image.open(BytesIO(image_data))

#     return render_template("result.html", image_caption=image_caption, image=image)

if __name__ == "__main__":
    app.run(debug=True)