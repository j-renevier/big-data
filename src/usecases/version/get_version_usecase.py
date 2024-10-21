import os

from common.Response import Response
from common.Response_codes import Response_codes, IResponseCode


class GetVersionUsecase:
    def execute()-> Response:
        try:
            version =  os.getenv('APP_VERSION')

            if not version: 
                raise Exception(Response_codes(IResponseCode.status.ERROR, IResponseCode.layer.USECASE, IResponseCode.context.VERSION, IResponseCode.file.GET_VERSION, IResponseCode.detail.NOT_FOUND_OR_NULL).message()) 
        
            response_code = Response_codes(IResponseCode.status.SUCCESS, IResponseCode.layer.USECASE, IResponseCode.context.VERSION, IResponseCode.file.GET_VERSION)

            return Response(status=response_code, content={'version': version})
        
        except Exception as exc:
            response_code = Response_codes(IResponseCode.status.ERROR, IResponseCode.layer.USECASE, IResponseCode.context.VERSION, IResponseCode.file.GET_VERSION, IResponseCode.detail.GENERIC)
            
            return Response(status=response_code, error=exc)