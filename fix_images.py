import urllib.request
import re
import random

def fetch_unsplash_urls(query):
    url = f"https://unsplash.com/s/photos/{query.replace(' ', '-')}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        # find photo ids
        matches = re.findall(r'images\.unsplash\.com/photo-([a-zA-Z0-9-]+)\?', html)
        return list(set(matches))
    except Exception as e:
        print("Error fetching:", e)
        return []

ids = fetch_unsplash_urls("indonesia village") + fetch_unsplash_urls("rice field") + fetch_unsplash_urls("indonesian culture") + fetch_unsplash_urls("indonesian people")
ids = list(set([i for i in ids if len(i) > 10]))
print(f"Found {len(ids)} unique photo IDs")

if len(ids) == 0:
    print("Fallback to hardcoded IDs")
    ids = [
        "1518548419970-58e3b4079ab2", "1533621412968-3ce48123287f", "1555505019-8c3f1e31d5cb", 
        "1552084117-56a98cea30ce", "1542385151-efd9000785a0", "1501179691627-eeaa65ea017c",
        "1588693959306-444fbf9f43f8", "1577706346261-26c9f7a7da09", "1511216113945-89688df2d854",
        "1604928143431-7bc73e130283", "1592358897086-ee5289df7173", "1602008779607-2a445d354b2d"
    ]

# Now read index.html and replace all picsum.photos with unsplash URLs
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

def replace_picsum(match):
    photo_id = random.choice(ids)
    return f"https://images.unsplash.com/photo-{photo_id}?auto=format&fit=crop&w=400&q=80"

content = re.sub(r'https://picsum\.photos/\d+/\d+\?random=\d+', replace_picsum, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated picsum images to contextual Unsplash images!")
