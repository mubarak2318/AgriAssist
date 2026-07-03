import json
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def _load(filename):
    filepath = os.path.join(BASE_DIR, "data", filename)
    with open(filepath, "r") as f:
        return json.load(f)

def load_crops():
    return _load("crops.json")

def load_schemes():
    return _load("schemes.json")

def load_fertilizers():
    return _load("fertilizers.json")

def load_pesticides():
    return _load("pesticides.json")

def load_loans():
    return _load("loans.json")

def load_vendors():
    return _load("vendors.json")

def load_market_prices():
    return _load("market_prices.json")