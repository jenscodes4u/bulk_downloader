import requests
from bs4 import BeautifulSoup as soup

file = open("links.txt","r") #  open file with links to download

for line in file:
	print("lade link:"+line)
	link = line.strip()
	responded_page = requests.get(link)
	if responded_page.status_code == 200:
		#save canonical link
		#(page_soup.link['href']
		seite = link.split("/")
		#page_soup = soup(seite, "html.parser")
		saved_html_file = open (seite[-1],"w", encoding="UTF-8")
		saved_html_file.write(responded_page.text)
		saved_html_file.close()

	else:
		print("Ein Fehler Code: "+ str(responded_page.status_code))
		break
		#hier programm stoppen
