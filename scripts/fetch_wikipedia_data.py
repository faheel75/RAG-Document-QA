import wikipediaapi
import os

def fetch_wikipedia_data(topic="Natural Language Processing", limit=10, data_dir='data/raw'):
    try:
        os.makedirs(data_dir, exist_ok=True)
        
        # Specify a user agent string
        wiki_wiki = wikipediaapi.Wikipedia(
            language='en',
            extract_format=wikipediaapi.ExtractFormat.WIKI,
            user_agent='YourAppName/1.0 (https://yourwebsite.com; your_email@example.com)'
        )
        
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

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    fetch_wikipedia_data(topic="Artificial Intelligence", limit=10)

