from.models import Category

def srecipe_context_processor(request):
    context = {}
    context['categories'] =Category.objects.all()
    return context
