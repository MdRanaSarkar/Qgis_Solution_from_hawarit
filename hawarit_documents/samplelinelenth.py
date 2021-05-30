def lineLengthCalc():
    """Sums together the length of features in a line type vector layer, then prints the result in km."""
    # get the current active layer
    layer = iface.activeLayer()

    total_length = 0

    for feat in layer.getFeatures():
        geometry = feat.geometry()
        total_length += geometry.length()

    # print out the result
    print("Total length of features in layer "+ layer.sourceName()+ " is:", round(total_length/1000, 1), "km")

# call the function
lineLengthCalc()