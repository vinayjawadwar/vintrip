from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    
    """
    dest1 = Destination()
    dest1.name = 'Delhi' 
    dest1.desc = 'overflowing with modern life, colourful, cacophonous Delhi pulsates ... '
    dest1.img = 'destination_4.jpg'
    dest1.price = 29999
    dest1.offer = False

    dest2  = Destination()
    dest2.name = 'Goa' 
    dest2.desc = 'The city of  beaches & sweetened with sun, sea, sand, seafood, susegad and spirituality'
    dest2.img= 'destination_5.jpg'
    dest2.price = 19999
    dest2.offer  = True

    dest3 = Destination()
    dest3.name = 'Ladakh' 
    dest3.desc = 'The city of picturesque beauty, unique culture, exciting adventure spots.'
    dest3.img= 'destination_6.jpg'
    dest3.price = 39999
    dest3.offer = False
    
    dests = [ dest1 , dest2 , dest3]

    OR
    """

    dests = Destination.objects.all()
    return render(request,"index.html",{'dests':dests})


