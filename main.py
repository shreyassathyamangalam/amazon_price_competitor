# Import libraries
import streamlit as st


def render_header():
    """Renders streamlit header"""
    
    st.title("Amazon Product Analysis")
    st.caption("Enter the ASIN to get product insights")

def render_inputs():
    """Render the input fields"""
    
    asin = st.text_input("ASIN", placeholder="e.g. B06Y1YD5W7")
    geo = st.text_input("Zip/Postal Code", placeholder="e.g. 83098")
    domain = st.selectbox("Domain", [
        "com", "ca", "co.uk", "de", "fr", "it", "ae"
    ])
    
    return asin.strip(), geo.strip(), domain

def main():
    st.set_page_config(page_title="Amazon Product Analysis", page_icon="📚", layout="wide")
    render_header()
    asin, geo, domain = render_inputs()
    
    if st.button("Scrape Product") and asin:
        with st.spinner("Scraping Product..."):
            st.write("Scraping Product")
            # Todo scrape product
        st.success("Product Scraped Successfully!")
        


if __name__ == "__main__":
    main()
