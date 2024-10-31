import wikipediaapi
import os

def fetch_wikipedia_data(topic="Natural Language Processing", limit=10, data_dir='data/raw'):
    os.makedirs(data_dir, exist_ok=True)
    
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page = wiki_wiki.page(topic)
    
    if not page.exists():
        print(f"The topic '{topic}' does not exist on Wikipedia.")
        return
    
    # Retrieve subpages or categories
    subpages = page.categorymembers
    
    count = 0
    for title, subpage in subpages.items():
        if count >= limit:
            break
        if subpage.ns == wikipediaapi.Namespace.MAIN:  # Ignore non-article pages
            page_text = subpage.text
            with open(f"{data_dir}/{title.replace('/', '-')}.txt", "w", encoding="utf-8") as file:
                file.write(page_text)
            print(f"Saved {title}")
            count += 1

    print("Data fetching complete.")

if __name__ == '__main__':
    fetch_wikipedia_data(topic="Artificial Intelligence", limit=10)

