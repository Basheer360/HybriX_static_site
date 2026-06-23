import os

out_dir = '/Users/hybrix/PROJECTS/HybriX_static_site'

def fix_links():
    for root, dirs, files in os.walk(out_dir):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                changed = False
                
                # Fix mailto links
                old_mailto = 'href="mailto:basheer@hybrixtechnologies.com" target="_blank"'
                new_mailto = 'href="mailto:basheer@hybrixtechnologies.com"'
                if old_mailto in content:
                    content = content.replace(old_mailto, new_mailto)
                    changed = True

                # Fix tel links
                old_tel = 'href="tel:+919947550033" target="_blank"'
                new_tel = 'href="tel:+919947550033"'
                if old_tel in content:
                    content = content.replace(old_tel, new_tel)
                    changed = True

                if changed:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Updated links in {file}")

if __name__ == '__main__':
    fix_links()
