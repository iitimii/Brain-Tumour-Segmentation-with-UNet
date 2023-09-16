from subprocess import call
import streamlit as st
import requests

# Define the FastAPI API endpoint URL
api_url = "http://0.0.0.0:10000/upload"  # Replace with the actual URL

# Streamlit app title
st.title("Brain Tumor Segmentation")

# Upload MRI images
st.header("Upload a FLAIR brain MRI scan")
flair = st.file_uploader("Upload a FLAIR brain MRI scan")
st.header("Upload a T1CE brain MRI scan")
t1ce = st.file_uploader("Upload a T1CE brain MRI scan")

# Check if files are uploaded
if flair and t1ce:
    st.write("Files Uploaded!")
    st.write("Processing...")

    # Create a dictionary to store files for FastAPI
    files = {
        "flair": flair,
        "t1ce": t1ce
    }

    # Make a POST request to the FastAPI endpoint
    response = requests.post(api_url, files=files)

    # Check the response status code
    if response.status_code == 200:
        st.success("Segmentation Successful!")

        # Provide a download link for the resulting file
        st.write("Download the segmented MRI:")
        st.download_button(
            label="Download Segmented MRI",
            data=response.content,
            file_name="segmented_mri.nii",
            key="download_button"
        )
    else:
        st.error("Error processing the image. Please try again.")


call(["python", "main.py"])