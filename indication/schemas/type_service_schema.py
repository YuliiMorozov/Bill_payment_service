from indication import ma
from indication.models.type_service import TypeService

class TypeServiceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TypeService
        fields = ('id', 'name_service')