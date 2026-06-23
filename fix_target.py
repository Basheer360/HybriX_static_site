import os

out_dir = '/Users/hybrix/PROJECTS/HybriX_static_site'

def fix_target():
    for root, dirs, files in os.walk(out_dir):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                old_js = "window.location.href = whatsappUrl;"
                new_js = "window.open(whatsappUrl, '_blank');"
                
                if old_js in content:
                    content = content.replace(old_js, new_js)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Updated redirect target in {file}")

if __name__ == '__main__':
    fix_target()
