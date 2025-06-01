
# Animals-10 Classification

## Project Description
This project classifies images into one of 10 animal categories using a trained ViT model and compares its performance to a zero-shot CLIP model.

## Name & URL

| Name           | URL                    |
|----------------|------------------------|
| Huggingface    | [Huggingface Space](https://huggingface.co/spaces/MichaelMM2000/animals10-demo) |
| Model Page     | [Huggingface Model Page](https://huggingface.co/MichaelMM2000/vit-base-animals10) |
| Code           | [GitHub Repository](https://github.com/MichaelMoeckli/cvProjectFinal) |

## Labels
The different animal categories are:
['butterfly', 'cat', 'chicken', 'cow', 'dog', 'elephant', 'horse', 'sheep', 'spider', 'squirrel']

## Data Sources and Features Used Per Source

| Data Source        | Description                                           |
|--------------------|-------------------------------------------------------|
| Animals-10 Dataset | Public dataset containing 10 animal categories.       |
| Google drive | [Public dataset containing 10 animal categories.](https://drive.google.com/file/d/14q2Qf9mukDZTZWcHMgjLbECtGd_UESHj/view)       |

## Data Augmentation

| Augmentation                 | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| RandomHorizontalFlip()      | Randomly flips the image horizontally with a probability of 0.5.            |
| RandomRotation(15)          | Rotates the image randomly within a range of ±15 degrees.                   |
| ColorJitter(...)            | Randomly alters brightness, contrast, and saturation within set limits.     |
| RandomResizedCrop(224)      | Randomly crops and resizes the image to 224×224 pixels.                     |

## Model Training

### Data Splitting Method (Train/Validation/Test)
The dataset was split as follows:

| Split      | Number of Images |
|------------|------------------|
| Train      | 18843            |
| Validation | 2355             |
| Test       | 2356             |

### Training Metrics

### Training Metrics

| Epoch | Training Loss | Validation Loss | Accuracy |
|-------|----------------|-----------------|----------|
| 1     | 0.099700       | 0.092796        | 97.32%   |
| 2     | 0.075200       | 0.067789        | 98.09%   |
| 3     | 0.074300       | 0.058433        | 98.39%   |
| 4     | 0.088200       | 0.060490        | 97.92%   |
| 5     | 0.065600       | 0.065273        | 98.13%   |

## TensorBoard

Details of training can be found at Huggingface TensorBoard:

| Model/Method                                                      | TensorBoard Link                        |
|------------------------------------------------------------------|-----------------------------------------|
| Transfer Learning with google/vit-base-patch16-224 (with aug.)   | `runs/Jun01_10-55-24_cs-01jwnhdb68etg2xr4j1yga79wz`                |
| Transfer Learning with google/vit-base-patch16-224 (no aug.)     | `runs/Jun01_13-16-37_cs-01jwnqfm7bt4be71dq5a10q9pe`                |

## Results

| Model/Method                                                  | Accuracy | Precision | Recall |
|---------------------------------------------------------------|----------|-----------|--------|
| Transfer Learning with google/vit-base-patch16-224 (with aug.) | 99.00%   | -         | -      |
| Zero-shot Classification with openai/clip-vit-base-patch32     | 99.00%   | -         | -      |


## References
- Animals-10 Dataset
- Hugging Face Transformers & Datasets
- OpenAI CLIP Model
