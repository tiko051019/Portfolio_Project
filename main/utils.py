from django.http import JsonResponse
import requests

def get_client_ipv4(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_client_ipv4_divice(request):
    user_agent_str = request.META.get('HTTP_USER_AGENT')
    
    return user_agent_str

#-------------------------------geolocation-----------------------------------

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        # Client may be behind proxy or load balancer
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_geo_location(ip):
    try:
        response = requests.get(f'https://ipinfo.io/{ip}/json')
        return response.json()
    except:
        return {}

def show_ip(request):
    ip = get_client_ip(request)
    geo_data = get_geo_location(ip)
    geo_data['ip'] = ip
    return JsonResponse(geo_data)




