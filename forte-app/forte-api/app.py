from flask import Flask, jsonify, request

from config import db_config
from adapters import db_adapters
from repository import db_repository
from usecases import txns_usercase


app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    response = jsonify({
        "statusCode": 200,
        "msg": "¡Hello FORTE!"
    })
    return response


@app.route("/transaction", methods=["POST"])
def save_transaction():

    mongo_config = db_config.MongoConfig()
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
    
    mongo_config = db_config.MongoConfig()
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
    mongo_config = db_config.MongoConfig()
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

    mongo_config = db_config.MongoConfig()
    mongodb = db_repository.MongoDb(mongo_config)

    tnxs_usecase = txns_usercase.TnxsUsecase(mongodb)
    transactions = tnxs_usecase.get_transactions_by_customer_id(customer_id)

    response = jsonify({
        "statusCode": 200,
        "transactions": transactions
    })

    return response


@app.route("/transactions", methods=["GET"])
def get_all_transactions():

    mongo_config = db_config.MongoConfig()
    mongodb = db_repository.MongoDb(mongo_config)

    tnxs_usecase = txns_usercase.TnxsUsecase(mongodb)
    tnxs = tnxs_usecase.get_all_transactions()

    response = jsonify({
        "statusCode": 200,
        "transactions": tnxs
    })

    return response



@app.route("/transactions/resume", methods=["GET"])
def transactions_resume():

    mongo_config = db_config.MongoConfig()
    mongodb = db_repository.MongoDb(mongo_config)

    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")

    tnxs_usecase = txns_usercase.TnxsUsecase(mongodb)
    resume = tnxs_usecase.get_transactions_resume(start_date, end_date)

    response = jsonify({
        "statusCode": 200,
        "transactionsResume": resume
    })

    return response


@app.route("/transactions/xlsx", methods=["GET"])
def transactions_download_xlsx():

    # TODO ADD REQUEST VALIDATION
    json_request = request.get_json()

    resume_by_category = json_request["transactionsResume"]["by_category"]
    txns_by_customer = json_request["transactionsResume"]["by_customer"]

    tnxs_resume_xlsx = txns_usercase.TnxsResumeXLSX()
    xlsx_file = tnxs_resume_xlsx.get_file(resume_by_category, txns_by_customer)

    return xlsx_file


@app.route("/transactions/xlsx", methods=["POST"])
def transactions_upload_xlsx():

    if 'file' not in request.files:
        return jsonify({
            "statusCode": 400
        })
    
    xlsx_file = request.files['file']

    tnxs_resume_xlsx = txns_usercase.TnxsResumeXLSX()
    presigned_url = tnxs_resume_xlsx.upload_file(xlsx_file, request.mimetype)

    response = jsonify({
        "statusCode": 200,
        "presigned_url": presigned_url
    })

    return response
