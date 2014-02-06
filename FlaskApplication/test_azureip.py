__author__ = '@codingoutloud'

import datetime
from azureip import AzureIp

def test(test_ip, azure_ip):
    test_region = azure_ip.find_ip(test_ip)
    if test_region is None:
        print("'%s' not found in any region" % test_ip)
    else:
        print("ip (%s) is in region (%s)" % (test_ip, test_region))

print("Begin")
print(datetime.datetime.now())

azure_ip = AzureIp()
print("AzureIp created")
print(datetime.datetime.now())

test_ip = "137.116.184.0"  # should be in uswest
test(test_ip, azure_ip)
print(datetime.datetime.now())
test_ip = "1.1.1.1"  # will not be found
test(test_ip, azure_ip)
print(datetime.datetime.now())
test_ip = "1.1.1.1"  # will not be found
test(test_ip, azure_ip)

print(datetime.datetime.now())
test_ip = "137.116.184.0"  # should be in uswest
test(test_ip, azure_ip)

print(datetime.datetime.now())
print("End")


