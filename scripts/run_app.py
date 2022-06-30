import streamlit as stl
from PIL import Image
from dna_app import generate_chart
from text_content import get_text_content


def main():
    image = Image.open('../imgs/DNA_dynamic.jpg')
    stl.image(image, use_column_width=True)

    # Header
    stl.markdown("<h2 style='text-align: center; font:bold'>DNA Nucleotide Count Web App</h2>", unsafe_allow_html=True)

    # Intro for the web app
    stl.markdown('''<h6 style='text-align: center; font:bold'>This app counts the nucleotide composition of query 
    DNA.</h6>''', unsafe_allow_html=True)
    stl.write("""
    ***
    """)
    stl.header('Enter DNA sequence')

    generate_chart()

    stl.write("""
    ***
    """)
    get_text_content()


if __name__ == '__main__':
    main()
