from  alibabacloud_alidns20150109.models import UpdateDomainRecordRequest
from  alibabacloud_alidns20150109.models import DescribeDomainRecordsRequest
from alibabacloud_alidns20150109.client import Client as AlidnsClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_openapi import models as open_api_models
from ipaddress import ip_address



class AliyunAPI:
    def __init__(self, config, logger):
        self.config=config
        self.logger=logger

        self.access_key_id = config['aliyun_account']['access_key_id']
        self.access_key_secret = config['aliyun_account']['access_key_secret']

        self.domain_name = config['domain']['name']
        self.domain_rr = config['domain']['rr']
        self.domain_type= config['domain']['type']

        self.client=self.get_client()

        self.domain_record_id = self.get_domain_record_id()

    def get_client(self):
        config = open_api_models.Config(
            access_key_id=self.access_key_id,
            access_key_secret=self.access_key_secret
        )
        return AlidnsClient(config)

    def get_domain_record_id(self):
        try:
            runtime = util_models.RuntimeOptions()
            response=self.client.describe_domain_records_with_options(
                DescribeDomainRecordsRequest(domain_name=self.domain_name,rrkey_word=self.domain_rr  ) ,runtime)
            record_id = response.body.domain_records.record[0].record_id
            return  record_id
        except Exception as e:
            self.logger.error(f"Failed to get domain record ID: {e}")
            raise

    def get_domain_record_value(self):
        try:
            runtime=util_models.RuntimeOptions()
            response=self.client.describe_domain_records_with_options(
                DescribeDomainRecordsRequest(domain_name=self.domain_name,rrkey_word=self.domain_rr),runtime)
            record_value=response.body.domain_records.record[0].value.strip()
            self.logger.info(f"Record_value:{record_value}")
            try:
                current_ip=ip_address(record_value)
                self.logger.success(f"Current IP address: {current_ip}")
                return current_ip
            except ValueError:
                self.logger.error(f"Invalid IP address: {record_value}")
        except Exception as e:
            self.logger.error(f"Failed to get domain record Value:{e}")
            raise

    def update_ddns(self, ip):
        try:
            request=UpdateDomainRecordRequest()
            request.record_id=self.domain_record_id
            request.rr=self.domain_rr
            request.type=self.domain_type
            request.value=ip
            self.client.update_domain_record(request)
            self.logger.success(f"DDNS updated to {ip}")
        except Exception as e:
            self.logger.error(f"Failed to update DDNS: {e}")
            raise