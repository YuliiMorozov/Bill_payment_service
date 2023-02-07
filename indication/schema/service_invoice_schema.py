from indication import ma
from indication.models.serviceinvoice import ServiceInvoice
from indication.schema.service_rule_schema import ServiceRuleSchema
from indication.schema.type_service_schema import TypeServiceSchema

class ServiceInvoiceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ServiceInvoice
        fields = ('id', 'date', 'prv_value', 'cur_value', 'paid', 'duty', 'typeservice', 'servicerule')
    typeservice = ma.Nested(TypeServiceSchema)
    servicerule = ma.Nested(ServiceRuleSchema)