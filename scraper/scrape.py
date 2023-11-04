import requests
from bs4 import BeautifulSoup

class PublicRepoFinder():
    def find(self,username):
        URL = f"https://github.com/{username}?tab=repositories"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id="user-repositories-list")
        #print(results.prettify())
        projects = results.find_all("div", class_="col-10 col-lg-9 d-inline-block")
        repo_details = {}
        for project in projects:
            #print(project, end="\n"*2)
            repo_name= project.find("a")
            link = repo_name.get("href")
            repo_details[repo_name.text] = f"https://github.com{link}"
        return repo_details