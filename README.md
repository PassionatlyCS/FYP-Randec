# FYP-Randec
This is the repository of github for Randec-II (maker is i160164@nu.edu.pk, nu id does not receive any mails regarding github :( )

Note of Clarrification: This project is done by two members, Afaq Asif (<i170217@nu.edu.pk>) and Usman Ali (<i160164@nu.edu.pk>) <br />
The files we have here:    <br />
   **For static analysis:**
   
   DataSetCSV on Ransomeware   <br />
   1. DataSet  <br />
      i.) Data.rar -> Kaggle dataset in the form of PE header files as csv (CS5242 Competition Kaggle 2017 https://www.kaggle.com/c/cs5242-malware-detection/data )<br />
      ii.) FeatureFile.rar (Multiple featureframes is a feature file -> output of our code) <br />
      iii.) Malware.rar (cuckoo sandbox malicious reports from multiple datasets from https://virusshare.com/)  <br />
      iv.) RawReports.rar (raw reports previously were not being downloaded, can be accessed 12/30/2020 2:01pm onwards  <br />
      For raw analysis reports: https://drive.google.com/file/d/1-ZumQ-qnHQgEm-kumToXQLxHEYpOLTHS/view?ts=5fb92f0a (too big to be uploaded here)   <br />
      <br />
      
   Codes on / for Datasets  <br /> 
   2. Codes  <br />
   i.) BinaryClassification over Data.csv  <br />
   ii.) Feature Creation over Malware Reports <br /> 
  
  
   Website Development Code      <br />
   3. Code on Website Development   <br />
      i.) Install Node.js  <br />
      ii.) Install Angular  https://angular.io/guide/setup-local    <br />
      iii.) Download the file from the link - unzip and goto the folder then from console npm install <br />
      (or yarn install for yarn framworks for react native and angular combined) within the folder  <br />
      - Note: you can install react native now, for future iterations from https://reactnative.dev/docs/getting-started   <br />
      -- Within the directory run npm install and npm start (undecided if watch method will be implemented later with mongodb)   <br />
      --- This should run the website on a browser window http://localhost:4200/home  <br />
      
      Link: https://drive.google.com/file/d/1ixoRqDeEUMmOAPHLTcxgtTomcwGdjggg/view?usp=sharing (only opens with nu id)
   
   How to run the code:  <br /> 
   Binary Classificaiton  <br /> 
   Step 1   Download Data.rar -> extract it and the use the csv file only.  <br /> 
   Step 2   Run BinaryClassification.ipynb and get the results  <br /> 
   
   Feature Creation:  <br /> 
   Step 1   Download rawreports.rar (or malware.rar). Use all csv files  <br /> 
   Step 2   Run FeatureCreation which will append data in the featurefile.csv  <br /> 

**for hybrid analysis:**
for prepared benign and malware images dataset:

training dataset
https://drive.google.com/drive/folders/1iBpH19WuitFQkXNK4lCSMMk38jkN71Jk?usp=sharing

testing dataset
https://drive.google.com/drive/folders/17kSASkX-NQuHZk-WaRy3EE1qNK9CmHZu?usp=sharing

for sources and preparing dataset on your own:
Dataset for malware images:
https://www.dropbox.com/s/ep8qjakfwh1rzk4/malimg_dataset.zip?dl=0

1)Download image dataset from the above link
#the dataset is mentioned in a couple of research papers and a link for one paper is given below
https://arxiv.org/pdf/2010.16108.pdf

Dataset for benign exe files:
https://figshare.com/articles/dataset/Malware_Detection_PE-Based_Analysis_Using_Deep_Learning_Algorithm_Dataset/6635642

1)The above link has 1000 benign exe files.
2)Code to convert these files to grayscale images is present in "Code for hybrid analysis" in "Codes".
3)After converting benign exe files to grayscale images, you have to move them all to a single folder and name the folder as "benign"
4)Move all the malware images out of their parent directories and inside a single directory named "malicious"
5)Move both directories of malicious and benign in to a new directory of "train"
6)You can also choose to split the images in testing and training datasets.
7)Copy and paste the training dataset path specified in the code.


**Running the hybrid analysis code:**
reference link for vgg16
https://machinelearningmastery.com/how-to-develop-a-convolutional-neural-network-to-classify-photos-of-dogs-and-cats/
last code snippet is used as it has employed transfer learning

1)Code is also changed for ResNet50,InceptionV3 and Xception 
2)Provide training path where specified in code
3)Provide test file path in run_example1() for classification
4)link for implemented research paper is given below
https://www.researchgate.net/publication/342167624_FCNNMD_A_Novel_Fusion_Method_based_on_Convolutional_Neural_Network_for_Malware_Detection




