# FYP-Randec
This is the repository of github for Randec-II (maker is i160164@nu.edu.pk, nu id does not receive any mails regarding github :( )

Note of Clarrification: This project is done by two members, Afaq Asif (<i170217@nu.edu.pk>) and Usman Ali (<i160164@nu.edu.pk>) <br />
The files we have here:    <br />
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
      (or yarn install for yarn framworks for reactnative and angular combined) within the folder  <br />
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
