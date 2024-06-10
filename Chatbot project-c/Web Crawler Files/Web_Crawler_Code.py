import nltk
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse, urljoin
import os

# Download NLTK resources if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def web_crawler(start_url, max_links, max_depth):
    """
    Custom web crawler function to create a knowledge base by crawling relevant URLs.

    Parameters:
    - start_url (str): The starting URL for crawling.
    - max_links (int): Maximum number of relevant links to crawl.
    - max_depth (int): Maximum depth for crawling (number of hops from the start_url).

    Returns:
    - urls_relevant (list): List of relevant URLs crawled.
    """

    # Initialize data structures to track visited URLs and unique domains
    urls_visited = set()
    unique_domains = set()
    urls_relevant = []

    # Initialize queue with the starting URL and depth 0
    queue = [(start_url, 0)]

    while queue and len(urls_relevant) < max_links:
        url, depth = queue.pop(0)

        if url not in urls_visited and depth <= max_depth:
            try:
                # Get HTML content from the URL
                html = requests.get(url).text

                # Parse HTML content using BeautifulSoup
                soup = BeautifulSoup(html, 'html.parser')

                # Extract text and store it in a file
                filename = f'{urlparse(url).hostname}.txt'
                with open(filename, 'w') as file:
                    for p in soup.find_all('p'):
                        file.write(p.get_text() + '\n')

                # Extract links from the page
                if depth < max_depth:
                    for link in soup.find_all('a', href=True):
                        absolute_link = urljoin(url, link['href'])
                        domain = urlparse(absolute_link).hostname
                        if absolute_link not in urls_visited and domain not in unique_domains:
                            queue.append((absolute_link, depth + 1))
                            unique_domains.add(domain)

                urls_relevant.append(url)
                urls_visited.add(url)
                print(f"Crawled: {url}")

            except requests.RequestException as e:
                print(f"Failed to get {url}")

    return urls_relevant[:max_links]

# Example usage of the web_crawler function
start_url = 'https://www.biography.com/actors/leonardo-dicaprio'
urls_relevant = web_crawler(start_url, 25, 2)

# Additional code (cleaning text, extracting important terms, updating knowledge base, etc.) can be integrated here

# Display the list of relevant URLs crawled
print("Relevant URLs crawled:")
for url in urls_relevant:
    print(url)
