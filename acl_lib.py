from genie.testbed import load
from pyats.topology import loader
from pyats import aetest
import re, logging
import pdb
from pyats.async_.exceptions import *
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class acl_common_functions():
    def configure_ip_address(device,intf,ip_address,mask):
        device.configure('''int {intf}\n no switchport\nip address {ip_address} {mask}\n no shut\n end'''.format(intf = intf,ip_address = ip_address, mask = mask))

    def unconfigure_ip_address(device,intf):
        device.configure('''int {intf}\n no ip address\n end'''.format(intf=intf))
    
    def enable_rip(device):
        device.configure('''feature rip\n end''')

    def disable_rip(device):
        device.configure('''no feature rip\n end''')

    def configure_rip(device,intf):
        device.configure('''int {intf}\n router rip 2\n end'''.format(intf=intf))

    def unconfigure_rip(device,intf):
        device.configure('''int {intf}\n no router rip 2\n end'''.format(intf=intf))

    def configure_acl(device,acl_name,rule):
        device.configure('''ip access-list {acl_name}\n {rule}'''.format(acl_name=acl_name,rule=rule))

    def unconfigure_acl(device,acl_name):
        device.configure('''no ip access-list {acl_name}'''.format(acl_name=acl_name))

    def configure_acl_interface(device,intf,acl_name,bound):
        device.configure('''int {intf} \n ip access-group {acl_name} {bound}'''.format(intf=intf,acl_name=acl_name,bound=bound))

    def unconfigure_acl_interface(device,intf,acl_name,bound):
        device.configure('''int {intf} \n no ip access-group {acl_name} {bound}'''.format(intf=intf,acl_name=acl_name,bound=bound))

    def sh_version(input):
        pattern1 = re.compile(' NXOS: version(?P<version>.*)')
        pattern2 = re.compile('  NXOS image file is: (?P<image>.*)')
#        pattern1 = re.compile('  NXOS: version (\d+\.\d+\(\d+\))')
#        pattern2 = re.compile('  NXOS image file is: bootflash:///nxos\.\d+\.\d+\.bin')
        output_dict = {}
        for line in input.split("\n"):
            p1 = pattern1.match(line)
            if p1:
                output_dict.update(p1.groupdict())
            p2 = pattern2.match(line)
            if p2:
                output_dict.update(p2.groupdict())
        return output_dict

    def validate_ping(input):
        pattern = re.compile('(?P<sent_pkt>[0-9]+) packets transmitted, (?P<receive_pkt>[0-9]+) packets received, (?P<pkt_loss>[0-9]+\.[0-9]+\%) packet loss')

        out_dict = {}
        for line in input.split('\n'):
            p1 = pattern.match(line)
            if p1:
                out_dict.update(p1.groupdict())
        return out_dict

