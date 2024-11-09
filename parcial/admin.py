from django.contrib import admin
from .models import comensal
from .models import menu
from .models import pedido
from .models import mesero
from .models import entrega
from .models import cocinero
from .models import prerara
from .models import comida
from .models import contiene
from .models import ingredientes
from .models import inventario
# Register your models here.
admin.site.register(comensal)
admin.site.register(menu)
admin.site.register(pedido)
admin.site.register(mesero)
admin.site.register(entrega)
admin.site.register(cocinero)
admin.site.register(prerara)
admin.site.register(comida)
admin.site.register(contiene)
admin.site.register(ingredientes)
admin.site.register(inventario)
