import os

out_dir = '/Users/hybrix/PROJECTS/HybriX_static_site'

def move_icons():
    new_ul = """                <ul class="medium-icon dark d-flex d-lg-none mb-0 list-unstyled align-items-center ms-3" style="padding: 0; margin: 0;">
                    <li class="my-0" style="margin: 0 8px;"><a class="whatsapp-nav facebook" href="https://wa.me/+919947550033" target="_blank"><i class="fa-brands fa-whatsapp" style="font-size: 20px;"></i></a></li>
                    <li class="my-0" style="margin: 0 8px;"><a class="dribbble" href="tel:+919947550033"><i class="fa-solid fa-phone" style="font-size: 20px;"></i></a></li>
                    <li class="my-0" style="margin: 0 8px;"><a class="twitter" href="mailto:basheer@hybrixtechnologies.com"><i class="fa-regular fa-envelope" style="font-size: 20px;"></i></a></li>
                </ul>
"""

    for root, dirs, files in os.walk(out_dir):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                changed = False
                
                old_div_start = '<div class="col-auto col-xl-2 col-lg-2 me-lg-auto">'
                new_div_start = '<div class="col-auto col-xl-2 col-lg-2 me-lg-auto d-flex align-items-center">'
                if old_div_start in content:
                    content = content.replace(old_div_start, new_div_start)
                    changed = True

                old_div_end = '</a>\n            </div>\n            <div class="col-auto col-xl-6 col-lg-8 menu-order position-static">'
                new_div_end = '</a>\n' + new_ul + '            </div>\n            <div class="col-auto col-xl-6 col-lg-8 menu-order position-static">'
                
                # Some files might have \r\n
                old_div_end_rn = '</a>\r\n            </div>\r\n            <div class="col-auto col-xl-6 col-lg-8 menu-order position-static">'
                new_div_end_rn = '</a>\r\n' + new_ul + '            </div>\r\n            <div class="col-auto col-xl-6 col-lg-8 menu-order position-static">'

                if old_div_end in content:
                    content = content.replace(old_div_end, new_div_end)
                    changed = True
                elif old_div_end_rn in content:
                    content = content.replace(old_div_end_rn, new_div_end_rn)
                    changed = True

                if changed:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Updated {file}")

if __name__ == '__main__':
    move_icons()
