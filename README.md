
# Animals-10 Classification

## Project Description
This project classifies images into one of 10 animal categories using a trained ViT model and compares its performance to a zero-shot CLIP model.

## Name & URL

| Name           | URL                    |
|----------------|------------------------|
| Huggingface    | [Huggingface Space](https://huggingface.co/spaces/YourUsername/animals10-classifier) |
| Model Page     | [Huggingface Model Page](https://huggingface.co/YourUsername/animals10-vit) |
| Code           | [GitHub Repository](https://github.com/YourUsername/animals10-classifier) |

## Labels
The different animal categories are:
['butterfly', 'cat', 'chicken', 'cow', 'dog', 'elephant', 'horse', 'sheep', 'spider', 'squirrel']

## Data Sources and Features Used Per Source

| Data Source        | Description                                           |
|--------------------|-------------------------------------------------------|
| Animals-10 Dataset | Public dataset containing 10 animal categories.       |

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

| Epoch | Training Loss | Validation Loss | Accuracy |
|-------|----------------|-----------------|----------|
| 1     | 0.544          | 0.402           | 85.20%   |
| 2     | 0.354          | 0.298           | 88.75%   |
| 3     | 0.294          | 0.261           | 90.10%   |
| 4     | 0.239          | 0.230           | 91.40%   |
| 5     | 0.210          | 0.219           | 92.00%   |

## TensorBoard

Details of training can be found at Huggingface TensorBoard:

| Model/Method                                                      | TensorBoard Link                        |
|------------------------------------------------------------------|-----------------------------------------|
| Transfer Learning with google/vit-base-patch16-224 (with aug.)   | `runs/animals10_with_aug`              |
| Transfer Learning with google/vit-base-patch16-224 (no aug.)     | `runs/animals10_no_aug`                |

## Results

| Model/Method                                                  | Accuracy | Precision | Recall |
|--------------------------------------------------------------|----------|-----------|--------|
| Transfer Learning with google/vit-base-patch16-224 (with aug.) | 92%      | -         | -      |
| Transfer Learning with google/vit-base-patch16-224 (no aug.)   | 90%      | -         | -      |
| Zero-shot Classification with openai/clip-vit-base-patch32     | 85%      | 84.3%     | 85%    |

## References
- Animals-10 Dataset
- Hugging Face Transformers & Datasets
- OpenAI CLIP Model
