"""schema

Response Schema

PROJECT: BaoAI Backend
AUTHOR: henry <703264459@qq.com>
WEBSITE: http://www.baoai.co
COPYRIGHT: Copyright © 2016-2020 广州源宝网络有限公司 Guangzhou Yuanbao Network Co., Ltd. ( http://www.ybao.org )
LICENSE: Apache-2.0
"""

from flask_restplus_patched import ModelSchema
from flask_marshmallow import base_fields
from .model import *

class RolesResourcesSchema(ModelSchema):
    class Meta:
        model = RolesResources

