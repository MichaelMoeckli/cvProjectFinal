
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
| Animals-10 Dataset | Public dataset containing 10 animal categories.  Mirror of Animals-10 dataset (original hosted on Kaggle). Used for convenience.  |
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

![image](https://github.com/user-attachments/assets/ff1708f8-8090-47a3-b5cc-5dc1bd786ee6)

## Model Card Summary

- **Architecture**: Vision Transformer (ViT)
- **Pretrained base**: google/vit-base-patch16-224
- **Training task**: Image classification (Animals-10)
- **Finetuned layers**: Classifier head
- **Zero-shot model**: openai/clip-vit-base-patch32

## Results and Conclusion

| Model/Method                                                  | Accuracy | Precision | Recall |
|---------------------------------------------------------------|----------|-----------|--------|
| Transfer Learning with google/vit-base-patch16-224 (with aug.) | 98.40%   | -         | -      |
| Transfer Learning with google/vit-base-patch16-224 (no aug.)   | 99.49%   | -         | -      |
| Zero-shot Classification with openai/clip-vit-base-patch32     | 99.36%   | 99.37         | 99.36      |

This project demonstrated that a ViT model fine-tuned on the Animals-10 dataset can achieve excellent classification performance, reaching up to 99.49% accuracy without data augmentation. Interestingly, the version trained without augmentation outperformed the augmented one, likely because the dataset consists of high-quality, centered images where augmentations may have introduced noise rather than helpful variety.

The comparison with the zero-shot CLIP model showed that CLIP can perform nearly as well — also achieving around 99% accuracy — without any task-specific training. This highlights the strength of pre-trained vision-language models for general classification tasks.

Overall, this project confirms that transfer learning with ViT is highly effective for structured image classification, while CLIP offers a flexible, training-free alternative that is surprisingly competitive, especially for smaller or simpler datasets.

## References
- Animals-10 Dataset
- Hugging Face Transformers & Datasets
- OpenAI CLIP Model
