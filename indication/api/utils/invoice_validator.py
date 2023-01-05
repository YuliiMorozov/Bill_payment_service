from flask import jsonify, abort
# from indication.api.exceptions.invoice_exceptions import CurrentValueError
from werkzeug.exceptions import BadRequest
from flask import Response
from indication.api.exceptions.invoice_exceptions import InvalidUsage



def validate_cur_value(cur_value, prv_invoice):

    messages = []

    try:
        float(cur_value)

        if float(cur_value) < 0:
            messages.append("Error, meter readings cannot be negative")

        elif prv_invoice and float(cur_value) < float(prv_invoice.cur_value):
            messages.append("Error, counter readings cannot be less than previous readings")

    except:
        messages.append("Error, meter readings must be in numeric format")

    if messages:
        return messages