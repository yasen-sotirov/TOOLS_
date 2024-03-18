"INTERFACE SEGREGATION"     # Разделяне на интерфейсите на малки парчета

'''
Разделяме бащините класове на малки парчета, 
които комбинираме в наследниците'''



"Методите на този клас не се ползват от всички наследници"
# class EntertainmentDevice:
#     def connect_to_device_via_hdmi_cable(self, device): pass
#     def connect_to_device_via_rca_cable(self, device): pass
#     def connect_to_device_via_ethernet_cable(self, device): pass
#     def connect_device_to_power_outlet(self, device): pass


"Разделяме кода на малки парчета - класове mix-ins"

class HDMICable:
    def connect_to_device_via_hdmi_cable(self, device): pass

class RCACable:
    def connect_to_device_via_rca_cable(self, device): pass

class EthernetCable:
    def connect_to_device_via_ethernet_cable(self, device): pass

class PowerOutlet:
    def connect_device_to_power_outlet(self, device): pass



class Television(RCACable, HDMICable, PowerOutlet):
    def connect_to_dvd(self, dvd_player):
        self.connect_to_device_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_hdmi_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)



class DVDPlayer(HDMICable, PowerOutlet):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)



class GameConsole(HDMICable, EthernetCable, PowerOutlet):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        self.connect_to_device_via_ethernet_cable(router)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)



class Router(EthernetCable, PowerOutlet):
    def connect_to_tv(self, television):
        self.connect_to_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_ethernet_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)