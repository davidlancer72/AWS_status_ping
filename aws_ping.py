import requests

def get_aws_status():
    url = 'https://status.aws.amazon.com/data.json'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error fetching AWS status:", e)
        return None

def main():
    aws_status = get_aws_status()
    if aws_status:
        print("Current AWS service status:")
        for service in aws_status['services']:
            print(f"{service['serviceName']}: {service['status']}")

if __name__ == "__main__":
    main()
