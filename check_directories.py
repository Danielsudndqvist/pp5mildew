import os

def check_dirs():
    base_dir = 'data/cherry_leaves'
    for category in ['healthy', 'powdery_mildew']:
        path = os.path.join(base_dir, category)
        print(f"\nChecking {path}:")
        if os.path.exists(path):
            contents = os.listdir(path)
            print(f"Number of files: {len(contents)}")
            if contents:
                print(f"Sample files: {contents[:5]}")
        else:
            print("Directory doesn't exist")

check_dirs()