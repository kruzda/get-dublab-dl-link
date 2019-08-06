from botocore.vendored import requests

DUBLAB_API_EP = "https://api-1.dublab.com/wp-json/lazystate/v1"

def lambda_handler(event, context):
    path = str(event['path'])
    r = requests.get(''.join([DUBLAB_API_EP, path]))
    link = r.json()[path]['audio']['url']
    return {
        "statusCode": r.status_code,
        "headers": {"content-type": "text/html"},
        "body": '<a href="{link}">{link}</a>'.format(link=link)
    }
