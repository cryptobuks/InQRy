from inqry.system_specs import cfgutil

CFGUTIL_OUTPUT = '''
{"Command":"get","Output":{"0xA64D620D30D26":{"serialNumber":"F71SHPP0HG6W", "totalDiskCapacity":32000000000,
"deviceType":"iPhone9,1","IMEI":"359167076630320","color":"1"},"0x970E80428AC26":{"serialNumber":"DLXQK7WRGMLD",
"totalDiskCapacity":31708938240,"deviceType":"iPad6,7","color":"#3b3b3c"}, "Errors":{"0xA64D620D30D26":{},
"0x970E80428AC26":{"IMEI":{"Domain":"com.apple.configurator.MobileDeviceKit.amd.error","FailureReason":"",
"Message":"The value is missing.", "Code":-402653163}}}},"Type":"CommandOutput","Devices":["0x970E80428AC26",
"0xA64D620D30D26"]}
'''

RESULT = cfgutil.parse_cfgutil_output(CFGUTIL_OUTPUT)
DEVICE0 = cfgutil.create_from_device_hardware_overview(CFGUTIL_OUTPUT)[0]
DEVICE1 = cfgutil.create_from_device_hardware_overview(CFGUTIL_OUTPUT)[1]


def test_getting_device_ecid():
    assert cfgutil.get_all_device_ecids(CFGUTIL_OUTPUT) == ["0x970E80428AC26", "0xA64D620D30D26"]


def test_getting_serial_of_first_device_using_device_value():
    ecid = RESULT['Devices'][0]
    assert RESULT['Output'][ecid]['serialNumber'] == 'DLXQK7WRGMLD'


def test_getting_serial_of_second_device_using_device_value():
    ecid = RESULT['Devices'][1]
    assert RESULT['Output'][ecid]['serialNumber'] == 'F71SHPP0HG6W'


def test_getting_ecid():
    assert RESULT['Devices'] == ["0x970E80428AC26", "0xA64D620D30D26"]


def test_getting_serial_number_from_device_specs_objects():
    assert DEVICE1.serial_number == 'F71SHPP0HG6W'


def test_getting_storage_returns_as_human_readable_string():
    assert DEVICE1.storage == '32 GB'


def test_getting_storage_returns_as_human_readable_string_from_second_device():
    assert DEVICE1.storage == '32 GB'


def test_getting_device_hardware_overview():
    assert cfgutil.get_hardware_overview_for_all_devices(CFGUTIL_OUTPUT)[1] == {
        "serialNumber": "F71SHPP0HG6W", "totalDiskCapacity": 32000000000,
        "deviceType": "iPhone9,1", "IMEI": "359167076630320", "color": "1"}
