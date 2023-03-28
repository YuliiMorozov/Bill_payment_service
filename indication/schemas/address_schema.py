from indication import ma
from indication.models.address import Address
from indication.schemas.type_service_schema import TypeServiceSchema


class AddressSchema(ma.SQLAlchemyAutoSchema):
    type_services = ma.Nested(TypeServiceSchema, many=True)

    class Meta:
        model = Address
        fields = ('id', 'country', 'city', 'street', 'house_number', 'flat_number', 'zip_code', 'type_services')