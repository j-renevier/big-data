from abc import ABC
from enum import Enum

class EResponseStatus(Enum):
    SUCCESS = 'SUCCESS'
    ERROR = 'ERROR'

class EResponseLayer (Enum):
    USECASE = 'USECASE'
    API = 'API'

class EResponseContext (Enum):
    VERSION = 'VERSION'
    FILE = 'FILE'
    
class EResponseFile (Enum):
    GET_VERSION = 'GET_VERSION'
    GET_FILE = 'GET_FILE'

class EResponseDetail(Enum):
    GENERIC = 'GENERIC'
    NO_DETAIL= 'NO_DETAIL'
    NOT_FOUND_OR_NULL= 'NOT_FOUND_OR_NULL'

class IResponseCode(ABC):
    status = EResponseStatus
    layer = EResponseLayer
    context = EResponseContext
    file = EResponseFile
    detail = EResponseDetail


class Response_codes:
    
    def __init__(self, 
                 response_status: IResponseCode.status, 
                 response_layer: IResponseCode.layer = None, 
                 response_context: IResponseCode.context = None, 
                 response_file: IResponseCode.file = None, 
                 response_detail: IResponseCode.detail = None):
        self.response_status = response_status
        self.response_layer = response_layer
        self.response_context = response_context
        self.response_file = response_file
        self.response_detail = response_detail

    def message(self): 
        # Ajout de vérification pour les arguments optionnels
        components = [self.response_status.value]
        
        if self.response_layer:
            components.append(self.response_layer.value)
        
        if self.response_context:
            components.append(self.response_context.value)
        
        if self.response_file:
            components.append(self.response_file.value)
        
        if self.response_detail:
            components.append(self.response_detail.value)
        
        return "_".join(components)
        

