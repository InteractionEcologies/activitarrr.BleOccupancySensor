from brisa.core.reactors import install_default_reactor
from brisa.core.reactors.glib2 import GLib2Reactor
#reactor = install_default_reactor()
import ipdb
import os
reactor = GLib2Reactor()
import brisa
from brisa.upnp.device import Device, Service

class SwitchPower(Service):

    def __init__(self):
        
        Service.__init__(self, 'SwitchPower',
                         'urn:schemas-upnp-org:service:SwitchPower:1',
                         '',
                         os.getcwd() + '/BleOccupancy-scpd.xml')
        self.target = False
        self.status = False


    def soap_SetTarget(self, *args, **kwargs):
        self.target = kwargs['newTargetValue']
        print 'Light switched ', {'1': 'on', '0': 'off'}.get(self.target, None)
        # Status here is the target because our device is "perfect" and
        # no errors could occur (this is a simulation)
        self.status = self.target
        return {}


    def soap_GetTarget(self, *args, **kwargs):
        return {'RetTargetValue': self.target}


    def soap_GetStatus(self, *args, **kwargs):
        return {'ResultStatus': self.status}

class BinaryLight(object):

    def __init__(self):
        self.server_name = 'Binary Light Device'
        self.device = None

    def _create_device(self):

        project_page = 'https://garage.maemo.org/projects/brisa'
        self.device = Device('urn:schemas-upnp-org:device:BinaryLight:1',
                             self.server_name,
                             manufacturer='Brisa Team. Embedded Laboratory '\
                                          'and INdT Brazil',
                             manufacturer_url=project_page,
                             model_name='Binary Light Device',
                             model_description='A UPnP Binary Light Device',
                             model_number='1.0',
                             model_url="http://www.bleoccupancy.com/",
                             serial_number="00")

    def _add_services(self):
        switch = SwitchPower()
        self.device.add_service(switch)

    def start(self):
        self._create_device()
        self._add_services()
        self.device.start()
        reactor.add_after_stop_func(self.device.stop)
        reactor.main()

if __name__ == '__main__':
    device = BinaryLight()
    device.start()
