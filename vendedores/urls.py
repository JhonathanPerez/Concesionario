from django.conf.urls import url
from vendedores.views import ListadoVehiculos
from vendedores.views import AdicionaVehiculo
from vendedores.views import VisualizaVehiculo
from vendedores.views import BorraVehiculo
from vendedores.views import ModificaVehiculo
from vendedores.views import ModificaPerfil

urlpatterns = [
    url(r'^listar-vehiculos/', ListadoVehiculos.as_view(), name='listar_vehiculos'),
    url(r'^adicionar-vehiculos/', AdicionaVehiculo.as_view(), name='adicionar_vehiculo'),
    url(r'^visualizar-vehiculos/(?P<id_vehiculo>\w+)', VisualizaVehiculo.as_view(), name='visualizar_vehiculo'),
    url(r'^borrar-vehiculos/(?P<id_vehiculo>\w+)', BorraVehiculo.as_view(), name='borrar_vehiculo'),
    url(r'^modificar-vehiculos/(?P<id_vehiculo>\w+)', ModificaVehiculo.as_view(), name='modificar_vehiculo'),
    url(r'^modificar-perfil/', ModificaPerfil.as_view(), name='modificar_perfil'),
]
