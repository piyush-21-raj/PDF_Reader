import streamlit as st


def main():
    st.set_page_config(page_title='Streamlit App', page_icon=':shark:', layout='wide')

    st.header('Streamlit App')
    st.text_input('Enter your name', 'Type here...')

    with st.sidebar:
        st.subheader('PDFs to be read')
        st.file_uploader('Upload PDFs and click on process')
        st.button('Process')

if __name__ == 'main':
    main()