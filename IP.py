# coding=utf-8


import requests

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Safari/605.1.15'}
error = False
try:
    source = requests.get('https://wtfismyip.com/json', headers=header)
except:
    error = True
    print('Network error, please lower connection frequency or check network status.')
formatted = source.json()
formatted['IP'] = formatted.pop('YourFuckingIPAddress')
formatted['Host'] = formatted.pop('YourFuckingHostname')
formatted['Location'] = formatted.pop('YourFuckingLocation')
formatted['Code'] = formatted.pop('YourFuckingCountryCode')
formatted['ISP'] = formatted.pop('YourFuckingISP')
formatted['Tor'] = formatted.pop('YourFuckingTorExit')


def show():
    """Print overall data, if connection error, return -1."""
    if error:
        return -1
    else:
        print('IP Address:', formatted['IP'])
        print('Host Name:', formatted['Host'])
        print('IP Location:', formatted['Location'])
        print('Country Code:', formatted['Code'])
        print('ISP:', formatted['ISP'])
        print('Is Tor Exit:', formatted['Tor'])


def overall():
    """Return a dictionary containing overall data, if connection error, return -1."""
    if error:
        return -1
    else:
        return formatted


def get(string: str = 'IP'):
    """Return a string containing specific data requested by the get(), if didn't specialize any string for requests, return IP address by default, if connection error, return -1."""
    if error:
        return -1
    else:
        if string in formatted.keys():
            return formatted[string]
        else:
            return -1
