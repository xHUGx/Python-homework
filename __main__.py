import argparse
import sys
import aiohttp
import asyncio

arg_parse = argparse.ArgumentParser()
arg_parse.add_argument('url', type=str,)
arg_parse.add_argument('-X', dest='method', type=str, default='GET')
arg_parse.add_argument('--schema', dest='schema', type=str, default='http://')


async def main():
    namespace = arg_parse.parse_args(sys.argv[1:])

    url = namespace.url
    if 'http://' not in url or 'https://' not in url:
        url = namespace.schema + url

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:], "...")


asyncio.run(main())