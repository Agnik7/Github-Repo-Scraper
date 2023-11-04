from scraper.scrape import PublicRepoFinder
def main():
    username = input("Enter username: ")
    print(f"Public Repos of {username} are listed below:")
    repo_finder = PublicRepoFinder()
    repo_details = repo_finder.find(username) # should return a dictionary
    for name,link in repo_details.items():
        print(f"{name} : {link}")

if __name__ == "__main__":
    main()