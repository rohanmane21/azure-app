<h1>Microsoft-Future-Ready-Talent-Virtual-Internship-Project</h1>
<h2>Project Title:</h2><b><a href="https://webpicanalyzer.azurewebsites.net/">Image Analyzer Using Computer Vision.</b></a>
<br>
<h2>Project Details</h2>
<b>Project Demo URL :</b> https://aiwebappazure.azurewebsites.net/ <br>
<b>Demo Video URL :</b> https://drive.google.com/file/d/1bLptg01EM3NtTRZY6j6X_FCmrwf_2TN9/view <br>
<b>Github Repository URL :</b> https://github.com/rohanmane21/azure-app.git <br>
<b>Industry :</b> Lifestyle<br>
<h2>Azure Services Used</h2>
<h3>
Core Azure Services : <br>
1. Azure App Service <br>
2. Azure Storage Account(Blob Storage)  <br> <br>
Azure AI Service <br>
1. Azure AI Computer Vision Service
</h3>
<h2>Problem Statement</h2>
<p align="justify">Developing an AI-based image analysis system to accurately classify and recognize diverse objects in complex visual environments poses a significant challenge.This project aims to enhance the efficiency and robustness of image analysis through advanced AI techniques, addressing the complexities associated with diverse and dynamic visual data.</p>
<h2>Project Description</h2>
<p align="justify">This project enables users to seamlessly upload images and leverage the power of the Azure Computer Vision API for comprehensive image analysis. By storing images securely in Azure Blob Storage and utilizing advanced image processing capabilities, users gain valuable insights into the content of their uploaded images. </p><br>
<b>Key Features :</b>
<ul>
    <li>Azure App Service for Hosting</li>
    <li>User-Friendly Interface</li>
    <li>Real-time Processing</li>
    <li>Accuracy and Reliability</li>
    <li>Azure Blob Service for Efficient Data Management</li>
</ul>
<b>Future Enhancements :</b>
<ul>
    <li>Improve the user interface with additional features.</li>
    <li>Implement user authentication and authorization.</li>
    <li>Explore additional Computer Vision API features for more detailed analysis.</li>
    <li>Consider incorporating frontend frameworks or libraries for a more interactive user experience.</li>
<h2>Core Azure Services</h2>
<b>Azure App Service :</b><br><p align="justify"><br>Azure App Service is a fully managed platform-as-a-service (PaaS) offering provided by Microsoft Azure. It enables developers to build, deploy, and scale web apps and APIs quickly without managing the underlying infrastructure. Azure App Service supports multiple programming languages, frameworks, and operating systems, providing a flexible and scalable environment for hosting various types of applications.</p>
<b>Azure Storage Account(Blob Storage) :</b><br><p align="justify">Azure Blob Storage is a cloud-based object storage service provided by Microsoft Azure. It is part of the Azure Storage services suite, offering scalable and secure storage for a variety of data types, including text and binary data such as images, videos, documents, and more. Azure Blob Storage is widely used for storing and managing unstructured data in the cloud.</p>
<h2>Azure AI Computer Vision Service</h2>
<b>Azure AI Compuetr Vision Service :</b><br><br><p align="justify">Azure offers an AI-powered Computer Vision service that enables developers to integrate computer vision capabilities into their applications without the need for extensive expertise in machine learning or computer vision algorithms.</p>
<h2>Project Flow</h2>
<p align="justify">
    <li><b>Step 1:</b> User Uploads an Image:</li>
    -Users access the web application and use the provided interface to upload an image.
    <li><b>Step 2: </b> Image Stored in Azure Blob Storage:</li>
    -<b>The upload_to_blob_storage</b> function is called to upload the image data to a specific container in Azure Blob            Storage.</li>
    <li><b>Step 3:</b> Retrieve Image for Analysis:</li>
    -When the user wants to view the analysis results, the application retrieves the image data from Azure Blob Storage.
    <li><b>Step 4:</b> Encode Image Data in Base64:</li>
    -The application encodes the image data in Base64 format. This encoded image is then used for display and analysis.  
    <li><b>Step 5:</b> Analyze Image Using Azure Computer Vision:</li> 
    -The encoded image is sent to the Azure Computer Vision API for analysis.The API returns analysis results, including categories, description, and color details.<br>
    <li><b>Step 6:</b>Display Results:</li>
    -The application extracts relevant information from the analysis results, such as image captions.
     The result page is rendered with the analyzed information, providing insights into the content of the uploaded image.

<h2>Screenshots</h2>
<h3>Azure App Service</h3>
<b>Description :</b><p align="justify">Azure App Service provides a scalable and reliable hosting environment for the Multilingual Content Hub. It ensures seamless deployment and high availability, facilitating an optimal user experience.</p>
<img src="https://github.com/rohanmane21/azure-app/blob/17340bb4d43505e11b211633c055becba967712b/screenshots/Screenshot%20from%202024-01-16%2007-21-03.png"></img><br>
<h3>Azure Storage Account(Blob Storage)</h3>
<b>Description :</b><p align="justify"> <b>Blob:</b> Binary Large Object, representing the data that you store in Azure Blob Storage. Blobs can be of different types, such as Block Blobs (optimized for streaming and storing large amounts of data) and Page Blobs (optimized for random read/write operations).</p>
<p> <b>Container:</b>A container is a logical unit for organizing blobs. All blobs must be stored in a container. Containers are similar to directories in a file system and help in organizing and managing blobs.</p>
<img src="https://github.com/rohanmane21/azure-app/blob/main/screenshots/Screenshot%20from%202024-01-16%2007-23-34.png"></img><br>
<h3>Azure AI Computer Vision/Custom Vision</h3>
<b>Description :</b><p align="justify">Azure Computer Vision API can analyze the content of an image, extracting information such as objects, brands, faces, and text. It can identify and categorize visual content, providing details about what is present in the image.</p>
<img src="https://github.com/rohanmane21/azure-app/blob/main/screenshots/Screenshot%20from%202024-01-16%2007-24-16.png"></img><br>
<h3>Working Live Project Display </h3>
<b>Description :</b><p align="justify">Here, I am attaching the final working website's screenshots for the reference.</p>
<img src="https://github.com/rohanmane21/azure-app/blob/main/screenshots/Screenshot%20from%202024-01-16%2014-19-11.png" alt="final-project-demo"></img>

<h3>Choosen Image: </h3>
<p align="justify">Select Image from local machine.</p>
<img src="https://github.com/rohanmane21/azure-app/blob/main/screenshots/Screenshot%20from%202024-01-16%2014-20-06.png"></img>
<h4>Output Page: </h4>
<p align="justify">Image after Analysis with analyzed Captions.</p>
<img src="https://github.com/rohanmane21/azure-app/blob/main/screenshots/Screenshot%20from%202024-01-16%2014-20-54.png"></img>
<h2>Conclusion:</h2>
<p align="justify">
<b>The image analysis web application successfully combines the capabilities of Azure Blob Storage and Azure Cognitive Services - Computer Vision API to provide users with a seamless and insightful experience and gives the captions for analyzed images. Through the integration of these Azure services.</b>
</p> <br>
</h2><b><a href="https://webpicanalyzer.azurewebsites.net/">Image Analyzer Using Azure AI Computer/Custom Vision Service</b></a>
