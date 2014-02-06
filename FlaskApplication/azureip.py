__author__ = '@codingoutloud'
import urllib2
from xml.dom.minidom import parseString
import netaddr
# import iptools  # http://code.google.com/p/python-iptools/
# import datetime

# start at http://msdn.microsoft.com/en-us/library/windowsazure/dn175718.aspx to find the below URL
# then follow to http://www.microsoft.com/en-us/download/confirmation.aspx?id=41653 to find the below (actual) URL
default_azure_region_xml_url = \
    'http://download.microsoft.com/download/0/1/8/018E208D-54F8-44CD-AA26-CD7BC9524A8C/PublicIPsByRegion_.xml'


class AzureIp:
    """
    Processes Azure Region IP Address data, including loading from the web and supports queries on the loaded data.
    """
    def __init__(self, region_xml_url=default_azure_region_xml_url):
        self.region_xml_url = region_xml_url
        self.regions = self.load_region_ip_ranges_dom()  # leave 'regions' in XML DOM format

    def load_region_ip_ranges_dom(self):
        ip_xml = urllib2.urlopen(self.region_xml_url).read()
        ip_xml_doc = parseString(ip_xml)
        return ip_xml_doc.getElementsByTagName('Region')

    def find_ip(self, ip_string):
        print("Seeking '%s'" % ip_string)
        print("%d regions available" % len(self.regions))
        for r in self.regions:  # expects self.regions in XML DOM format - good enough for now
            region_name = r.attributes['Name'].value
            ip_ranges = r.getElementsByTagName('IpRange')
            print("region %s has %d ranges" % (region_name, len(ip_ranges)))
            for ipr in ip_ranges:
                cidr = ipr.attributes['Subnet'].value
                if netaddr.IPAddress(ip_string) in netaddr.IPNetwork(cidr):
                    # print("FOUND -----------------------------------------------")
                    return region_name
                # ip_address_range = iptools.IpRangeList(cidr)
                # ip_address_list = ip_address_range.ips[0]
                # first_ip = ip_address_list[0]
                # last_ip = ip_address_list[-1]
                # ip_count = len(ip_address_list)
                # print("seeking %s in %s" % (ip_string, cidr))
                # print("%s %s range goes from %s to %s (%d ip addresses)" %
                #       (region_name, cidr, first_ip, last_ip, ip_count))
        # print("None...")
        return None


