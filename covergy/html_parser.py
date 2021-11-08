from jinja2 import Environment, PackageLoader, select_autoescape

class HtmlParser:
    def __init__(self,app_name = "covergy",html_file = "default.html"):
        self.env = Environment(loader=PackageLoader(app_name),
                        autoescape=select_autoescape())
        self.template = self.env.get_template(html_file)

    def generate(self,**kwargs):
        return self.template.render(**kwargs)
