# aliyun_ddns_updater
使用pythonAPI的阿里云ddns更新器，方便nas更新活动外网地址

思维定势影响，以前总是跑到nas后台设置一堆定时任务，现在通过docker镜像，一键部署，自动启动，妈妈再也不担心我的nas连不上网了。


# Aliyun_API依赖
from  alibabacloud_alidns20150109.models import UpdateDomainRecordRequest

from  alibabacloud_alidns20150109.models import DescribeDomainRecordsRequest

from alibabacloud_alidns20150109.client import Client as AlidnsClient

from alibabacloud_tea_util import models as util_models

from alibabacloud_tea_openapi import models as open_api_models

