# medical_image_processing_using_filters

In this simple medical imaging application , we tried to build a simple medical imaging processing application using monai framework,.

-First we were in need to test medical images , fortunately there is radiopaeda which is an opensource pedia for medical images
under Case courtesy of Stefan Tigges, <a href="https://radiopaedia.org/?lang=us">Radiopaedia.org</a>. From the case <a href="https://radiopaedia.org/cases/98013?lang=us">rID: 98013</a>

![normal-brain-mri-42](https://user-images.githubusercontent.com/37244966/171997160-1d5e3d38-7d7a-4d40-876e-e1ebe8cd4ec0.png)

-This is a normal brain MRI from sagittalT1 view ,the MRI is in PNG format which facilitates the mission.

-Second we have to define the most common operations to be performed upon this MRI , refering to MONAI they used 3 image processings techniques ,
which are Guassian , Sobel and median operations 

-Third after applying the three operators the result was as shown 




![final_output](https://user-images.githubusercontent.com/37244966/171997366-e62a6726-0a68-4a7f-b68a-835bfb75979a.png)



-Fourth the Application needs to be packed in order to be converted into Docker image for production , thanks to MONAI SDK for making this step easier. 


-Repository structure is as follows


1-filter adding to medicalimage -> main development code and the application file.


2-input -> input images used to test the filters.

3-output -> output results after filters operations. 


4-execution and packaging -> script to package the application into a container.



5-application_Docker file -> Docker container that carries and includes application files for ready made usage.
