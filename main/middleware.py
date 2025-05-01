from .utils import *
import logging

logger = logging.getLogger(__name__)

class LogIPMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = get_client_ip(request)
        logger.info(f"Visitor IP: {ip}")
        response = self.get_response(request)
        return response