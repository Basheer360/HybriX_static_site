import os

out_dir = '/Users/hybrix/PROJECTS/HybriX_static_site'

def fix_js():
    for root, dirs, files in os.walk(out_dir):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Fix the JS condition
                old_condition = "if (pair[0] !== 'csrfmiddlewaretoken') {"
                new_condition = "if (pair[0] !== 'csrfmiddlewaretoken' && pair[0] !== 'redirect') {"
                
                if old_condition in content:
                    content = content.replace(old_condition, new_condition)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Fixed {file}")

if __name__ == '__main__':
    fix_js()
