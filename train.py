
from ultralytics import YOLO
from pathlib import Path

# Path to the prepared dataset configuration
DATA_YAML = Path(
    r"D:\Downloads\cat_dog_dataset\ultralytics_dataset\data.yaml"
)

# Load a pretrained YOLOv8 model
model = YOLO("yolov8n.pt")

# Train the model
if __name__ == "__main__":
    model.train(
        data=str(DATA_YAML),
        epochs=50,
        imgsz=640,
        batch=8,
        project="runs/detect",
        name="cat_dog_training",
        exist_ok=True
    )
