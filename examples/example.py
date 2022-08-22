from algosdk.v2client import algod
import algosdk
import msgpack


from alammex.v1.alammex_client import AlammexTestnetClient

algodUri = 'https://testnet-algorand.api.purestake.io/ps2'
algodToken = {
	'X-API-Key': '<INSERT PURESTAKE API KEY>'
}
algodPort = ''
apiKey = ''


client = AlammexTestnetClient(algodUri, algodToken, algodPort, apiKey)
quote = client.get_fixed_input_swap_quote(0, 10458941, 1000000)
referrer = ''
txnGroup = client.get_swap_quote_transactions(
	'DWQXOZMGDA6QZRSPER6O4AMTO3BQ6CEJMFO25EWRRBK72RJO54GLDCGK4E',
	quote,
	1,
	''
)

pk = algosdk.mnemonic.to_private_key('bottom stone elegant just symbol bunker review curve laugh burden jewel pepper replace north tornado alert relief wrist better property spider picture insect abandon tuna')

signedTxns = []
for txn in txnGroup.txns:
	if txn.logicSigBlob:
		signedTxns.append(msgpack.unpackb(txn.logicSigBlob))
	else:
		txnObj = algosdk.encoding.future_msgpack_decode(txn.data)
		signedTxns.append(txnObj.sign(pk))

algod = algod.AlgodClient(algodToken['X-API-Key'], algodUri, algodToken)

txId = algod.send_transactions(signedTxns)

print(txId)