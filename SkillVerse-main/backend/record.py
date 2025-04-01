import ipfshttpclient

# Connect to the local IPFS node
client = ipfshttpclient.connect("/ip4/127.0.0.1/tcp/5001/http")

def upload_to_ipfs(file_path):
    """Uploads a file to IPFS and returns its CID (Content Identifier)."""
    try:
        res = client.add(file_path)
        return res['Hash']  # Unique CID
    except Exception as e:
        return str(e)

def retrieve_from_ipfs(cid, output_path):
    """Retrieves a file from IPFS using its CID and saves it locally."""
    try:
        client.get(cid, output_path)
        return f"File saved to {output_path}"
    except Exception as e:
        return str(e)

# Example Usage
file_hash = upload_to_ipfs("medical_record.txt")
print(f"File uploaded! IPFS CID: {file_hash}")

retrieval_status = retrieve_from_ipfs(file_hash, "downloaded_medical_record.txt")
print(retrieval_status)