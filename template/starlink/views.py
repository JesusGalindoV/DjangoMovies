from django.shortcuts import redirect, render
from datetime import date, datetime
import datetime

# Create your views here.
pelicula= [{"titulo": "Deadpool", "year":2016 , "descripcion" : "Wade Wilson, tras ser sometido a un cruel experimento científico, adquiere poderes especiales que le convierten en Deadpool Armado con sus nuevas habilidades y un retorcido sentido del humor tratará de dar caza al hombre que casi destruye su vida" },
{"titulo": "Spiderman", "year":2011 , "descripcion" : "Tras descubrirse la identidad secreta de Peter Parker como Spider-Man, la vida del joven se vuelve una locura. Peter decide pedirle ayuda al Doctor Extraño para recuperar su vida. Pero algo sale mal y provoca una fractura en el multiverso."}]

modificacionPelicula=[{"titulo": "mi pobre angelito", "year":1992 , "descripcion" : "Morro que se queda en su casa"}]
def start(request):
    return render(request, 'start.html',{"valor":"start","pelicula": pelicula})



#agregar
def agregar(request):
    if request.method == "POST":
        pelicula.append({"titulo":request.POST["titulo"],
        "year":int(request.POST["year"]),
        "descripcion":request.POST["descripcion"]})
        return redirect('start')
    return render (request,"agregar.html",{})

#Borrar
def borrar(request,id):
    pelicula.pop(id)
    return render(request,"start.html",{"pelicula":pelicula})

#modificar
def modificar(request,id):
    if request.method == "POST":
        pelicula[id]={"titulo":request.POST["titulo"],
        "year":int(request.POST["year"]),
        "descripcion":request.POST["descripcion"],
    }
    return render(request,"modificar.html",
    {"titulo":pelicula[id]["titulo"],
    "descripcion":pelicula[id]["descripcion"],
    "year":pelicula[id]["year"], "id":id})

def index(request):
    ahora = datetime.datetime.now()
    return render(request,"peliculas.html",{'ahora':ahora})