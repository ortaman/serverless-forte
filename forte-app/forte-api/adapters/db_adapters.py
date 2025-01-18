from datetime import datetime, timezone
from bson.decimal128 import Decimal128


def format_output_txns(transaction):
    
    transaction['_id'] = str(transaction['_id'])
    transaction['amount'] = "{:.2f}".format(transaction['amount'].to_decimal())
    transaction['date'] = transaction['date'].isoformat()

    return transaction


def create_transaction(mongodb, data):

    data["amount"] = Decimal128(str(data["amount"]))
    data["date"] = datetime.now(timezone.utc)
        
    mongodb.set_collection("transactions")
    txn_id = mongodb.insert(data)
    
    return str(txn_id) if txn_id else txn_id


def get_transactions(mongodb, filter_by):
    txns = []

    mongodb.set_collection("transactions")
    transactions = mongodb.fetch_all(filter_by)

    for transaction in transactions:
        transaction = format_output_txns(transaction)
        txns.append(transaction)
    
    return txns


def update_transaction(mongodb, filter_by, data):
    mongodb.set_collection("transactions")

    transaction = mongodb.fetch_one(filter_by)

    if not transaction or transaction["deactivated"]:
        return False

    if data.get("amount"):
        data["amount"] = Decimal128(str(data["amount"]))

    modified = mongodb.update_one(filter_by, data).raw_result["nModified"]

    return True if modified else False


def deactived_transaction(mongodb, transaction_id):
    search_by = {"transaction_id": transaction_id}
    data = {"deactivated": True}

    updated = update_transaction(mongodb, search_by, data)
    return updated
