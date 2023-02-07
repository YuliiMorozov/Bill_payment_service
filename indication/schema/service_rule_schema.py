from indication import ma
from indication.models.service_rule import ServiceRule

class ServiceRuleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ServiceRule
        fields = ('id', 'tax')