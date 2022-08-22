class AlammexPathElement:

    def __init__(self, name: str, inputASAId: int, outputASAId: int):
        self.name = name
        self.inputASAId = inputASAId
        self.outputASAId = outputASAId

    @staticmethod
    def from_api_response(apiResponse):
        return AlammexPathElement(apiResponse['name'], apiResponse['in']['id'], apiResponse['out']['id'])