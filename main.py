#comentarios aqui
import os
import webapp2
import jinja2

#aqui se cargan los path para la carpeta templates
JINJA_ENVIRONMENT = jinja2.Environment(
    loader= jinja2.FileSystemLoader(os.path.dirname(__file__)+"/templates"))

#este es el main es y aparti de aqui se manda llamar atodo lo demas
class MainHandler(webapp2.RequestHandler):
    def get(self):
        title = "Paginas web con Python"
        #se crea un diccionario para enviarselo al html y este lo lee con el nombre que se le da en el
        #archivo html en este caso es el titulo el que estara cambiando segun la pagina
        template_vars = {
            "title": title
        }
        template = JINJA_ENVIRONMENT.get_template("index.html")
        #aqui se renderiza el index
        self.response.write(template.render(template_vars))

class ProductsHandler(webapp2.RequestHandler):
    def get(self):
        title = "Productos"
        template_vars = {
            "title":title
        }
        template = JINJA_ENVIRONMENT.get_template("products.html")
        #aqui se renderiza el index
        self.response.write(template.render(template_vars))

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        title = "Acerca de mi"
        template_vars = {
            "title":title
        }
        template = JINJA_ENVIRONMENT.get_template("about.html")
        #aqui se renderiza el index
        self.response.write(template.render(template_vars))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/products.html', ProductsHandler),
    ('/about.html', AboutHandler),
], debug=True)
