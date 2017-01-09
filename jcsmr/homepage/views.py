from django.shortcuts import render
from .models import HomePageImage, HomePageSlider, HomePageText, ContactPageImage
from contacts.forms import AddContactForm
from contacts.models import Contact
# Create your views here.
def index(request):
    data = HomePageImage.objects.all()
    data1 = HomePageSlider.objects.all()
    data2 = HomePageText.objects.all()

    # validamos el query y si no damos valores a las variables
    if data:
        # Sacamos el nombre de cada imagen de portada
        for obj in data:
            nombre = '%s' %(obj.main_icon.name)
            nombre1 = '%s' %(obj.parallax_image1.name)
            nombre2 = '%s' %(obj.parallax_image2.name)
            nombre3 = '%s' %(obj.favicon.name)
    else:
        nombre = '%s' %('')
        nombre1 = '%s' %('')
        nombre2 = '%s' %('')
        nombre3 = '%s' %('')
    # validamos el query y si no damos valores a las variables
    if data2:
        # Sacamos el texto que va a llevar la pagina
        for obj1 in data2:
            texto = '%s' %(obj1.title)
            texto1 = '%s' %(obj1.subtitle)
            texto2 = '%s' %(obj1.blank_panel_text)
            texto3 = '%s' %(obj1.blank_panel_text_2)
            texto4 = '%s' %(obj1.blank_panel_title)
            texto5 = '%s' %(obj1.blank_panel_title2)
            color = '%s' %(obj1.color_title)
            color1 = '%s' %(obj1.color_small_tag)
    else:
        texto = '%s' %('Titulo')
        texto1 = '%s' %('este es un subtitulo')
        texto2 = '%s' %('Titulo')
        texto3 = '%s' %('este es un subtitulo')
        color = '%s' %('lighten-5')
        color1 = '%s' %('lighten-5')
        texto4 = '%s' %('Titulo blank section')
        texto5 = '%s' %('Titulo blank section')
    context = {
        'img1' : nombre,
        'img2' : nombre1,
        'img3' : nombre2,
        'img4' : nombre3,
        'mainTitle' : texto,
        'mainDescription' : texto1,
        'blanktextDescription1' : texto2,
        'blanktextDescription2' : texto3,
        'blanktextTitle1' : texto4,
        'blanktextTitle2' : texto5,
        'data' : data1,
        'colorMaintitle' : color,
        'colorMainSubtitle' : color1,
    }
    return render(request, 'ini.html', context)

def contact(request):
    data = HomePageImage.objects.all()
    data2 = ContactPageImage.objects.all()
    # validamos el query y si no damos valores a las variables
    if data:
        # Sacamos el nombre de cada imagen de portada
        for obj in data:
            nombre = '%s' %(obj.main_icon.name)
            nombre1 = '%s' %(obj.parallax_image1.name)
            nombre3 = '%s' %(obj.favicon.name)
    else:
        nombre = '%s' %('')
        nombre1 = '%s' %('')
        nombre3 = '%s' %('')
    print ( data.__dict__ )
    # validamos el query y si no damos valores a las variables
    if data2:
        # Sacamos el nombre de cada imagen de portada
        for obj in data2:
            imageContact = '%s' %(obj.contact_image.name)
            textContact1 = '%s' %(obj.text1)
            textContact2 = '%s' %(obj.text2)
    else:
        imageContact = '%s' %('')
        textContact1 = '%s' %('')
        textContact2 = '%s' %('')
    context = {
        'img1' : nombre,
        'img2' : nombre1,
        'img4' : nombre3,
        'imageContact' : imageContact,
        'textContact1' : textContact1,
        'textContact2' : textContact2,
    }
    if request.method == 'POST':
        paquete = {
            'first_name' : request.POST.get('first_name'),
            'phone' : request.POST.get('phone'),
            'email' : request.POST.get('email'),
            'message' : request.POST.get('message')
            }
        form = AddContactForm(paquete)
        if form.is_valid():
            form.save()
    return render(request, 'contact.html', context)
