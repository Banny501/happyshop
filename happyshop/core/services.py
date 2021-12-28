

class DataMixin:
    @staticmethod
    def get_user_context(**kwargs):
        context = kwargs
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        if 'menu_selected' not in context:
            context['menu_selected'] = None
        return context
