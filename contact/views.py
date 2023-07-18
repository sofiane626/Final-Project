from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404
from product.models import *
from django.core.mail import send_mail
from contact.models import *

# Create your views here.

def updateContact(request,id):
    edit = Contact.objects.get(id=id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('back_Contact')
    else:
        form = ContactForm(instance=edit)
    return render(request, 'Projet_Final/back/back_edit.html', {'form': form})

def destroy_Contact(request, id):
    destroy = Contact(id)
    destroy.delete()
    return redirect('back_Contact')

def contact_mail(request):
    cart_items = CartItem.objects.all()[:4]
    allProducts = Product.objects.all()
    contacts = Contact.objects.all()
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['EMAIL']
        message = request.POST['message']
        contact = Contact_mail(name=name, email=email, message=message)
        contact.save()
        
        # Info du mail 
        subject = 'Prise de contact'
        message = "Quelqu'un a essayée de vous contacter"
        from_email = '58880@etu.he2b.be'        
        # to_email = User.objects.filter(role=1).first() 
        to_email = 'mounir.eloudghiri@hotmail.com' 
        # Envoi du mail
        send_mail(subject, message, from_email, [to_email])
        
        return redirect('home')
    return render(request, 'Projet_Final/front/contact.html', {'contacts': contacts, 'allProducts': allProducts, "cart_items": cart_items})


def mark_as_read(request, mail_id):
    mail = get_object_or_404(Contact_mail, id=mail_id)
    mail.toggle_read()
    return redirect('mailbox')

def mailbox(request):
    contact_mails = Contact_mail.objects.all()
    return render(request, 'Projet_Final/back/back_mailbox.html', {'contact_mails': contact_mails})

def destroyContact_mail(request, id):
    destroy = Contact_mail(id)
    destroy.delete()
    return redirect('mailbox')