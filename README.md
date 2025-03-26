Abstract:
This project is titled as Hairstyle Recommendation system. It establishes a relationship between facial features and hairstyles by analyzing the results of facial recognition and supervised machine learning. In this project particularly, the methodology used is a combination of random forest classification and K-fold cross validation. The goal is to create a Hairstyle Recommendation System that suggests hairstyles suiting an individual's unique characteristics. Hairstyle is a significant aspect of personal identity and self-expression. It influences not just our appearance but also our confidence and how we are perceived by others. Especially for occasions where a good haircut is important, such as a job interview; The wrong haircut can badly influence a first impression. Going to the hairdresser comes with difficult decision making. Not knowing their own preferences, the best style suitable for oneself, blindly depending on a hairdresser, not knowing the end result; leads to fear and ambiguity. The impact of the decision makes it hard to choose but also the large amount of options causes difficulty; There are several examples of haircuts; However, these examples are not personalized. A lot of time is consumed but there is no guarantee of a that the hairstyle will look good on the client and make them feel confident. Therefore, challenge that is to be tackled here is to make it easier for people to decide on a new hairstyle by minimizing the risk of a bad hairstyle and limiting the options for a quicker decision. In conclusion, the Hairstyle Recommender System presents an innovative and promising solution for individuals and businesses in the beauty and fashion industry. It Opens up possibilities for users to discover, experiment with, and embrace new hairstyles with confidence.

1	Introduction to Hairstyle Recommendation System:

1.1	Introduction :
The goal of this project, Hairstyle recommendation system is to recommend hairstyles most suitable to an individual. To achieve this the base factor is considered to be the Individual's face shape. There are several different face shapes and each face shape has unique characteristics. Choosing the correct hairstyle is to make sure it highlights the good features while lessening the impact of the other features. For example, a round face shape has same proportions from the forehead to the chin; Therefore, the chosen hairstyle must hide the larger areas and give a shape to the face. This is called face-framing. Similarly, a square face shape is very sharp and angular. Therefore, the chosen hairstyle should passivate the sharp looks and give a softer look. These are few examples of how the face shape majorly impacts the decision making of choosing a hairstyle.

There is a wide range of face shapes. This project considers only four major face shapes that could fit in all the other possible face shapes. They are: round, square, oval and heart. While the face shape is detected by the system, the user must also provide their preferences; The first preferences in hair length either long or short The second preference in hair type; It has three options: curly, wavy and straight Hence, the three factors considered for hairstyle recommendation are face shape, hair length and hair type. Once the three factors are confirmed, three hairstyles are recommended that match these factors. Three images of hair styles are presented along with their name for an easy reference. 

1.2	Methodology:

To satisfy all the above requirements, the objectives can be listed as following:
❖	Data collection
❖	Interface for user input 
❖	Face shape recognition
❖	Model implementation
❖	Model comparison
❖	Recommendations

DATA COLLECTION:
Data collection is the basis of any project. Without the data none of the other objectives can be implemented. Hence, it is necessary to collect accurate data that meets the requirements of other objectives. For this project, there are two sets of data that are required. First one is the data for face shape classification, second is the data for hairstyle recommendations. So, the data required is the different face shapes and hairstyle that suit each face shape. The best source is the celebrity faces. Collecting a set of celebrity faces will include all possible face shapes. It is also easy to find information of each celebrity faces and classify them into the correct face shape. Similarly, it is easier to collect hairstyle images referring to the celebrities.
In this project, the dataset consists a total of 240 celebrity images which is explained in detail in section:4.1. However, it is necessary to ensure the collected image meets the following conditions:
•	Images should have the face facing forward
•	The face should also be facing in the same angle
•	The size of all the images should be scaled to similar sizes for accurate results
•	The image should be clean and clear
•	The image should have the complete face without any disturbances. For example, hair on the face or a face mask.

INTERFACE FOR USER INPUT:
The interface should contain a select button and a confirmation button. The select button lets user browse the files and choose an image. Once chosen the image is displayed. The user then confirms the image by clicking on the ‘OKAY’ button. This interface is made using a python library called TKinter. It is used to create Graphical User Interfaces. It provides a toolkit to create widgets such as buttons, labels, text entries and more.

FACE SHAPE RECOGNITION:
Face shape recognition is divided into three parts:
●	face point extraction
●	face point calculations
●	face shape classification
Using a python library called face_recognition, the face in the input image is divided into 68 points as shown in figure:4. The extracted face points are called as face landmarks represented as in figure:5. These points are used to make several calculations of the features such as face height, face width and many more. These features are calculated using the Euclidian’s distance formula as represented in figure:6. These feature values are then compared and used to classify the face into appropriate face shape.

MODEL IMPLEMENTATION:
Different models that are expected to give the most accurate results are considered and implemented. Using the features calculated, the face shapes are grouped and classified. Therefore, a classification algorithm is used. In a classification algorithm, the model is trained to generalize the labeled data. So, whenever a new instance is added, it is automatically classified into its respective label. In this project, three algorithms are implemented: MLP, Random forest classification and logistic regression. To achieve more accuracy each of these is also implemented in a combination with k-fold.
The Multilayer perceptron is a type of artificial neural network. It is known to handle complex data relationships. It comprises of layers of neurons which help in non-linear mappings within the data. Logistic regression is a statistical model. It predicts probability of an instance belonging to a particular class. It also provides coefficients that indicate the impact of each feature on the classification. Random forest is an ensemble learning method. It constructs multiple decision trees during training and outputs the average prediction. Hence, improves accuracy and robustness.
K-fold is a technique used to evaluate the performance. It partitions the dataset in k folds or subsets. The model is trained on k-1 fold and validated on remaining. This process is repeated k times, each time using a different fold as validation set.

MODEL COMPARISON:
These models are implemented and compared. The model with the highest accuracy is the used in the final implementation. Model comparison is explained in detail in section:4. In this the project the model with highest accuracy is the combination of random forest and k-fold.

RECOMMENDER:
This is the final step of the project; displaying the recommended images. The users are asked for preferences. The preferences are considered and accordingly three images of the recommendations are displayed along with their name. It also displays a statement justifying how these hair styles are the top recommendations. The user is also given an option to get two other hairstyle recommendations. This recommender is made using HTML and JavaScript. The flask library is used to pass the data from python to the html code.
This is the complete description of the methodology and working of the hairstyle recommendation system.

3	Proposed Method:

3.1 Problem Statement:
The problem statement for hairstyle recommendation system is to produce hair style recommendations that best suit the individual using the system. The factors that are to be considered while recommending is the face shape, hair length and hair texture. It also includes providing the user a friendly interface so that they do not have any problems uploading the pictures or while choosing their preferences. As mentioned earlier the system should let the user browse for an image and then upload. The uploaded image after confirmed is used to identify the user’s face shape. The users face shape is displayed and the user chooses their preferences of length and texture. Considering all these factors top three recommendations are produced. If required give the user two other recommendations.
3.2 Objectives:
•	The system takes in the user images as input. While taking the image, it should let the user browse the files and choose an image. The chosen image is displayed. Then the system asks for confirmation. If the user confirms the image proceed for the next operation, else the use can browse and choose another image.
•	If the image is confirmed, identify the face shape and classify it as one of the following four shapes: round, square, heart and oval.
•	Display the user face shape.
•	Ask for user preferences in hair length and hair type. The hair length has two choices: long and short. The hair type has three choices: curly, straight and wavy.
•	After the user confirms their preferences display the recommendations that match the given preferences. Three images of the recommended hairstyles are displayed along with their name.
•	Give an option to get two other recommendations; 


4 Results and Discussions:

To predict the face shape using these features, the model has to be selected and implemented. Three different models are implemented and compared based on accuracy. The models implemented are MLP, logistic regression and random forest classification. They are also implemented with and without k-fold. The following figure:20 Shows the comparison of the models with and without k-fold.

•	The model with highest accuracy is MLP without using k-fold.
•	The model with least accuracy is random forest without k-fold.
•	The highest accuracy achieved without k-fold is 76 percentage.
•	To increase the accuracy k-fold is implemented combined with the previous models.
•	The model with highest accuracy using k-fold is random forest.
•	Both MLP and logistic regression achieved equal accuracy.
•	The highest accuracy achieved using k-fold is 100 percentage.

•	Though random forest was the least accurate without k-fold, it achieved more accuracy with k-fold than the model with highest accuracy without k-fold.
•	The accuracy of both MLP and logistic regression remain almost same with and without k-fold.
•	Since not much difference nor improvement is visible, random forest classification is finalized to be the project implementation model.


5	Conclusion and Future Enhancements:

This section is the summary and conclusion to the project. This project aimed to develop a system for face shape prediction and hairstyle recommendation using image of the user’s face. By analyzing various facial features, the face shape is predicted and suitable hairstyles recommendations based on user preferences are given. The methodology involves classification algorithms such as logistic regression, multi-layer perceptron (MLP), and random forest, with k-fold cross-validation to enhance accuracy. The dataset consists of 240 images of females aged between 15-30; divided into four face shapes (round, square, heart, and oval). After various experiments, the random forest classifier combined with k-fold cross-validation produced the highest accuracy. Hence, is the chosen method for implementation.

This system aimed to help the users in choosing hairstyles that suit their face shape by machine learning algorithms to analyse and classify facial features. Therefore, the project focused on improving the accuracy of face shape prediction and providing personalized hairstyle recommendations.
The already existing systems have used face recognition and shape prediction using various machine learning techniques. Common methods included logistic regression, neural networks, and decision trees. However, they faced many challenges such as limited datasets, imbalanced data, and varying accuracies across different models. This project aimed to overcome these issues by experimenting with multiple algorithms and incorporating k-fold cross-validation for better performance.

The methodology involved several steps: data collection, feature extraction, algorithm selection, model training and testing, and evaluation. The dataset of 240 images was categorized into four face shapes. Each face shape had 30 images, categorized based on hair length and type, resulting in 24 possible combinations. Key facial features (height, width, jaw-width, chin width, side length) were measured using specific points on the face.

Face shape determination involved calculating distances between the facial points and comparing average values for all the face shapes. The face shapes were grouped based on similarities in these parameters. Further improvements were made using ratios of these parameters. Three models (MLP, logistic regression, random forest) were tested with and without k-fold cross-validation.

The random forest classifier with k-fold cross-validation achieved the highest accuracy (100%), making it the preferred model. The MLP without k-fold showed the highest accuracy without cross-validation (76%). The random forest classifier with k-fold cross-validation achieved 100% accuracy in predicting heart and oval face shapes. While round and square shapes were less accurately predicted. However, the system overall demonstrated significant accuracy. Therefore, this project successfully developed a system for predicting face shapes and recommending hairstyles using machine learning algorithms.







For all the ideas mentioned to work, it requires a huge amount of data which satisfies various requirements. It also requires a huge dataset for recommendations. It has to be an environment where the system is constantly updating and meeting with the latest trends. It should turn into a System that is changing every day for a Better user experience. Only then will the Recommendation system be useful in the Industry as well as in the daily life of an average user. The enhancement of this project will also lead to enhancement of industry. Overall, this project laid a strong foundation for developing an effective and reliable face shape prediction and hairstyle recommendation system.
