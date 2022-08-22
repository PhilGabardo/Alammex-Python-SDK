from .alammex_transaction import AlammexTransaction

class AlammexTransactionGroup:

    def __init__(self, txns: list):
        self.txns = txns

    @staticmethod
    def from_api_response(apiResponse):
        return AlammexTransactionGroup([AlammexTransaction.from_api_response(txn) for txn in apiResponse['txns']])