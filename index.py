from botocore.vendored import requests

DUBLAB_API_EP = "https://api-1.dublab.com/wp-json/lazystate/v1"

def handler(event, context):
    if type(event) != NoneType:
        path = str(event['path'])
    else:
        path = "/archive/ale-elevation-through-sound-live-from-tunein-studios-11-18-15"
    r = requests.get(''.join([DUBLAB_API_EP, path]))
    link = r.json()[path]['audio']['url']
    return {
        "statusCode": r.status_code,
        "headers": {"content-type": "text/html"},
        "body": '<a href="{link}">{link}</a>'.format(link=link)
    }
