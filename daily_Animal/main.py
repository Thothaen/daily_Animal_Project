from init import * 

def main():
    
    with open("all_Animals.csv", newline="", encoding="utf-8") as f: #using utf-8 because csv was exported from excel
        items = [row[0] for row in csv.reader(f)][1:] #[1:] skips header
        title = wiki_Search(random.choice(items))
        link = "https://en.wikipedia.org/wiki/" + title.replace(" ", "_")
        webbrowser.open(link)

#returns top result from wiki search
def wiki_Search(query):
    url = "https://en.wikipedia.org/w/api.php"
    params = {"action": "query", "list": "search", "srsearch": query, "format": "json"}
    headers = {"user-Agent": "daily_Animal_Project/1.0 (Student Project)"} #bypasses bot block
    r = requests.get(url, params = params, headers = headers, timeout = 10)
    data = r.json()
    return data["query"]["search"][0]["title"]

if __name__ == "__main__":
    main()