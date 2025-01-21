from datetime import datetime, timezone


def format_output_txns(transaction):
    
    transaction['_id'] = str(transaction['_id'])
    transaction['amount'] = "{:.2f}".format(transaction['amount'])
    transaction['date'] = transaction['date'].isoformat()

    return transaction


def create_transaction(mongodb, data):

    data["amount"] = float(data["amount"])
    data["date"] = datetime.now(timezone.utc)
        
    txn_id = mongodb.insert(data)
    
    return str(txn_id) if txn_id else txn_id


def get_transactions(mongodb, filter_by):
    
    txns = []
    transactions = mongodb.fetch_all(filter_by)

    for transaction in transactions:
        transaction = format_output_txns(transaction)
        txns.append(transaction)
    
    return txns


def update_transaction(mongodb, transaction_id, data):

    search_by = {"transaction_id": transaction_id}
    transaction = mongodb.fetch_one(search_by)
    
    if not transaction or transaction["deactivated"]:
        return False

    if data.get("amount"):
        data["amount"] = float(data["amount"])

    modified = mongodb.update_one(search_by, data).raw_result["nModified"]

    return True if modified else False


def deactived_transaction(mongodb, transaction_id):
    data = {"deactivated": True}

    updated = update_transaction(mongodb, transaction_id, data)
    return updated


def get_transactions_by_date_range(mongodb, start_date, end_date):

    filter_by = {
        "date": {
            "$gte": datetime.strptime(start_date, "%Y-%m-%d"),
            "$lte": datetime.strptime(end_date, "%Y-%m-%d")
        }
    }

    transactions = mongodb.fetch_all(filter_by)

    return transactions
