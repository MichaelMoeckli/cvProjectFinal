import gradio as gr
from transformers import pipeline

vit_classifier = pipeline("image-classification", model="MichaelMM2000/vit-base-animals10")

clip_detector = pipeline(model="openai/clip-vit-base-patch32", task="zero-shot-image-classification")

# Animals-10 class names
labels_animals10 = [
    "butterfly", "cat", "chicken", "cow", "dog",
    "elephant", "horse", "sheep", "spider", "squirrel"
]

def classify_animal(image):
    # Run ViT classifier
    vit_results = vit_classifier(image)
    vit_output = {result['label']: result['score'] for result in vit_results}

    # Run CLIP zero-shot classifier
    clip_results = clip_detector(image, candidate_labels=[f"a photo of a {label}" for label in labels_animals10])
    clip_output = {result['label']: result['score'] for result in clip_results}

    return {
        "ViT Classification": vit_output,
        "CLIP Zero-Shot Classification": clip_output
    }

# Optional: you can add example images
example_images = [
    "example_images/cat.jpeg",
    "example_images/chicken1.jpeg",
    "example_images/chicken2.jpeg",
    "example_images/elefant.jpg",
    "example_images/spider.jpeg",
    "example_images/butterfly.jpg"
]


iface = gr.Interface(
    fn=classify_animal,
    inputs=gr.Image(type="filepath"),
    outputs=gr.JSON(),
    title="Animals-10 Classification: ViT vs CLIP",
    description="Upload an animal image to compare predictions from your trained ViT model and a zero-shot CLIP model.",
    examples=example_images  # <- jetzt korrekt
)


iface.launch()
