with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

bencana_map_html = '''
                <!-- Peta Bencana -->
                <div class="bencana-map-container reveal shadow" style="background: white; border-radius: 12px; padding: 30px; margin-bottom: 40px; text-align: center;">
                    <h3 style="margin-bottom: 20px; color: #2e7d32;">Peta Bencana Banjir</h3>
                    <img src="Peta Bencana Banjir_page-0001.jpg" alt="Peta Bencana Banjir Dogongan"
                        style="width: 100%; max-width: 900px; height: auto; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); display: inline-block;">
                    <p style="margin-top: 20px;">
                        <a href="Peta Bencana Banjir_page-0001.jpg" target="_blank" class="btn btn-outline"
                            style="border: 2px solid #2e7d32; color: #2e7d32; display: inline-block; padding: 10px 25px;"><i
                                class="fas fa-expand"></i> Perbesar Peta Bencana</a>
                    </p>
                </div>
'''

target_string = '<h3 class="reveal" style="text-align: center; color: #2e7d32; margin-bottom: 30px;">Jenis Ancaman &\n                    Faktor Risiko</h3>'

if target_string in content and 'Peta Bencana Banjir_page-0001.jpg' not in content:
    content = content.replace(target_string, bencana_map_html + '\n                ' + target_string)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Peta Bencana Banjir added successfully!')
else:
    print('Failed to find target string or map already exists.')
    print("Is target string in content? ", target_string in content)
