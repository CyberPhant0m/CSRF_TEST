import bs4
import argparse
import requests
import ast
from os import system
import os
from termcolor import colored 


parser = argparse.ArgumentParser()
parser.add_argument('--method', help='Indicar metodo [GET, POST]')
parser.add_argument('--enctype', help='Indicar tipo de encriptacion')
parser.add_argument('--url', help='Indicar URL')
parser.add_argument('--fields', help='Indicar valores de campos "Input".')
parser.add_argument('--output', help='Indicar nombre de archivo')

def csfrpoc():
    args = parser.parse_args()
    method = args.method
    enctype = args.enctype
    url = args.url
    fields = args.fields
    output = args.output
    try:
        sitio = requests.get(url)
        if sitio.status_code == 200:
            print(colored("""
-------------------
    URL Valida.
-------------------""","green"))
        if sitio.status_code == 204:
            print(colored("""
-----------------------
    No hay contenido
-----------------------""","yellow"))
        if sitio.status_code == 302:
            print(colored("""
--------------------------------------
    El directorio ha sido movido.
--------------------------------------""","yellow"))
        if sitio.status_code == 400:
            print(colored("""
-------------------
    URL invalida
-------------------""","red"))
        if sitio.status_code == 403:
            print(colored("""
--------------------------------
    Directorio prohibido.
--------------------------------""","blue"))
        if sitio.status_code == 404:
            print(colored(f"""
--------------------------------
    Directorio no existe.
--------------------------------""","blue"))
        if sitio.status_code == 500:
            print(colored("""
------------------------------------            
    Error interno del servidor.
------------------------------------""","red"))
        if sitio.status_code == 501:
            print(colored("""
-----------------------------------------
    No reconoce el método del request.
-----------------------------------------""","red"))
        if sitio.status_code == 502:
            print(colored("""
-------------------
    Bad Gateway.
-------------------""","red"))
        if sitio.status_code == 503:
            print(colored("""
--------------------------------
    Servicio no disponible.
--------------------------------""","yellow"))
        if sitio.status_code == 504:
            print(colored("""
-----------------------
    Gateway Timeout.
-----------------------""","blue"))

        contenido = bs4.BeautifulSoup("<html></html>", "html.parser")
        html = contenido.find("html")
        form_tag = contenido.new_tag("form", enctype=enctype, action=url, method=method)
        html.append(form_tag)
        fields = ast.literal_eval(fields)

        for campo in fields:
            input_tag = contenido.new_tag("input", type=campo['type'])
            input_tag['name'] = campo['name']
            form_tag.append(input_tag)

        submit_tag = contenido.new_tag("input", type="submit", value="submit")
        form_tag.append(submit_tag)
        print(colored("-------------------------------------------","white","on_yellow"))
        print(colored("                 HTML                      ","white","on_yellow"))
        print(colored("-------------------------------------------","white","on_yellow"))
        print(contenido.prettify())

        if output is not None:
            texto = open(output,"w")
            texto.write(str(contenido.prettify()))
            texto.close()
            
            if os.path.exists(str(output)):
                print(f"Archivo creado correctamente como '{output}'.")
            else:
                print("Hubo un error al crear el archivo.")

    except requests.exceptions.ConnectionError:
        print(colored("""
------------------------------------------------------------------------
    No se reconoce el host indicado, verifique su conexion a internet.
------------------------------------------------------------------------""","red"))
        contenido = bs4.BeautifulSoup("<html></html>", "html.parser")
        html = contenido.find("html")
        form_tag = contenido.new_tag("form", enctype=enctype, action=url, method=method)
        html.append(form_tag)
        fields = ast.literal_eval(fields)

        for campo in fields:
            input_tag = contenido.new_tag("input", type=campo['type'])
            input_tag['name'] = campo['name']
            form_tag.append(input_tag)

        submit_tag = contenido.new_tag("input", type="submit", value="submit")
        form_tag.append(submit_tag)
        print(colored("-------------------------------------------","white","on_yellow"))
        print(colored("                 HTML                      ","white","on_yellow"))
        print(colored("-------------------------------------------","white","on_yellow"))
        print(contenido.prettify())

        if output is not None:
            texto = open(output,"w")
            texto.write(str(contenido.prettify()))
            texto.close()
            
            if os.path.exists(str(output)):
                print(f"Archivo creado correctamente como '{output}'.")
            else:
                print("Hubo un error al crear el archivo.")

    except requests.exceptions.MissingSchema:
        parser.print_help()

def logo():
    system("clear")
    logo1 = colored(
"""
  ____ ____  ____  _____   _____ _____ ____ _____ 
 / ___/ ___||  _ \|  ___| |_   _| ____/ ___|_   _|
| |   \___ \| |_) | |_      | | |  _| \___ \ | |  
| |___ ___) |  _ <|  _|     | | | |___ ___) || |  
 \____|____/|_| \_\_|       |_| |_____|____/ |_|  
                                    Cyber Phantom            

""", "red")
    print(logo1)

if __name__ == "__main__":
    logo()
    csfrpoc()

