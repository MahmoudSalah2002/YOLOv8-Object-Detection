
from pathlib import Path
import random
import shutil

ROOT = Path(r"D:\Downloads\cat_dog_dataset")
SOURCE = ROOT / "obj_train_data"
DEST = ROOT / "ultralytics_dataset"

classes = ["cat", "Dog"]
images = sorted(
    p for p in SOURCE.iterdir()
    if p.suffix.lower() in {".jpg", ".jpeg", ".png"}
)

if not images:
    raise SystemExit("ERROR: No images found.")

# Check every annotation before copying anything
for img in images:
    label = img.with_suffix(".txt")
    if not label.exists():
        raise SystemExit(f"Missing annotation: {label.name}")

    lines = [s.strip() for s in label.read_text().splitlines() if s.strip()]
    if not lines:
        raise SystemExit(f"Empty annotation: {label.name}")

    for line in lines:
        parts = line.split()
        if len(parts) != 5:
            raise SystemExit(f"Invalid YOLO row in {label.name}: {line}")

        cls = int(parts[0])
        coords = list(map(float, parts[1:]))

        if cls not in range(len(classes)):
            raise SystemExit(f"Invalid class ID in {label.name}: {cls}")
        if any(v < 0 or v > 1 for v in coords):
            raise SystemExit(f"Coordinates outside 0-1 in {label.name}")

random.seed(42)
random.shuffle(images)

if len(images) < 3:
    raise SystemExit("Need at least 3 images.")

n_val = max(1, round(len(images) * 0.15))
n_test = max(1, round(len(images) * 0.15))
splits = {
    "train": images[:len(images) - n_val - n_test],
    "val": images[len(images) - n_val - n_test:len(images) - n_test],
    "test": images[len(images) - n_test:],
}

for split, files in splits.items():
    img_dir = DEST / "images" / split
    label_dir = DEST / "labels" / split
    img_dir.mkdir(parents=True, exist_ok=True)
    label_dir.mkdir(parents=True, exist_ok=True)

    for img in files:
        shutil.copy2(img, img_dir / img.name)
        shutil.copy2(img.with_suffix(".txt"), label_dir / f"{img.stem}.txt")

yaml_text = f"""path: {DEST.as_posix()}
train: images/train
val: images/val
test: images/test

names:
  0: cat
  1: Dog
"""
(DEST / "data.yaml").write_text(yaml_text, encoding="utf-8")

print("Dataset prepared successfully!")
for split, files in splits.items():
    print(f"{split}: {len(files)} images")
print(f"Config: {DEST / 'data.yaml'}")
