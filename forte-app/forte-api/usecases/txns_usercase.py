from adapters import db_adapters

class TnxsUsecase:

    def __init__(self, db):
        self.db = db

    def save_transaction(self, txn):
        txn_id = db_adapters.create_transaction(self.db, txn)
        return txn_id

    def update_transaction(self, transaction_id, data):
        search_by = {"transaction_id": transaction_id}

        updated = db_adapters.update_transaction(self.db, search_by, data)
        return updated

    def get_transactions_by_customer_id(self, customer_id):
        search_by = {"customer_id": customer_id}

        txns = db_adapters.get_transactions(self.db, search_by)
        return txns

    def list_transactions(self):
        txn = db_adapters.get_transactions(self.db, {})
        return txn

    def deactived_transaction(self, transaction_id):
        deactived = db_adapters.deactived_transaction(self.db, transaction_id)
        return deactived
