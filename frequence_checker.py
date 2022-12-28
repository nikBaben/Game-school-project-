import win32api


def printInfo(device):
    settings = win32api.EnumDisplaySettings(device.DeviceName, -1)
    for varName in ['DisplayFrequency']:
        return getattr(settings, varName)
