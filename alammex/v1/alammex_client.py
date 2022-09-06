from ..utils import fetch_api_data
from .alammex_quote import AlammexQuote
from .alammex_transaction_group import AlammexTransactionGroup

class AlammexClient:
    def __init__(self, algodUri: str, algodToken, algodPort: str, chain: str, apiKey: str):
        self.algodUri = algodUri
        self.algodToken = algodToken
        self.algoPort = algodPort
        self.chain = chain
        self.apiKey = apiKey

    def get_fixed_input_swap_quote(self, fromASAId: int, toASAId: int, amount: int, disabledProtocols: list = [], maxGroupSize: int = 16):
        apiResponse = fetch_api_data(self.chain, 'fetchQuote', {
            'algodUri': self.algodUri,
            'algodToken': self.algodToken,
            'algodPort': self.algoPort,
            'amount': amount,
            'type': 'fixed-input',
            'fromASAID': fromASAId,
            'toASAID': toASAId,
            'apiKey': self.apiKey,
            'disabledProtocols': disabledProtocols,
            'maxGroupSize': maxGroupSize
        })
        return AlammexQuote.from_api_response(apiResponse)

    def get_fixed_output_swap_quote(self, fromASAId: int, toASAId: int, amount: int, disabledProtocols: list = [], maxGroupSize: int = 16):
        apiResponse = fetch_api_data(self.chain, 'fetchQuote', {
            'algodUri': self.algodUri,
            'algodToken': self.algodToken,
            'algodPort': self.algoPort,
            'amount': amount,
            'type': 'fixed-output',
            'fromASAID': fromASAId,
            'toASAID': toASAId,
            'apiKey': self.apiKey,
            'disabledProtocols': disabledProtocols,
            'maxGroupSize': maxGroupSize
        })
        return AlammexQuote.from_api_response(apiResponse)

    def get_swap_quote_transactions(self, address: str, quote: AlammexQuote, slippage, referrer):
        apiResponse = fetch_api_data(self.chain, 'executeSwapTxns', {
            'algodUri': self.algodUri,
            'algodToken': self.algodToken,
            'algodPort': self.algoPort,
            'address': address,
            'txnPayloadJSON': quote.txnPayload,
            'slippage': slippage,
            'referrer': referrer,
            'apiKey': self.apiKey
        })
        return AlammexTransactionGroup.from_api_response(apiResponse)


class AlammexTestnetClient(AlammexClient):
    def __init__(self, algodUri: str, algodToken, algodPort: str, apiKey: str):
        super().__init__(algodUri, algodToken, algodPort, 'testnet', apiKey)


class AlammexMainnetClient(AlammexClient):
    def __init__(self, algodUri: str, algodToken, algodPort: str, apiKey: str):
        super().__init__(algodUri, algodToken, algodPort, 'mainnet', apiKey)

