import requests
from urllib.parse import urlparse
import os
from dotenv import load_dotenv
import argparse


def shorten_link(token, long_url):
    api_endpoint = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {'Authorization': f'Bearer {token}'}
    payload = {
        'domain': 'bit.ly',
        'long_url': long_url,
    }
    response = requests.post(
        api_endpoint,
        headers=headers,
        json=payload,
    )
    response.raise_for_status()
    return response.json()['id']


def count_clicks(token: str, bitlink: str):
    api_endpoint = (
        f'https://api-ssl.bitly.com'
        f'/v4/bitlinks/{bitlink}/clicks/summary'
    )
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(
        api_endpoint,
        headers=headers,
    )
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(token, link):
    api_endpoint = (
        f'https://api-ssl.bitly.com'
        f'/v4/bitlinks/{link}'
    )
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(
        api_endpoint,
        headers=headers,
    )
    return response.ok


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'link',
        help='Long URL or Bitlink',
    )
    args = parser.parse_args()

    load_dotenv()
    token = os.getenv('BITLY_TOKEN')
    link = args.link

    parsed_link = urlparse(link)
    schemeless_link = f'{parsed_link.netloc}{parsed_link.path}'

    try:
        if is_bitlink(token, schemeless_link):
            display_msg = (
                f'Total clicks: '
                f'{count_clicks(token, schemeless_link)}'
            )
        else:
            display_msg = (
                f'Here is your new bitlink: '
                f'{shorten_link(token, link)}'
            )
    except requests.exceptions.HTTPError as error:
        display_msg = error

    print(display_msg)


if __name__ == '__main__':
    main()
