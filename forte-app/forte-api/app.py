from flask import Flask, jsonify, request
from infra import db_infra

from adapters import db_adapters
from repository import db_repository
from usecases import txns_usercase


app = Flask(__name__)


@app.route("/")
def hello():
    response = jsonify({
        "statusCode": 200,
        "msg": "¡HELLO FORTE!"
    })
    return response


@app.route("/transaction", methods=["POST"])
def save_transaction():

    mongo_config = db_infra.MongoConfig()
    mongodb = db_repository.MongoDb(mongo_config)

    # TODO ADD REQUEST VALIDATION
    json_request = request.get_json()

    tnxs_usecase = txns_usercase.TnxsUsecase(mongodb)
    txn_id = tnxs_usecase.save_transaction(json_request)

    if not txn_id:
        return jsonify({
            "statusCode": 409,
            "_id": txn_id
        })

    return jsonify({
        "statusCode": 201,
        "_id": txn_id
    })


@app.route("/transaction/<transaction_id>", methods=["PUT"])
def update_transaction(transaction_id):
    
    mongo_config = db_infra.MongoConfig()
    mongodb = db_repository.MongoDb(mongo_config)

    # TODO ADD REQUEST VALIDATION
    json_request = request.get_json()

    tnxs_usecase = txns_usercase.TnxsUsecase(mongodb)
    updated = tnxs_usecase.update_transaction(transaction_id, json_request)

    response = jsonify({
        "statusCode": 200,
        "updated": updated
    })

    return response


@app.route("/transaction/<transaction_id>", methods=["DELETE"])
def deactived_transaction(transaction_id):
    mongo_config = db_infra.MongoConfig()
    mongodb = db_repository.MongoDb(mongo_config)

    tnxs_usecase = txns_usercase.TnxsUsecase(mongodb)
    deactivated = tnxs_usecase.deactived_transaction(transaction_id)

    response = jsonify({
        "statusCode": 200,
        "deactivated": deactivated
    })

    return response


@app.route("/transactions/<customer_id>", methods=["GET"])
def get_transactions_by_customer_id(customer_id):

    mongo_config = db_infra.MongoConfig()
    mongodb = db_repository.MongoDb(mongo_config)

    tnxs_usecase = txns_usercase.TnxsUsecase(mongodb)
    transactions = tnxs_usecase.get_transactions_by_customer_id(customer_id)

    response = jsonify({
        "statusCode": 200,
        "transactions": transactions
    })

    return response


@app.route("/transactions", methods=["GET"])
def list_transactions():

    mongo_config = db_infra.MongoConfig()
    mongodb = db_repository.MongoDb(mongo_config)

    tnxs_usecase = txns_usercase.TnxsUsecase(mongodb)
    transactions = tnxs_usecase.list_transactions()

    response = jsonify({
        "statusCode": 200,
        "transactions": transactions
    })

    return response


"""
curl -X GET http://localhost:5000/transactions
curl -X GET http://localhost:5000/transactions/bd7b69fa-9207-4996-91cd-b7eec3fce21a

curl  -X POST http://localhost:5000/transaction -H "Content-Type: application/json" --DATA '{"transaction_id": "bd7b69fa-9207-4996-91cd-b7eec3fce21z", "customer_id": "bd7b69fa-9207-4996-91cd-b7eec3fce21z", "amount": 50.11,"category": "cz", "type": "income", "deactivated": false, "date": "2025-01-16T18:28:55Z"}'

curl  -X PUT http://localhost:5000/transaction/bd7b69fa-9207-4996-91cd-b7eec3fce21b -H "Content-Type: application/json" --DATA '{"amount":11.11,"category":"c3"}'
curl  -X DELETE http://localhost:5000/transaction/bd7b69fa-9207-4996-91cd-b7eec3fce21b -H "Content-Type: application/json"

"""