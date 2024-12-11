from azure.storage.blob import BlobServiceClient

connection_string = "DefaultEndpointsProtocol=https;AccountName=gakudoaiappgroup649;AccountKey=ZmmYyp1QQP92Y+XDcqeKgWAp5RhmNXhXbA08bGWywWtrm4SuUymmcgIn8QntRYa7E8LP3i11Z1RD+AStRgSeTA==;EndpointSuffix=core.windows.net"
container_name = "gai-report-blob"
# Initialize the BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)

# Upload multiple files
def upload_files(file_paths):
    for file_path in file_paths:
        file_name = file_path.split("/")[-1]
        blob_client = container_client.get_blob_client(blob=file_name)
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data)
        print(f"Uploaded: {file_name}")

# Example file paths to upload
file_paths = ["mayank.pdf"]
upload_files(file_paths)