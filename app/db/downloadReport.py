from azure.storage.blob import generate_blob_sas, BlobSasPermissions
from datetime import datetime, timedelta, timezone
from azure.storage.blob import BlobServiceClient
from fastapi.encoders import jsonable_encoder

connection_string = "DefaultEndpointsProtocol=https;AccountName=gakudoaiappgroup649;AccountKey=ZmmYyp1QQP92Y+XDcqeKgWAp5RhmNXhXbA08bGWywWtrm4SuUymmcgIn8QntRYa7E8LP3i11Z1RD+AStRgSeTA==;EndpointSuffix=core.windows.net"
container_name = "gai-report-blob"
# Initialize the BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)

# Function to generate a SAS URL for a given file
def generate_report_download_url(account_name= "gakudoaiappgroup649", blob_name="arvind1.pdf", container_name=container_name):
    sas_token = generate_blob_sas(
        account_name="gakudoaiappgroup649",
        container_name=container_name,
        blob_name=blob_name,
        account_key="ZmmYyp1QQP92Y+XDcqeKgWAp5RhmNXhXbA08bGWywWtrm4SuUymmcgIn8QntRYa7E8LP3i11Z1RD+AStRgSeTA==",
        permission=BlobSasPermissions(read=True),
        expiry=datetime.now(timezone.utc) + timedelta(hours=24)
    )
    blob_url = f"https://{account_name}.blob.core.windows.net/{container_name}/{blob_name}?{sas_token}"
    print("blob_url:::", {"url":blob_url})
    return {"url":blob_url}



# Initialize Azure BlobServiceClient
def check_blob_exists(blob_name: str) -> bool:
    """
    Check if the blob exists in the container.
    """
    try:
        # Get a BlobClient to interact with the blob
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        # Try to get the blob properties, which will raise an error if it doesn't exist
        blob_client.get_blob_properties()
        return True  # Blob exists
    except Exception as e:
        print(f"Error checking blob: {e}")
        return False  # Blob does not exist


