import requests
import random
import time

from ipaddress import ip_address

class FetchPublicIP:
    def __init__(self,config,logger):
        self.config=config
        self.logger=logger
        self.urls=self.config['get_public_ip']['urls']
        self.timeout=120

    def run(self):
        random.shuffle(self.urls)
        for url in self.urls:
            try:
                with requests.get(url,timeout=self.timeout) as response:
                    if response.status_code==200:
                        ip_stred=response.text.strip()
                        try:
                            ip=ip_address(ip_stred)
                            self.logger.success(f"Public IP response: {ip_stred} from {url}")
                            return ip
                        except ValueError:
                            self.logger.error(f"Invalid IP address: {ip_stred} from {url}" )
                            continue
            except Exception as e:
                self.logger.error(f"Failed to fetch public IP from {url}: {e}")
                continue
        self.logger.error("Failed to fetch public IP from all URLs")
        raise Exception("Failed to fetch public IP from all URLs")