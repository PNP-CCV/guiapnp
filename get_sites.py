import requests
import xml.etree.ElementTree as ET
import pdfkit
import os
from PyPDF2 import PdfMerger
import tempfile
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from google.cloud import storage

def get_urls_from_sitemap(sitemap_url):
    response = requests.get(sitemap_url)
    response.raise_for_status()
    root = ET.fromstring(response.content)
    urls = [elem.text for elem in root.iter() if elem.tag.endswith('loc')]
    return urls

def get_urls_from_navbar(base_site):
    response = requests.get(base_site)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    menu_nav = soup.find('nav', class_='menu-body')
    if not menu_nav:
        # fallback: try to find by id
        menu_nav = soup.find('nav', id='main-navigation')
    if not menu_nav:
        raise Exception('Could not find navbar/menu in the HTML')
    urls = []
    # 1st level links
    for a in menu_nav.find_all('a', class_='menu-item divider', href=True):
        href = a['href']
        if href.startswith('javascript'):  # skip dummy links
            continue
        urls.append(urljoin(base_site, href))
    # 2nd level links (inside menu-folder > ul > li > a)
    for folder in menu_nav.find_all('div', class_='menu-folder'):
        ul = folder.find('ul')
        if ul:
            for li in ul.find_all('li'):
                a = li.find('a', class_='menu-item', href=True)
                if a:
                    href = a['href']
                    if href.startswith('javascript'):
                        continue
                    urls.append(urljoin(base_site, href))
    return urls

def download_as_pdf(url, output_path):
    try:
        # Create temporary CSS to hide header, navbar, and footer elements
        css = """
        footer, .footer, #footer, [class*='footer'], [id*='footer'],
        header, .header, #header, [class*='header'], [id*='header'],
        nav, .nav, #nav, [class*='nav'], [id*='nav'] {
            display: none !important;
        }
        """
        
        with tempfile.NamedTemporaryFile(suffix='.css', mode='w', delete=False) as f:
            f.write(css)
            css_path = f.name
        
        options = {
            'user-style-sheet': css_path
        }
        
        # Use wkhtmltopdf config if needed
        path_wkhtmltopdf_win = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        path_wkhtmltopdf_linux = '/usr/bin/wkhtmltopdf'
        config = None
        if os.path.exists(path_wkhtmltopdf_win):
            config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf_win)
        elif os.path.exists(path_wkhtmltopdf_linux):
            config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf_linux)
        
        pdfkit.from_url(url, output_path, options=options, configuration=config)
        
        # Clean up temporary CSS file
        os.remove(css_path)
        return True
    except Exception as e:
        print(f"Error converting {url} to PDF: {e}")
        return False

def merge_pdfs(pdf_files, output_path):
    merger = PdfMerger()
    for pdf in pdf_files:
        if os.path.exists(pdf):
            merger.append(pdf)
    merger.write(output_path)
    merger.close()

def upload_to_gcs(bucket_name, source_file, destination_blob, credentials_path):
    client = storage.Client.from_service_account_json(credentials_path)
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob)
    blob.upload_from_filename(source_file)
    print(f"Uploaded {source_file} to gs://{bucket_name}/{destination_blob}")

if __name__ == "__main__":
    #sitemap_url = "https://referencialpnp.dsbr.org/sitemap.xml"
    base_site = "http://127.0.0.1:4000/guiapnp/"
    #urls = get_urls_from_sitemap(sitemap_url)
    urls = get_urls_from_navbar(base_site)
    
    # Create temp directory for individual PDFs
    temp_dir = "temp_pdfs"
    os.makedirs(temp_dir, exist_ok=True)

    pdf_files = []
    print(f"Found {len(urls)} URLs to process (from navbar order)")
    
    # Download and convert each URL to PDF
    for i, url in enumerate(urls):
        print(f"Processing {i+1}/{len(urls)}: {url}")
        output_pdf = os.path.join(temp_dir, f"page_{i}.pdf")
        if download_as_pdf(url, output_pdf):
            pdf_files.append(output_pdf)
    
    # Merge all PDFs
    if pdf_files:
        output_file = "./guiapnp.pdf"
        print(f"Merging {len(pdf_files)} PDFs into {output_file}")
        merge_pdfs(pdf_files, output_file)
        print(f"Successfully created {output_file}")
        print(f"The PDF is available at: ./guiapnp.pdf")
    else:
        print("No PDFs were created.")