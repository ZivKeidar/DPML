# build train and validation dataloaders from Amazon Reviews (2018) dataset for binary classification
# devide the dataset to different product categories and save the dataset for the following categories:
# books, DVDs, electronics and kitchen appliances
from datasets import load_dataset
import os
train_dataset = load_dataset('amazon_reviews_multi', 'en', split='train')
books_train_dataset = train_dataset.filter(lambda example: example['product_category'] == 'Books')
dvd_train_dataset = train_dataset.filter(lambda example: example['product_category'] == 'DVD')
electronics_train_dataset = train_dataset.filter(lambda example: example['product_category'] == 'Electronics')
kitchen_train_dataset = train_dataset.filter(lambda example: example['product_category'] == 'Kitchen')

# set the label to 0 for negative reviews and 1 for positive reviews if the rating is greater than 3 stars, drop neutral reviews
books_train_dataset = books_train_dataset.map(lambda example: {'label': 1 if example['stars'] > 3 else 0})
dvd_train_dataset = dvd_train_dataset.map(lambda example: {'label': 1 if example['stars'] > 3 else 0})
electronics_train_dataset = electronics_train_dataset.map(lambda example: {'label': 1 if example['stars'] > 3 else 0})
kitchen_train_dataset = kitchen_train_dataset.map(lambda example: {'label': 1 if example['stars'] > 3 else 0})

# balance the dataset to have the same number of positive and negative reviews for each category make the dataset as big as possible
books_balanced_train_dataset = books_train_dataset.filter(lambda example: example['label'] == 1).shuffle(seed=42)
books_balanced_train_dataset = books_balanced_train_dataset.concatenate(books_train_dataset.filter(lambda example: example['label'] == 0).shuffle(seed=42).select(range(books_balanced_train_dataset.dataset_size)))
dvd_balanced_train_dataset = dvd_train_dataset.filter(lambda example: example['label'] == 1).shuffle(seed=42)
dvd_balanced_train_dataset = dvd_balanced_train_dataset.concatenate(dvd_train_dataset.filter(lambda example: example['label'] == 0).shuffle(seed=42).select(range(dvd_balanced_train_dataset.dataset_size)))
electronics_balanced_train_dataset = electronics_train_dataset.filter(lambda example: example['label'] == 1).shuffle(seed=42)
electronics_balanced_train_dataset = electronics_balanced_train_dataset.concatenate(electronics_train_dataset.filter(lambda example: example['label'] == 0).shuffle(seed=42).select(range(electronics_balanced_train_dataset.dataset_size)))
kitchen_balanced_train_dataset = kitchen_train_dataset.filter(lambda example: example['label'] == 1).shuffle(seed=42)
kitchen_balanced_train_dataset = kitchen_balanced_train_dataset.concatenate(kitchen_train_dataset.filter(lambda example: example['label'] == 0).shuffle(seed=42).select(range(kitchen_balanced_train_dataset.dataset_size)))

# save the balanced datasets
if not os.path.exists('data/books/train.csv'):
    os.makedirs('data/books/train.csv')
if not os.path.exists('data/dvd/train.csv'):
    os.makedirs('data/dvd/train.csv')
if not os.path.exists('data/electronics/train.csv'):
    os.makedirs('data/electronics/train.csv')
if not os.path.exists('data/kitchen/train.csv'):
    os.makedirs('data/kitchen/train.csv')
books_balanced_train_dataset.to_csv('data/books/train.csv')
dvd_balanced_train_dataset.to_csv('data/dvd/train.csv')
electronics_balanced_train_dataset.to_csv('data/electronics/train.csv')
kitchen_balanced_train_dataset.to_csv('data/kitchen/train.csv')

# do the same process for the validation dataset
validation_dataset = load_dataset('amazon_reviews_multi', 'en', split='validation')
books_validation_dataset = validation_dataset.filter(lambda example: example['product_category'] == 'Books')
dvd_validation_dataset = validation_dataset.filter(lambda example: example['product_category'] == 'DVD')
electronics_validation_dataset = validation_dataset.filter(lambda example: example['product_category'] == 'Electronics')
kitchen_validation_dataset = validation_dataset.filter(lambda example: example['product_category'] == 'Kitchen')

books_validation_dataset = books_validation_dataset.map(lambda example: {'label': 1 if example['star_rating'] > 3 else 0})
dvd_validation_dataset = dvd_validation_dataset.map(lambda example: {'label': 1 if example['star_rating'] > 3 else 0})
electronics_validation_dataset = electronics_validation_dataset.map(lambda example: {'label': 1 if example['star_rating'] > 3 else 0})
kitchen_validation_dataset = kitchen_validation_dataset.map(lambda example: {'label': 1 if example['star_rating'] > 3 else 0})

books_balanced_validation_dataset = books_validation_dataset.filter(lambda example: example['label'] == 1).shuffle(seed=42)
books_balanced_validation_dataset = books_balanced_validation_dataset.concatenate(books_validation_dataset.filter(lambda example: example['label'] == 0).shuffle(seed=42).select(range(books_balanced_validation_dataset.dataset_size)))
dvd_balanced_validation_dataset = dvd_validation_dataset.filter(lambda example: example['label'] == 1).shuffle(seed=42)
dvd_balanced_validation_dataset = dvd_balanced_validation_dataset.concatenate(dvd_validation_dataset.filter(lambda example: example['label'] == 0).shuffle(seed=42).select(range(dvd_balanced_validation_dataset.dataset_size)))
electronics_balanced_validation_dataset = electronics_validation_dataset.filter(lambda example: example['label'] == 1).shuffle(seed=42)
electronics_balanced_validation_dataset = electronics_balanced_validation_dataset.concatenate(electronics_validation_dataset.filter(lambda example: example['label'] == 0).shuffle(seed=42).select(range(electronics_balanced_validation_dataset.dataset_size)))
kitchen_balanced_validation_dataset = kitchen_validation_dataset.filter(lambda example: example['label'] == 1).shuffle(seed=42)
kitchen_balanced_validation_dataset = kitchen_balanced_validation_dataset.concatenate(kitchen_validation_dataset.filter(lambda example: example['label'] == 0).shuffle(seed=42).select(range(kitchen_balanced_validation_dataset.dataset_size)))

# save the balanced datasets
if not os.path.exists('data/books/validation.csv'):
    os.makedirs('data/books/validation.csv')
if not os.path.exists('data/dvd/validation.csv'):
    os.makedirs('data/dvd/validation.csv')
if not os.path.exists('data/electronics/validation.csv'):
    os.makedirs('data/electronics/validation.csv')
if not os.path.exists('data/kitchen/validation.csv'):
    os.makedirs('data/kitchen/validation.csv')
books_balanced_validation_dataset.to_csv('data/books/validation.csv')
dvd_balanced_validation_dataset.to_csv('data/dvd/validation.csv')
electronics_balanced_validation_dataset.to_csv('data/electronics/validation.csv')
kitchen_balanced_validation_dataset.to_csv('data/kitchen/validation.csv')