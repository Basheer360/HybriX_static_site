import os
import re

out_dir = '/Users/hybrix/PROJECTS/HybriX_static_site'

def move_icons():
    for root, dirs, files in os.walk(out_dir):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Step 1: Remove the old UL inside the collapse menu
                old_ul_pattern = re.compile(
                    r'<ul class="medium-icon dark d-block d-sm-none">.*?</ul>',
                    re.DOTALL
                )
                content = old_ul_pattern.sub('', content)

                # Step 2: Add flex classes to the logo container and insert the new UL
                # Find: <div class="col-auto col-xl-2 col-lg-2 me-lg-auto">
                #       <a href="/" class="navbar-brand">
                logo_container_pattern = re.compile(
                    r'(<div class="col-auto col-xl-2 col-lg-2 me-lg-auto">)(\s*<a href="/" class="navbar-brand">.*?</a>\s*)(</div>)',
                    re.DOTALL
                )

                new_ul = """
                <ul class="medium-icon dark d-flex d-lg-none mb-0 list-unstyled align-items-center ms-3" style="padding: 0; margin: 0;">
                    <li class="my-0" style="margin: 0 8px;"><a class="whatsapp-nav facebook" href="https://wa.me/+919947550033" target="_blank"><i class="fa-brands fa-whatsapp" style="font-size: 20px;"></i></a></li>
                    <li class="my-0" style="margin: 0 8px;"><a class="dribbble" href="tel:+919947550033"><i class="fa-solid fa-phone" style="font-size: 20px;"></i></a></li>
                    <li class="my-0" style="margin: 0 8px;"><a class="twitter" href="mailto:basheer@hybrixtechnologies.com"><i class="fa-regular fa-envelope" style="font-size: 20px;"></i></a></li>
                </ul>
"""

                def replacement(match):
                    # Change container to flex
                    start_div = '<div class="col-auto col-xl-2 col-lg-2 me-lg-auto d-flex align-items-center">'
                    inner_content = match.group(2)
                    end_div = match.group(3)
                    return start_div + inner_content + new_ul + end_div

                content = logo_container_pattern.sub(replacement, content)

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated {file}")

if __name__ == '__main__':
    move_icons()
