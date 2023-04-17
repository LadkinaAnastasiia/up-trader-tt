from django import template

from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu_templates.html', takes_context=True)
def draw_menu(context, menu_name):
    try:
        menu = MenuItem.objects.get(name=menu_name, id_parent=None)
    except MenuItem.DoesNotExist:
        menu = None
    local_context = {'menu_item': menu}
    requested_url = context['request'].path

    local_context['active_url'] = requested_url

    return local_context


@register.inclusion_tag('menu/menu_templates.html', takes_context=True)
def draw_menu_item_children(context, child):
    local_context = {'menu_item': child}
    if 'active_url' in context:
        local_context['active_url'] = context['active_url']
    return local_context
