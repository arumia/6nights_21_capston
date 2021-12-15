def getgps():
    import gpsd

    # Connect to the local gpsd
    gpsd.connect()

    # See the inline docs for GpsResponse for the available data
    for i in range(0,10):
        # Get gps position
        packet = gpsd.get_current()
        if(packet.mode):
            print("lat lng: "+packet.lat+", "+ packet.lon)
            return True, packet.lat, packet.lon
        else:
            continue
    return False, -1, -1