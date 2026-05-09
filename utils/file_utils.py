import os
import re


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', '_', name)