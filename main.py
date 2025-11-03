# main.py
# ===============================================
# SafeSite AI Detection — Helmet Violation Detection
# ===============================================

from ultralytics import YOLO
import cv2
import json
import os

# --- STEP 1: Load YOLO model ---
# If you don’t have a custom helmet model, we’ll use a general YOLOv8 model.
# (You can replace this with a fine-tuned model path later.)
model = YOLO("yolov8n.pt")

# --- STEP 2: Input image or video ---
# Place your test image in a folder named "test_images"
img_path = "test_images/site1.png"

if not os.path.exists(img_path):
    raise FileNotFoundError("⚠️ Please place a test image at 'test_images/site1.png'")

# --- STEP 3: Run detection ---
results = model(img_path, show=True)

# --- STEP 4: Simple logic to estimate helmet violations ---
# If the model detects 'person' but no 'helmet', count that as a violation.
helmet_violations = 0

for r in results:
    for box in r.boxes:
        cls_id = int(box.cls[0])
        label = model.names[cls_id].lower()

        # Adjust logic depending on labels available
        if "person" in label:
            helmet_violations += 1  # Assume a person needs a helmet
        if "helmet" in label or "hardhat" in label:
            helmet_violations -= 1  # Detected helmet, so reduce violation count

helmet_violations = max(0, helmet_violations)

print(f"✅ Detected {helmet_violations} helmet violation(s).")

# --- STEP 5: Update shared data file ---
data_path = "data.json"

# Read current sensor data
if os.path.exists(data_path):
    with open(data_path, "r") as f:
        data = json.load(f)
else:
    data = {}

# Update with AI detection result
data["helmet_violations"] = helmet_violations

with open(data_path, "w") as f:
    json.dump(data, f, indent=4)

print("📁 Updated data.json with AI detection result.")

# --- STEP 6: Display result image (optional) ---
# Save annotated image
output_path = "output.png"
annotated_img = results[0].plot()
cv2.imwrite(output_path, annotated_img)
print(f"🖼️ Result saved to {output_path}")

# --- STEP 7: End ---
print("🎯 AI detection complete! Dashboard will show updated safety metrics.")
