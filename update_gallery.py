import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

def replace_gallery(match):
    replace_gallery.count += 1
    category = match.group(1)
    text = match.group(2)
    url = f'https://picsum.photos/400/500?random={replace_gallery.count + 100}'
    return f'<div class="masonry-item {category}">\n                        <img src="{url}" alt="{text}" loading="lazy">\n                        <div class="masonry-overlay"><span>{text}</span></div>\n                    </div>'

replace_gallery.count = 0
content = re.sub(r'<div class="masonry-item (\w+) placeholder-img-small">\s*<div class="masonry-overlay"><span>([^<]+)</span></div>\s*</div>', replace_gallery, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated gallery!')
