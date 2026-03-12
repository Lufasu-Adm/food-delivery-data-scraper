from bs4 import BeautifulSoup
from typing import List, Dict

class FoodParser:
    @staticmethod
    def parse_restaurant_list(html_content: str) -> List[Dict[str, str]]:
        """Mengekstrak data restoran dari HTML mentah."""
        if not html_content:
            return []
            
        soup = BeautifulSoup(html_content, 'html.parser')
        restaurants = []
        
        cards = soup.select(".result") 
        print(f"Parsing {len(cards)} restaurant cards...")

        for card in cards:
            try:
                name_tag = card.select_one("a.business-name")
                name = name_tag.get_text(strip=True) if name_tag else "N/A"
                
                link = "https://www.yellowpages.com" + name_tag['href'] if name_tag else ""
                
                rating_tag = card.select_one(".ratings .result-rating")
                if rating_tag:
                    rating_classes = rating_tag.get("class", [])
                    rating = " ".join(rating_classes)
                else:
                    rating = "0"

                restaurants.append({
                    "name": name,
                    "rating": rating,
                    "link": link
                })
            except Exception as e:
                print(f"Skipping a card due to error: {e}")
                continue
            
        return restaurants