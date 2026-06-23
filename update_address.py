import os

out_dir = '/Users/hybrix/PROJECTS/HybriX_static_site'

def update_address():
    old_address_block = """                        <li><span class="form-icon"><i class="fa-solid fa-location-dot"></i></span>&nbsp;&nbsp;<a href="https://maps.app.goo.gl/GFhb7udH1v4eayYA7">Office: #1408, HiLite Business Park<br>
                            <span class="ms-23">Kozhikode, Kerala - 673014</span></a></li>
                        <li><span class="form-icon"><i class="fa-solid fa-location-dot"></i></span>&nbsp;&nbsp;<a href="https://maps.app.goo.gl/neT9oAFfpDvheZWj8" class="fs-15">Service Point: Near KINFRA Techno Park<br>
                            <span class="ms-25">Calicut Airport Road - Kakkanchery</span></a></li>"""

    old_address_block_rn = old_address_block.replace('\n', '\r\n')

    new_address_block = """                        <li><span class="form-icon"><i class="fa-solid fa-location-dot"></i></span>&nbsp;&nbsp;<a href="https://maps.app.goo.gl/neT9oAFfpDvheZWj8" class="fs-15">Office: Near KINFRA Techno Park<br>
                            <span class="ms-25">Calicut Airport Road - Kakkanchery</span></a></li>"""
    
    new_address_block_rn = new_address_block.replace('\n', '\r\n')

    for root, dirs, files in os.walk(out_dir):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                changed = False

                if old_address_block in content:
                    content = content.replace(old_address_block, new_address_block)
                    changed = True
                elif old_address_block_rn in content:
                    content = content.replace(old_address_block_rn, new_address_block_rn)
                    changed = True

                if changed:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Updated {file}")

if __name__ == '__main__':
    update_address()
