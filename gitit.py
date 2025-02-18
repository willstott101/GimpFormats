from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

base_url = "https://sourceforge.net/projects/rods-custom-font-xcf-files/files/Fonts%20created%20by%20Deezy%20-%20Custom%20Fonts%20created%20by%20RD%20-%20CAP%20LETTERS%20ONLY/"
download_folder = "downloads"

# Get file links
response = requests.get(base_url)
soup = BeautifulSoup(response.text, "html.parser")
links = [a["href"] for a in soup.find_all("a", href=True) if "/files/" in a["href"]]

# Download files
for link in links:
	print(link)
	file_url = urljoin(base_url, link)
	filename = link.split("/")[-2]

	if filename:
		print(f"Downloading {filename}...")
		file_data = requests.get(file_url, stream=True)

		with open(f"{download_folder}/{filename}", "wb") as f:
			for chunk in file_data.iter_content(chunk_size=8192):
				f.write(chunk)

print("Download complete!")
