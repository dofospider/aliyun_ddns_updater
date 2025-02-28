import time
import yaml
from ipaddress import ip_address

from logger import Logger
from public_ip_fecther import FetchPublicIP
from aliyun_api import AliyunAPI

# Configure loguru

def load_config(logger):
    with open('config.yaml', 'r') as file:
        return yaml.safe_load(file)



def main():
    logger=Logger()
    config = load_config(logger)
    fetch_public_ip=FetchPublicIP(config,logger)


    aliyun_api = AliyunAPI(config, logger)
    # record_id = aliyun_api.get_domain_record_id()



    while True:
        try:
            current_ip=aliyun_api.get_domain_record_value()
            new_ip = fetch_public_ip.run()

            if ip_address(new_ip) != ip_address(current_ip):
                aliyun_api.update_ddns(new_ip)
                logger.success(f"IP updated to {new_ip}")
            else:
                logger.success(f"IP is still {new_ip}")
            time.sleep(300)  # Check every 5 minutes
        except Exception as e:
            logger.error(f"Error: {e}")
            time.sleep(60)  # Wait 1 minute before retrying

if __name__ == "__main__":
    main()