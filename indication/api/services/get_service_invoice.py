from flask import jsonify
from indication import db
from indication.api.utils.cur_user import cur_user
from indication.models import ServiceInvoice, TypeService, Address


def get_service_invoice(address_id):

    address = (
        db.session
        .query(Address)
        .filter_by(user_id=cur_user().id, id=address_id)
        .one()
    )

    test = (
        db.session
        .query(ServiceInvoice)
        .filter_by(address_id=address_id)
        .order_by(ServiceInvoice.type_service_id.desc(), ServiceInvoice.id.desc())
        .distinct(ServiceInvoice.type_service_id)
        .all()
    )
    test_2 = ServiceInvoice.query.filter_by(address_id=address_id).order_by(ServiceInvoice.type_service_id.desc(), ServiceInvoice.id.desc()).distinct(ServiceInvoice.type_service_id).all()
    print(test_2)


    return jsonify(test_2), 200


    # test = (
    #     db.session
    #     .query(ServiceInvoice)
    #     .filter_by(address_id=address_id)
    #     .order_by(ServiceInvoice.id.desc())
    #     # .order_by(ServiceInvoice.id.desc())
    #     # .distinct(ServiceInvoice.type_service_id)

    #     # .filter_by(address_id=address_id, type_service_id="1")
    #     # .one()
    #     .subquery()
    # )

    # subquery = (
    #     db.session
    #     .query(Address)
    #     .filter(Address.user_id==cur_user().id, Address.id==address_id)
    #     # .one()
    #     .subquery()
    # )
    # # print(subquery)


    # # subquery = (
    # #     db.session
    # #     .query(ServiceInvoice.id).filter(ServiceInvoice.address_id==address_id).subquery()
    # # )
    # query = (
    #     db.session
    #     .query(ServiceInvoice)
    #     .filter(ServiceInvoice.address_id.in_(subquery))
    #     .all()
    # )
    # # print(type(test))
    # # print(testtest)


    # for i in test:
        # print(i.id)
    
    # select * from address where      user_id = current_user().id and id = address_id

    # for address in all_user_addresses:

    #     if address_id == address.id:

    #         invoices = []

    #         all_services = (
    #             db.session
    #             .query(TypeService)
    #             .all()
    #         )

    #         for service in all_services:   

    #             last_invoice = (
    #                 db.session
    #                 .query(ServiceInvoice)
    #                 .filter(ServiceInvoice.address_id == address_id)
    #                 .order_by(ServiceInvoice.id.desc())
    #                 .filter(ServiceInvoice.type_service_id == service.id)
    #                 .first()
    #             )

    #             if last_invoice:

    #                 get_info = {
    #                     "id": last_invoice.id,
    #                     "type_service_id": last_invoice.type_service_id,
    #                     "service_rule_id": last_invoice.service_rule_id,
    #                     "previous_value": last_invoice.prv_value,
    #                     "current_value": last_invoice.cur_value,
    #                     "duty": last_invoice.duty
    #                 }

    #                 invoices.append(get_info)

    #         return jsonify({"invoices": invoices}), 200

    # return jsonify("Bad request"), 400
    return jsonify(address.city)