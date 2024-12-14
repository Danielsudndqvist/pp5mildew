import os

def check_organization():
    healthy_dir = 'data/cherry_leaves/healthy'
    mildew_dir = 'data/cherry_leaves/powdery_mildew'

    print(f"Healthy images: {len(os.listdir(healthy_dir)) if os.path.exists(healthy_dir) else 0}")
    print(f"Mildew images: {len(os.listdir(mildew_dir)) if os.path.exists(mildew_dir) else 0}")

check_organization()
