# FastBrute

FastBrute is an ultra-fast web directory and vhost brute-forcer written in Python. It uses asynchronous HTTP requests to achieve high performance and can handle a large number of concurrent tasks.

## Features

- Asynchronous HTTP requests for high performance
- Directory brute-forcing
- Vhost brute-forcing
- High concurrency
- Verbose and quiet modes
- Error handling
- Custom delay between requests
- Output to file

## Requirements

- Python 3.6+
- `aiohttp` library

You can install the required library using pip:

```bash
pip install aiohttp
```

## Usage

To use FastBrute, run the script with the desired options. You can specify either a URL for directory brute-forcing or a domain for vhost brute-forcing.

### Directory Brute-forcing

```bash
python fastbrute.py --url http://example.com --wordlist wordlist.txt --threads 100
```

### Vhost Brute-forcing

```bash
python fastbrute.py --domain example.com --wordlist subdomains.txt --threads 100
```

## Options

```
-u, --url              Base URL to brute-force directories (e.g., http://example.com)
-d, --domain           Domain to brute-force vhosts (e.g., example.com)
-w, --wordlist         Path to the wordlist file (required)
-t, --threads          Number of concurrent tasks to use (default: 100)
-o, --output           Output file to write results to
--delay                Time each thread waits between requests (e.g., 1500ms, default: 0)
--no-error             Don't display errors
--no-progress          Don't display progress
--no-color             Disable color output
-q, --quiet            Don't print the banner and other noise
-v, --verbose          Verbose output (errors)
```

## Example

```bash
python fastbrute.py --url http://example.com --wordlist common.txt --threads 200 --verbose
```

This command starts directory brute-forcing on `http://example.com` using `common.txt` as the wordlist with 200 concurrent tasks and verbose error output.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements.

## Contact

For any questions or inquiries, please contact me on twitter.

```
# FastBrute
