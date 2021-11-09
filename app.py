import jinja2

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "pdf_interest_report.html"
template = templateEnv.get_template(TEMPLATE_FILE)


outputText = template.render(name = "Martin")
html_file = open('martin'+ '.html', 'w')
html_file.write(outputText)
html_file.close()

