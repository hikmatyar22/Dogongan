with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove profil link from footer if exists
content = content.replace('<li><a href="#profil">Profil</a></li>\r\n                        ', '')
content = content.replace('<li><a href="#profil">Profil</a></li>\n                        ', '')

print('Has ~800:', '~800' in content)
print('Has Kondisi Geografis:', 'Kondisi Geografis' in content)
print('Has Batas Wilayah:', 'Batas Wilayah' in content)
print('Has profil section:', 'id="profil"' in content)
print('Has dinamika section:', 'id="dinamika"' in content)
print('File size:', len(content))

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Saved OK')
