import os
import re

out_dir = '/Users/hybrix/PROJECTS/HybriX_static_site'

def fix_icons():
    for root, dirs, files in os.walk(out_dir):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                changed = False

                # 1. Remove the previously inserted UL
                old_ul_pattern = re.compile(
                    r'\s*<ul class="medium-icon dark d-flex d-lg-none mb-0 list-unstyled align-items-center ms-3" style="padding: 0; margin: 0;">.*?</ul>',
                    re.DOTALL
                )
                if old_ul_pattern.search(content):
                    content = old_ul_pattern.sub('', content)
                    changed = True

                # 2. Wrap navbar-toggler and insert the new UL before it
                target_button_pattern = re.compile(
                    r'(<div class="col-auto col-xl-6 col-lg-8 menu-order position-static">)\s*(<button class="navbar-toggler float-start"[^>]*>.*?</button>)',
                    re.DOTALL
                )

                new_html = r"""\1
                <div class="d-flex align-items-center">
                    <ul class="medium-icon dark d-flex d-lg-none mb-0 list-unstyled align-items-center me-3" style="padding: 0; margin: 0;">
                        <li class="my-0" style="margin: 0 8px;"><a class="whatsapp-nav facebook" href="https://wa.me/+919947550033" target="_blank"><i class="fa-brands fa-whatsapp" style="font-size: 20px;"></i></a></li>
                        <li class="my-0" style="margin: 0 8px;"><a class="dribbble" href="tel:+919947550033"><i class="fa-solid fa-phone" style="font-size: 20px;"></i></a></li>
                        <li class="my-0" style="margin: 0 8px;"><a class="twitter" href="mailto:basheer@hybrixtechnologies.com"><i class="fa-regular fa-envelope" style="font-size: 20px;"></i></a></li>
                    </ul>
                    \2
                </div>"""

                # Only do this if we haven't already wrapped it!
                if 'class="d-flex align-items-center"' not in content and target_button_pattern.search(content):
                    content = target_button_pattern.sub(new_html, content)
                    changed = True

                if changed:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Updated {file}")

if __name__ == '__main__':
    fix_icons()
