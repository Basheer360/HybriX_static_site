import os
import re

out_dir = '/Users/hybrix/PROJECTS/HybriX_static_site'

def update_footer():
    for root, dirs, files in os.walk(out_dir):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Find the footer services section
                # <span class="fs-17 fw-600 d-block text-dark-gray mb-5px">Services</span>
                # <ul> ... </ul>
                
                pattern = re.compile(
                    r'(<span class="fs-17 fw-600 d-block text-dark-gray mb-5px">Services</span>\s*)<ul.*?>.*?</ul>',
                    re.DOTALL
                )
                
                new_ul = """<ul>
                    <li><a href="service-web-development.html">🌐 Web Development</a></li>
                    <li><a href="service-search-engine-optimization-seo.html">🌟 Digital Marketing</a></li>
                    <li><a href="service-aws-hosting.html">🔃 Cloud Computing</a></li>
                    <li><a href="service-networking.html">🔀 Networking</a></li>
                    <li><a href="service-computers.html">🖥️ Computers</a></li>
                    <li><a href="service-laptops.html">💻 Laptops</a></li>
                    <li><a href="service-printers.html">🖨️ Printers</a></li>
                    <li><a href="service-cctv.html">📷 CCTV</a></li>
                    <li><a href="service-cctv.html">🛡️ Security</a></li>
                </ul>"""

                # Wait, the original had no links: `<li>Sales and Services</li>`. 
                # Wait, the user uploaded a screenshot that shows "Services" list without underlining. Let's just use <a> with class="text-dark-gray" or no class, or just plain text.
                # Actually, plain text `<li>` is safer and matches exactly the existing DOM.
                
                new_ul_plain = """<ul>
                    <li>🌐 Web Development</li>
                    <li>🌟 Digital Marketing</li>
                    <li>🔃 Cloud Computing</li>
                    <li>🔀 Networking</li>
                    <li>🖥️ Computers</li>
                    <li>💻 Laptops</li>
                    <li>🖨️ Printers</li>
                    <li>📷 CCTV</li>
                    <li>🛡️ Security</li>
                </ul>"""

                if pattern.search(content):
                    content = pattern.sub(r'\g<1>' + new_ul_plain, content)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Updated {file}")

if __name__ == '__main__':
    update_footer()
