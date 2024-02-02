import colorsys

def rgb_to_hsl(rgb):
    """
    Convert RGB to HSL.
    """
    # Scale the RGB values to the 0-1 range
    r, g, b = [x / 255.0 for x in rgb]
    
    # Convert RGB to HSL
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    
    # Scale the HSL values to the 0-360, 0-100, 0-100 ranges
    h = round(h * 360)
    l = round(l * 100)
    s = round(s * 100)
    
    return (h, s, l)
