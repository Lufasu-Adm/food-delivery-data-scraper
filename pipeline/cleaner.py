import re

def clean_rating(rating_str: str) -> float:
    """Membersihkan format string rating menjadi float."""
    if not rating_str or rating_str == "0":
        return 0.0
    
    rating_map = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'half': 0.5
    }
    
    r_lower = rating_str.lower()
    score = 0.0
    
    for word, value in rating_map.items():
        if word in r_lower:
            score += value
            
    if score == 0.0:
        try:
            return float(re.findall(r"[-+]?\d*\.\d+|\d+", rating_str)[0])
        except (IndexError, ValueError):
            return 0.0
            
    return score