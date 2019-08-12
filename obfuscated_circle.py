def o(ô): #obfuscated circle function :3
    o = -~0
    ò = o
    while ò >= -o:
        ö = round((o-ò**(o+o))**(o/(o+o))*ô)
        print(" "*(ô-ö)+"O"*ö*(o+o))
        ò -= o/ô
        
def circle(radius):
    y = 1
    while y >= -1:
        x = round((1-y**2)**0.5*radius)
        print(" "*(radius-x)+"O"*x*2)
        y -= 1/radius
