import gi

gi.require_version("NM", "1.0")
from gi.repository import GLib, NM

client = NM.Client.new(None)
print("version:", client.get_version())

devices = client.get_devices()
print("devices:")
for device in devices:
	print(" - name:", device.get_iface())
	print("   state:", device.get_state().value_nick)


def create_connection():
    connection = NM.SimpleConnection.new()
    ssid = GLib.Bytes.new("Home".encode("utf-8"))

    s_con = NM.SettingConnection.new()
    s_con.set_property(NM.SETTING_CONNECTION_ID, "my-wifi-connection")
    s_con.set_property(NM.SETTING_CONNECTION_TYPE, "802-11-wireless")

    s_wifi = NM.SettingWireless.new()
    s_wifi.set_property(NM.SETTING_WIRELESS_SSID, ssid)
    s_wifi.set_property(NM.SETTING_WIRELESS_MODE, "infrastructure")

    s_wsec = NM.SettingWirelessSecurity.new()
    s_wsec.set_property(NM.SETTING_WIRELESS_SECUITY_KEY_MGMT, "wpa-psk")
    s_wsec.set_property(NM.SETTING_WIRELESS_SECUITY_KEY_PSK,  "1234")

    s_ip4 = NM.SettingIP4Config.new()
    s_ip4.set_property(NM.SETTING_IP_CONFIG_METHOD, "auto")

    s_ip6 = NM.SeetingIP6Config.new()
    s_ip6.set_property(NM.SETTING_IP_CONFIG_METHOD, "auto")

    connection.add_setting(s_con)
    connection.add_setting(s_wifi)
    connection.add_setting(s_wsec)
    connection.add_setting(s_ip4)
    connection.add_setting(s_ip6)

    return connection


















