import fitz
from docx import Document
import os


UPLOAD_FOLDER="uploads"


os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


def save_file(file):

    path=f"{UPLOAD_FOLDER}/{file.filename}"

    with open(path,"wb") as f:
        f.write(file.file.read())

    return path



def extract_text(path):

    if path.endswith(".pdf"):

        text=""

        pdf=fitz.open(path)

        for page in pdf:
            text += page.get_text()

        return text


    elif path.endswith(".docx"):

        doc=Document(path)

        text="\n".join(
            [
                p.text 
                for p in doc.paragraphs
            ]
        )

        return text


    else:

        raise Exception(
            "Only PDF and DOCX allowed"
        )