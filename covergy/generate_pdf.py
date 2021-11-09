import jinja2
import pdfkit
from pathlib import Path
def get_filename(filename):
    return filename.replace(" ", "_")

def generate_pdf(filename = "bob"):
    html_path = Path("html")
    html_file = filename.replace(".pdf", ".html")
    html_full = html_path / html_file
    pdf_path = Path("pdf")
    full_path = pdf_path / filename
    
    pdfkit.from_file(str(html_full), str(full_path))



def generate_html(app_name = "covergy",html_file = "default.html",user_name = "Bob",**kwargs):
    filename = get_filename(user_name)
    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = f"./{app_name}/templates/{html_file}"
    template = templateEnv.get_template(TEMPLATE_FILE)
    outputText = template.render(**kwargs)
    data_folder = Path("html")
    filename = filename+'.html'
    html_file = open(data_folder / filename, 'w+')
    html_file.write(outputText)
    html_file.close()

def generate_output(user_name):
    generate_html(user_name=user_name,name=user_name)
    filename = get_filename(user_name)+'.pdf'
    generate_pdf(filename=filename)

generate_output("Martin Yanchev")