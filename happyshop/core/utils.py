
menu = [
    {'title': "Shop", 'url_name': 'shop'},
    {'title': "About", 'url_name': 'about'},
    {'title': "Contact", 'url_name': 'contact'},
]


class DataMixin:
    @staticmethod
    def get_user_context(**kwargs):
        context = kwargs
        context['menu'] = menu
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        if 'menu_selected' not in context:
            context['menu_selected'] = None
        if 'card_list' not in context:
            context['card_list'] = []
        return context
