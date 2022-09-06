from rest_framework import pagination

class ShowPagination(pagination.PageNumberPagination):
    page_size = 3
    page_query_param = 'p'
    
    # give options for users
    page_size_query_param = 'size'  # to override the default value
    max_page_size = 10
    last_page_strings = 'end'
    
    
class ShowLOPagination(pagination.LimitOffsetPagination):
    default_limit = 5
    max_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'start'
    
    
class ShowCPagination(pagination.CursorPagination):
    page_size = 5
    cursor_query_param = 'record'
    ordering = 'created'