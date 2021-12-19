from django import template

register = template.Library()

@register.filter

def show_rating(countstar):
    html = ""
    
    notcountstart = 5 - countstar#5 ulduz uzerinden oylama edirik ele bil
    
    for i in range(countstar):
        html += '<i class="fa fa-star active"></i>'
    
    for j in range(notcountstart):
        html += '<i class="fa fa-star"></i>'
    
    #bura ise butun hamsinda gorunecek
    html += f'<span class="rounded bg-warning text-dark pl-1 pr-1">5/{countstar}</span>'
    return html#return unutma burda hemise yazilmalidirki html terefine gonderilsin yoxsa islemez html terefinde
    