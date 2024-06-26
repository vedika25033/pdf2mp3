import pyttsx3
import PyPDF2
import tkinter as tk
from tkinter.filedialog import askopenfilename

# Initialize tkinter and hide the root window
root = tk.Tk()
root.withdraw()

# Open a file dialog to select a PDF file
book = askopenfilename(
    title="Select PDF file",
    filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
)

# Check if a file was selected
if not book:
    print("No file selected.")
else:
    try:
        # Open the PDF file
        with open(book, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            pages = len(pdf_reader.pages)
            print(f"Number of pages: {pages}")

            # Initialize the text-to-speech engine
            speaker = pyttsx3.init()
            rate = 150  # Speed: 150 words per minute (slower than default)

            # Set speech rate
            speaker.setProperty('rate', rate)

            # Variable to hold all the text from the PDF
            full_text = ""

            # Iterate through all the pages in the PDF
            for page_num in range(pages):
                # Extract text from each page
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                if text:  # Check if text extraction was successful
                    # Clean the extracted text
                    clean_text = text.strip().replace('\n', ' ')
                    print(f"Extracted text from page {page_num + 1}: {clean_text[:100]}...")  # Print first 100 characters
                    # Add the clean text to the full text
                    full_text += clean_text + " "
                else:
                    print(f"Warning: No text extracted from page {page_num + 1}")

            print("Full text:", full_text[:100])  # Print first 100 characters of full text

            # Ensure there is text to read
            if full_text:
                # Save the full text to an MP3 file and speak it
                speaker.save_to_file(full_text, 'story.mp3')
                speaker.runAndWait()
                print("The story has been saved to 'story.mp3'")
            else:
                print("No text extracted from the PDF.")

            # Stop the speaker
            speaker.stop()

    except Exception as e:
        print(f"An error occurred: {e}")