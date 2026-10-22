
from pathlib import Path
from ultralytics import YOLO

# Project paths
PROJECT_DIR = Path(__file__).resolve().parent
DATA_YAML = PROJECT_DIR / "ultralytics_dataset" / "data.yaml"

# Pretrained YOLOv8 model
MODEL_NAME = "yolov8n.pt"


def main():
    if not DATA_YAML.exists():
        raise FileNotFoundError(
            f"Dataset configuration not found: {DATA_YAML}\n"
            "Please prepare the dataset first using prepare_dataset.py."
        )

    model = YOLO(MODEL_NAME)

    model.train(
        data=str(DATA_YAML),
        epochs=50,
        imgsz=640,
        batch=8,
        project=str(PROJECT_DIR / "runs" / "detect"),
        name="cat_dog_training",
        exist_ok=True,
    )


if __name__ == "__main__":
    main()
