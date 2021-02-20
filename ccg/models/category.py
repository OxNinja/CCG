"""Representing all supported categories, with corresponding sub-categories
Each sub-categories got its own class in `../category/sub_category_name.py` to ensure the creation of a challenge
"""
CATEGORIES = {
    'crypto': ['encoding', 'rsa'],
    'steg': ['hidden_message', 'lsb'],
    'web': ['sqli', 'ssti', 'xss']
}
