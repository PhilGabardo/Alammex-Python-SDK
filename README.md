# Alammex-Python-SDK
Alammex Python SDK for fetching
- Alammex quote for a swap
- the transaction group to execute a given Alammex quote

### Installation

Run: `pip install git+https://github.com/PhilGabardo/Alammex-Python-SDK`

## Fetch Alammex Quote

To fetch an Alammex quote, initialize the client and use:
- `get_fixed_input_swap_quote` for a fixed input swap
- `get_fixed_output_swap_quote` for a fixed output swap


Example (for fixed input):

```
from alammex.v1.alammex_client import AlammexMainnetClient
import algosdk
import msgpack

algodUri = <INSERT URI>
algodToken = <INSERT TOKEN>
algodPort = ''
apiKey = ''
inputAsset = 0 # ALGO
outputAsset = 31566704 # USDC
amount = 1000000 # amount in base units. This would equate to 1 ALGO (since ALGO has 6 decimals)

client = AlammexMainnetClient(algodUri, algodToken, algodPort, apiKey)
quote = client.get_fixed_input_swap_quote(0, 10458941, 1000000)
```

## Fetch Transaction Group for Executing Alammex Quote

To fetch the transaction group for executing an Alammex quote, 
use `get_swap_quote_transactions`.

Example (using quote from example above):

```
...

swapperAddress = 'DWQXOZMGDA6QZRSPER6O4AMTO3BQ6CEJMFO25EWRRBK72RJO54GLDCGK4E'
swapperMnemonic = 'bottom stone elegant just symbol bunker review curve laugh burden jewel pepper replace north tornado alert relief wrist better property spider picture insect abandon tuna'
referrer = '' # referrer address, for getting 50% of commission fees (see https://docs.alammex.com/developers/alammex-referral-program)
slippage = 1 # slippage percent
txnGroup = client.get_swap_quote_transactions(
	swapperAddress,
	quote,
	slippage,
	referrer
)

pk = algosdk.mnemonic.to_private_key(swapperMnemonic)

signedTxns = []
for txn in txnGroup.txns:
	if txn.logicSigBlob:
		signedTxns.append(msgpack.unpackb(txn.logicSigBlob))
	else:
		txnObj = algosdk.encoding.future_msgpack_decode(txn.data)
		signedTxns.append(txnObj.sign(pk))

algod = algod.AlgodClient(algodToken['X-API-Key'], algodUri, algodToken) # assuming purestake algod

txId = algod.send_transactions(signedTxns)

print(txId)
```





