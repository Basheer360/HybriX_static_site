import os

out_dir = '/Users/hybrix/PROJECTS/HybriX_static_site'

def update_instagram():
    old_link = "https://www.instagram.com/hybrix_technologies_llp/"
    new_link = "https://www.instagram.com/hybrix_technologies_"

    for root, dirs, files in os.walk(out_dir):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                if old_link in content:
                    content = content.replace(old_link, new_link)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Updated {file}")

if __name__ == '__main__':
    update_instagram()
