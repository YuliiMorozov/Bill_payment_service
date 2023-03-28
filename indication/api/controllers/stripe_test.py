from flask import jsonify
from indication.api.controllers import api
from indication import stripe_keys


@api.route('/stripe_test', methods=['GET'])
def stripe_test():   
    stripe_config = {"publicKey": stripe_keys["publishable_key"]}     
    return jsonify (stripe_config)
    # '''
    # <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.0/css/bulma.min.css">
    # <button class="button is-primary" id="submitBtn">Purchase!</button>
    # <script defer src="https://use.fontawesome.com/releases/v5.14.0/js/all.js"></script>
    # <script>console.log("Sanity check!");</script>

    # '''