Optical Character Recognition (OCR) is a technology used to convert different types of documents—such as scanned paper documents, PDFs, or images taken with a camera—into editable and searchable text. OCR identifies and extracts characters from images, such as letters and numbers, making it possible to digitize printed texts for further processing.

Key Features and Uses of OCR:-
(i) Text Recognition: Recognizes and extracts text from scanned images or photos.
(ii) Searchability: Converts printed text into a format that can be indexed and searched.
(iii) Document Automation: Often used in automation processes for digitizing data.
(iv) Applications: Used in various fields like banking (for check processing), education, document management, and more.

Case statement:- We operate in the B2B space, sourcing items from APMC (Agricultural Produce Market Committee) buyers, among others. To calculate the final margin on our IRN (Invoice Reference Number), we need to exclude APMC cess, which, although payable to the government, should not impact our margin calculations. However, distinguishing between APMC and other buyers in our records has been challenging, especially since the invoice data is provided in PNG format. As a Data Analyst focused on staples, I'm responsible for addressing this issue. 

Technology used:- 
   > OCR(Optical character recognition) by pytesseract library.

Working Procedure:

1) Data Collection and Initial Setup: First, we collect the dataset and load it into a pandas DataFrame. We need to read each invoice link in .jpeg or .jpg format. To do this, we import  necessary modules such as requests, Image and BytesIO from PIL to handle image processing.

2) Image Retrieval and Validation: Each invoice image is accessed via its URL. We apply logic to verify that the image is accessible online by checking if request.status_code == 200.     This ensures that we only process images successfully retrieved from the web.

3) OCR Application: Once validated, each image is passed to the PyTesseract module. The image is then converted to text using image_to_string.

4) APMC Identification: We check for the presence of terms like "apmc yard" or "apmc" within the extracted text. If these terms are found, we mark an apmc_check field as "yes"; otherwise, it is set to "no".

This workflow allows us to systematically process each invoice and flag those that contain APMC-specific identifiers.

   
Sample input data_set snap :- ![image](https://github.com/user-attachments/assets/54486934-2647-4e9b-9f2c-14ca323ea45c)

Sample output snap :- ![image](https://github.com/user-attachments/assets/ce87380b-0b73-4993-99a1-31e80418e22f)

