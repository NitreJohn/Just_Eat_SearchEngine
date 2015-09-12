from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
text = """<form action="/hw/formsubmit/" method="post">
     <input type="text" name="your_name" /><br />
    <select multiple="multiple" name="bands">
        <option value='Beatles'>The Beatles</option>
        <option value='Who'>The Who</option>
        <option value='Zombies'>The Zombies</option>
    </select>  <br/>    <input type="submit" />  </form>  <br/>
    <input type="text" value="%s ; %s" width="10"/>
"""


@csrf_exempt
def index(request):
    temp = "You haven't chose a band."
    print type(temp)
    if(len(request.POST.getlist('bands')) > 0):
        return HttpResponse(text % (request.POST['your_name'], request.POST.getlist('bands')[0]))
    elif(request.POST['your_name'] == ""):
        return HttpResponse(text % ("You haven't chose your name.", temp))
    else:
        return HttpResponse(text % (request.POST['your_name'], temp))
