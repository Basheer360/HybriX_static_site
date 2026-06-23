import os

out_dir = '/Users/hybrix/PROJECTS/HybriX_static_site'

def fix_images():
    for root, dirs, files in os.walk(out_dir):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                changed = False
                if "__6.jpeg" in content:
                    content = content.replace("__6.jpeg", "6.jpeg")
                    changed = True
                if "__7.jpeg" in content:
                    content = content.replace("__7.jpeg", "7.jpeg")
                    changed = True
                
                if changed:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Updated images in {file}")

if __name__ == '__main__':
    fix_images()
