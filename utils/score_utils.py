import re

def extract_scores(text):
    """
    Extract numeric scores from table column:
    | Score (out of 5) | 4 |
    """
    pattern = r'\|\s*\*?\*?\s*\d+(?:\.\d+)?\s*\*?\*?\s*\|'
    
    # Alternative simpler approach:
    matches = re.findall(r'\|\s*(\d(?:\.\d)?)\s*\|', text)
    
    scores = [float(m) for m in matches if 0 <= float(m) <= 5]
    return scores
