
Developed a website utilizing Streamlit and lottie packages that showcase my personal information and data in an interactive and engaging way.

Step 1: Imported all the packages listed in the requirement.

Step 2: Set the page congifuration and the styling of the page and icon.
        Find more page icon here: https://www.webfx.com/tools/emoji-cheat-sheet/ 

Step 3: Next created the Header section where I have made a container and in that added a subheader,title and the links .

Step 4: Then I have created the "About" Section.
        In this we have divided the page into 2 halves(left and right column)
        left column include only the text,the right column includes the image,
        basically it is the animated image which makes the User Interface more 
        appealing.
        In this part we have taken the help of lottie module of the streamlit.
        Copied the link of the GIF and pasted in the load_lottieurl function.

Step 5: Further headed to make the section of "PROJECT" here also we have divided the page into 2 halves(image_column, text_column) where the width of the image_column is less than that of the text_column.
In this step we have made a folder named "image" in the working directory and downloaded the image that i have to see in the webpage in that directory.
Here we have used PIL Image package to import image from the folder.

Step 6: Further headed towards "Contact" and created a response generated tabs where one has to write their Names,Email ID and the message they have to send to me.
In this module I have taken the help of "formsubmit.co" and linked my email to the form.

Step 7: For the styling and structured font I have used style.css folder in which their is a code for styling and structured format,which I got it from https://www.w3schools.com/howto/howto_css_contact_form.asp 
