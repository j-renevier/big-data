import os
import sys
import traceback
from flask import Blueprint, jsonify, current_app


from common.Response_codes import Response_codes, IResponseCode
from common.Response import Response
from usecases.version.get_version_usecase import GetVersionUsecase

api_version_blueprint = Blueprint('api_version', __name__)

@api_version_blueprint.route('/version', methods=['GET'])
def get_version():
    
    result: Response
    try: 
        result = GetVersionUsecase.execute()

        if result.error:
            raise Exception()

        return jsonify({'message': f'{result.status.message()}', 'content': result.content}), 200
    
    except Exception as error:
        message = result.status.message() if result.status else Response_codes(IResponseCode.status.ERROR, IResponseCode.layer.API, IResponseCode.context.VERSION, IResponseCode.file.GET_VERSION, IResponseCode.detail.GENERIC).message()
        error_msg = result.error if result.error else Response_codes(IResponseCode.status.ERROR, IResponseCode.layer.API, IResponseCode.context.VERSION, IResponseCode.file.GET_VERSION, IResponseCode.detail.NO_DETAIL).message()

        return jsonify({'message': f'{message}', 'content': '', 'error': f'{error_msg}'}), 500
