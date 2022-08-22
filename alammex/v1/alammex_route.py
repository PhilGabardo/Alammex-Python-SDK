from .alammex_path_element import AlammexPathElement

class AlammexRoute:

    def __init__(self, percent: int, path: list):
        self.percent = percent
        self.path = path

    @staticmethod
    def from_api_response(apiResponse):
        return AlammexRoute(
            apiResponse['percentage'],
            [AlammexPathElement.from_api_response(pathElement) for pathElement in apiResponse['path']]
        )