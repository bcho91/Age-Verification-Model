# Project 5:

Project members: Ani Zotti, Ashanti Jabri, Brian Cho

## Problem Statement

In today's digital society, parents and officials have actively fought child exploitation on the internet. Online enticement occurs across all platforms, this can involve illegal video content of minors, online enticement of children, or the transaction of a child's sexual images to others. Snapchat is one of many social media applications where age verification would play a major role. Snapchat is particularly dangerous for children because the snaps/media content are quickly deleted. This makes it incredibly difficult for parents/officials to see what the child is doing with the application. Age verification processes and the Children's Online Privacy Protection Rule are some practices that were designed to restrict adult content to minors. However, many age verification processes can be easily bypassed (children can create fake emails, parents can lie, etc.). In this project, our team will explore how we can build a model that can take an image and classify whether it is a child or an adult.

In this project, our team utilized three different deep neural networks to classify photos as either children or adults (trained Convolutional Neural Network, ResNet50, and VGG-16). Success was determined through a variety of classification metrics: accuracy, loss, precision, and recall.

## Summary

### Datasets Used:

The dataset used was the UTKFace dataset. The dataset consists of over 20,000 images with annotations of age, gender, and ethnicity with ages that range from 0 to 116 years old (https://susanqq.github.io/UTKFace/).

### Data Cleaning & EDA

The UTKFace Dataset had images that were already cleaned and labelled. The format of the labels is as follows:

[age]\_[gender]\_[race]\_[date&time].jpg

The team created a dataframe which included the file name and the corresponding age that is associated with the file. Ages 0-17 were defined as children and ages 18 and up were defined as adults.

### Pre-processing

The original dataset had an imbalance of classes, less than 20% of the data had faces that were of ages 18 and below.

![Distribution of Classes Before Image Augmentation](https://raw.git.generalassemb.ly/briancho/Submissions/master/projects/project%205/images/project5dist1.png?token=AAAIJS2N2E3E5MFZALJFDLTAOT6LG)

In order to balance the classes, we augmented images from ages 0-17 and incorporated them into the dataset. The dataset had an even balance of photos that incorporated child and adult faces.

![Distribution of Classes After Image Augmentation](https://raw.git.generalassemb.ly/briancho/Submissions/master/projects/project%205/images/project5dist2.png?token=AAAIJS7OKDZC2CX6FHHWJH3AOT6NC)

Once the team balanced the classes, the dataset was split between train, validation, and testing datasets.

### Modeling Process

In the modeling process, the team utilized three models. The Convolutional Neural Network model that was trained, the ResNet50 model, and the VGG-16 model. Transfer learning was utilized on the ResNet50 and VGG-16 models in order to classify photos as adults or children.

Evaluation:

Our trained CNN model performed extremely well compared to the ResNet50 and VGG-16 models. The Dream Team model had an accuracy score of 99.45%, loss of 0.31%, precision score of 99.14%, and a recall score of 99.67%.

![Trained CNN Model](https://raw.git.generalassemb.ly/briancho/Submissions/master/projects/project%205/images/dreamteam.png?token=AAAIJS232EUCXNLB543ELBLAOT6VO)

The ResNet50 model had an accuracy score of 94.92%, loss of 1.5%, precision score of 94.36%, and a recall score of 98.5%.

![ResNet50](https://raw.git.generalassemb.ly/briancho/Submissions/master/projects/project%205/images/resnet50.png?token=AAAIJS77A7SMVG5WJGYG3DLAOT6W4)

Lastly, the VGG-16 model performed the best with an accuracy score of 99.78%, loss of 0.08%, precision score of 99.83%, and a recall score of 99.89%.

![VGG-16](https://raw.git.generalassemb.ly/briancho/Submissions/master/projects/project%205/images/vgg16.png?token=AAAIJS5K437MVF3U5AOE6STAOT6YC)

### Deployment

The team utilized Streamlit to build the user interface of the application. The application can be utilized at https://dream-team-age-classifier.herokuapp.com/. The binary age classification app was then deployed on Heroku.

## Conclusion/Recommendations

Adding an additional layer of security for age verification can prove to be useful for parents and organizations alike. By utilizing our binary classification model, organizations can incorporate a facial recognition feature to verify ages for their users and prohibit minors from accessing adult content. This solution also aims to provide companies with preventative measures against possible litigation and public complaints for not adding the necessary security measures. Another application for this model is to detect children in pornographic material and other forms of child sexploitation.

We recommend that this model serves as the basis for classifying children and adults. In order to improve upon this application, one can utilize the OpenCV library to incorporate a real-time facial recognition system that can identify children/adults in real time.