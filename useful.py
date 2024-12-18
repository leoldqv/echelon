#import chat_exporter
import discord
import json
import io

import cloudinary
import cloudinary.uploader

def load_data(file_name: str):
    """Loads and returns the object contained in the .json file of which the name is provided."""
    with open(f"database/{file_name}.json") as f:
        data = json.load(f)
        return data
    
def save_data(obj, file_name: str):
    """Saves the provided object to the .json file of the provided name."""
    with open(f"database/{file_name}.json", "w") as f:
        json.dump(obj, f, indent=4)