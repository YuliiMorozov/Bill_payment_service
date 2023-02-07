from indication import ma
from indication.models import TypeService

class TypeServiceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TypeService
        fields = ('id', 'name_service')