import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the giant SVG placeholders with Unsplash nature/village photos
unsplash_urls = [
    'https://images.unsplash.com/photo-1518548419970-58e3b4079ab2?auto=format&fit=crop&w=800&q=80',
    'https://images.unsplash.com/photo-1533621412968-3ce48123287f?auto=format&fit=crop&w=800&q=80',
    'https://images.unsplash.com/photo-1555505019-8c3f1e31d5cb?auto=format&fit=crop&w=800&q=80',
    'https://images.unsplash.com/photo-1552084117-56a98cea30ce?auto=format&fit=crop&w=800&q=80',
    'https://images.unsplash.com/photo-1542385151-efd9000785a0?auto=format&fit=crop&w=800&q=80',
    'https://images.unsplash.com/photo-1501179691627-eeaa65ea017c?auto=format&fit=crop&w=800&q=80',
]

def replace_svg(match):
    replace_svg.count += 1
    idx = replace_svg.count % len(unsplash_urls)
    return unsplash_urls[idx]

replace_svg.count = 0

content = re.sub(r'data:image/svg\+xml;charset=UTF-8,[^\"]+', replace_svg, content)

# Replace the div placeholders for KT/UMKM etc.
def replace_div(match):
    replace_div.count += 1
    # Use picsum for varied photos
    url = f'https://picsum.photos/400/300?random={replace_div.count}'
    return f'<img src="{url}" class="rounded-img shadow" style="width:100%; height:150px; object-fit:cover; margin-bottom:15px;" alt="Foto Kegiatan" />'

replace_div.count = 0
content = re.sub(r'<div class="umkm-img-placeholder"[^>]*>.*?</div>', replace_div, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated index.html placeholders!')
