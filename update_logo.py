import os

out_dir = '/Users/hybrix/PROJECTS/HybriX_static_site'

def update_logo():
    for root, dirs, files in os.walk(out_dir):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                if 'logo.png' in content:
                    content = content.replace('logo.png', 'logo.jpeg')
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Updated logo in {file}")

if __name__ == '__main__':
    update_logo()
