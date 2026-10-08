import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_cards = '''<div class="umkm-scroll-area" id="umkm-container">
                            <!-- UMKM TAHU 1 -->
                            <div class="umkm-card umkm-item umkm-tahu">
                                <img src="Tahu 1.jpeg" class="rounded-img shadow" style="width:100%; height:150px; object-fit:cover; margin-bottom:15px;" alt="Sentra Produksi Tahu 1" />
                                <div class="umkm-content">
                                    <span class="badge" style="background: #e67e22; color:white;">Tahu</span>
                                    <h3>Sentra Produksi Tahu</h3>
                                    <p class="umkm-desc">Beragam usaha rumahan yang memproduksi tahu berkualitas dari kedelai pilihan warga.</p>
                                </div>
                            </div>

                            <!-- UMKM TAHU 2 -->
                            <div class="umkm-card umkm-item umkm-tahu">
                                <img src="Tahu 2.jpeg" class="rounded-img shadow" style="width:100%; height:150px; object-fit:cover; margin-bottom:15px;" alt="Sentra Produksi Tahu 2" />
                                <div class="umkm-content">
                                    <span class="badge" style="background: #e67e22; color:white;">Tahu</span>
                                    <h3>Proses Pembuatan Tahu</h3>
                                    <p class="umkm-desc">Proses pembuatan tahu yang bersih dan higienis oleh masyarakat Dogongan.</p>
                                </div>
                            </div>

                            <!-- UMKM TEMPE 1 -->
                            <div class="umkm-card umkm-item umkm-tempe">
                                <img src="Tempe 1.jpeg" class="rounded-img shadow" style="width:100%; height:150px; object-fit:cover; margin-bottom:15px;" alt="Produksi Tempe Lokal 1" />
                                <div class="umkm-content">
                                    <span class="badge" style="background: #f39c12; color:white;">Tempe</span>
                                    <h3>Produksi Tempe</h3>
                                    <p class="umkm-desc">Tempe tradisional dengan cita rasa khas hasil fermentasi alami, diproduksi setiap hari.</p>
                                </div>
                            </div>

                            <!-- UMKM TEMPE 2 -->
                            <div class="umkm-card umkm-item umkm-tempe">
                                <img src="Tempe 2.jpeg" class="rounded-img shadow" style="width:100%; height:150px; object-fit:cover; margin-bottom:15px;" alt="Produksi Tempe Lokal 2" />
                                <div class="umkm-content">
                                    <span class="badge" style="background: #f39c12; color:white;">Tempe</span>
                                    <h3>Kualitas Tempe Terbaik</h3>
                                    <p class="umkm-desc">Pengolahan kedelai terbaik menjadi tempe yang kaya akan nutrisi dan protein.</p>
                                </div>
                            </div>

                            <!-- UMKM WAYANG -->
                            <div class="umkm-card umkm-item umkm-kerajinan">
                                <img src="Wayang.jpeg" class="rounded-img shadow" style="width:100%; height:150px; object-fit:cover; margin-bottom:15px;" alt="Kerajinan Wayang" />
                                <div class="umkm-content">
                                    <span class="badge" style="background: #9b59b6; color:white;">Kerajinan</span>
                                    <h3>Kerajinan Wayang</h3>
                                    <p class="umkm-desc">Pembuatan kerajinan wayang dengan ukiran mendetail dan bernilai seni tinggi oleh pengrajin lokal.</p>
                                </div>
                            </div>

                            <!-- UMKM FURNITURE / MEBEL -->
                            <div class="umkm-card umkm-item umkm-kerajinan">
                                <img src="Mabel.jpeg" class="rounded-img shadow" style="width:100%; height:150px; object-fit:cover; margin-bottom:15px;" alt="Kerajinan Furniture Mebel" />
                                <div class="umkm-content">
                                    <span class="badge" style="background: #34495e; color:white;">Furniture</span>
                                    <h3>Mebel & Furniture</h3>
                                    <p class="umkm-desc">Pembuatan perabotan mebel kayu yang presisi, kuat, dan tahan lama oleh ahli kayu Dogongan.</p>
                                </div>
                            </div>
                        </div>'''

content = re.sub(r'<div class="umkm-scroll-area" id="umkm-container">.*?</div>\n                    </div>\n                </div>\n            </div>\n        </section>', new_cards + '\n                    </div>\n                </div>\n            </div>\n        </section>', content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("UMKM cards successfully updated!")
