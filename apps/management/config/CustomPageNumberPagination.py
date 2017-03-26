from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    """
    Custom class configuring the REST API pagination
    """
    page_size = 100
    max_page_size = 1000
    page_query_param = "page"
    page_size_query_param = "page_size"
