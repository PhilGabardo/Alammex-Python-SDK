class AlammexTransaction:

    def __init__(self, data: str, group: str, logicSigBlob):
        self.data = data
        self.group = group
        self.logicSigBlob = logicSigBlob

    @staticmethod
    def from_api_response(apiResponse):
        return AlammexTransaction(
            apiResponse['data'],
            apiResponse['group'],
            bytearray(apiResponse['logicSigBlob'].values()) if apiResponse['logicSigBlob'] else False
        )