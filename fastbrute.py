import argparse
import aiohttp
import asyncio
import sys

# Banner
BANNER = """
███████╗ █████╗ ███████╗████████╗██████╗ ██████╗ ██╗   ██╗████████╗███████╗
██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝
█████╗  ███████║███████╗   ██║   ██████╔╝██████╔╝██║   ██║   ██║   █████╗  
██╔══╝  ██╔══██║╚════██║   ██║   ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  
██║     ██║  ██║███████║   ██║   ██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗
╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝
Created by therealslimshady
https://github.com/therealslimshady0
https://x.com/dare4lslimshady
"""

async def request_url(session, url, verbose, no_error):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                print(f"[200] {url}")
            elif response.status == 403:
                print(f"[403] {url}")
            elif response.status != 404:
                print(f"[{response.status}] {url}")
    except aiohttp.ClientError as e:
        if verbose:
            print(f"[ERROR] {url} - {e}")
        elif not no_error:
            print(f"[ERROR] {url}")

async def brute_force_directories(base_url, wordlist, threads, verbose, no_error, delay):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for path in wordlist:
            url = f"{base_url}/{path.strip()}"
            tasks.append(request_url(session, url, verbose, no_error))
            if delay > 0:
                await asyncio.sleep(delay / 1000.0)
            if len(tasks) >= threads:
                await asyncio.gather(*tasks)
                tasks = []
        if tasks:
            await asyncio.gather(*tasks)

async def brute_force_vhosts(domain, wordlist, threads, verbose, no_error, delay):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for subdomain in wordlist:
            url = f"http://{subdomain.strip()}.{domain}"
            tasks.append(request_url(session, url, verbose, no_error))
            if delay > 0:
                await asyncio.sleep(delay / 1000.0)
            if len(tasks) >= threads:
                await asyncio.gather(*tasks)
                tasks = []
        if tasks:
            await asyncio.gather(*tasks)

def read_wordlist(wordlist_file):
    with open(wordlist_file, 'r') as file:
        return file.readlines()

def main():
    parser = argparse.ArgumentParser(description='FastBrute: A fast web directory and vhost brute-forcer.')
    parser.add_argument('-u', '--url', help='Base URL to brute-force directories (e.g., http://example.com)', required=False)
    parser.add_argument('-d', '--domain', help='Domain to brute-force vhosts (e.g., example.com)', required=False)
    parser.add_argument('-w', '--wordlist', help='Path to the wordlist file', required=True)
    parser.add_argument('-t', '--threads', help='Number of concurrent tasks to use', type=int, default=100)
    parser.add_argument('-o', '--output', help='Output file to write results to', type=str, default=None)
    parser.add_argument('--delay', help='Time each thread waits between requests (e.g., 1500ms)', type=int, default=0)
    parser.add_argument('--no-error', help='Don\'t display errors', action='store_true')
    parser.add_argument('--no-progress', help='Don\'t display progress', action='store_true')
    parser.add_argument('--no-color', help='Disable color output', action='store_true')
    parser.add_argument('-q', '--quiet', help='Don\'t print the banner and other noise', action='store_true')
    parser.add_argument('-v', '--verbose', help='Verbose output (errors)', action='store_true')

    args = parser.parse_args()

    if not args.quiet:
        print(BANNER)

    wordlist = read_wordlist(args.wordlist)

    if args.url:
        print(f"Starting directory brute-force on {args.url} with wordlist {args.wordlist}")
        asyncio.run(brute_force_directories(args.url, wordlist, args.threads, args.verbose, args.no_error, args.delay))
    elif args.domain:
        print(f"Starting vhost brute-force on {args.domain} with wordlist {args.wordlist}")
        asyncio.run(brute_force_vhosts(args.domain, wordlist, args.threads, args.verbose, args.no_error, args.delay))
    else:
        print("Error: Either --url or --domain must be specified.")
        sys.exit(1)

if __name__ == "__main__":
    main()
