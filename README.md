# Agricultural Crop Classification Model

This repository contains an agricultural crop classification model implemented using transfer learning and the fastai library. The model is designed to classify different types of crops based on input images.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [Results](#results)

## Introduction

Crop classification plays a crucial role in agriculture for various applications such as monitoring, yield estimation, and disease detection. This project focuses on building an accurate crop classification model using transfer learning, which leverages the pre-trained weights of a deep learning model trained on a large dataset.

## Dataset

To train and evaluate the model, we use a [dataset](https://www.kaggle.com/datasets/mdwaquarazam/agricultural-crops-image-classification) consisting of images of various agricultural crops. The dataset contains labeled images for different crop categories, such as wheat, tomato, rice, soyabean, etc. Each image is associated with a specific crop class.

The dataset used in this project is not included in the repository due to its large size. However, you can obtain a similar dataset from public agricultural image datasets or collect your own dataset for training the model.

## Model Architecture

The agricultural crop classification model is implemented using the fastai library, which provides a high-level API for deep learning tasks. The model architecture follows a transfer learning approach, utilizing a pre-trained convolutional neural network (CNN) as the base model. The base model used in this project is ResNet-101, a widely adopted CNN architecture known for its excellent performance on image classification tasks.

## Results

After training the crop classification model on a suitable dataset, you can evaluate its performance by measuring metrics such as accuracy on a validation set. Accuracy achieved = 79%
