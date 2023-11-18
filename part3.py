import random as rd


class HtmlDocument:
    """HtmlDocument class"""
    def __init__(self) -> None:
        """__init__ method"""

        self.head = ["<html>\n", "</head>\n"]
        self.title = ["\t""<title>", "My Artwork", "</title>\n"]
        self.body = ["<body>\n"]
        self.footer = ["</body>\n", "</html>\n"]
    
    def write_html(self, filename) -> None:
        """write_html method"""


        with open(filename, "w") as f:
            f.write(" ".join(self.head))
            f.write(" ".join(self.title))
            f.write(" ".join(self.body))
            f.write(" ".join(self.footer))

    def add_svg_canvas(self, canvas) -> None:
        """add_svg_canvas method"""

        self.body.insert(1, canvas)

class SvgCanvas:
    """SvgCanvas class"""

    def __init__(self, width, height) -> None:
        """__init__ method"""

        self.canvas = f'\t<svg width="{width}" height="{height}">\n'
        self.shapes = []
        
    def add_shape(self, shape) -> None:
        """add_shape method"""

        self.shapes.append(shape)
        
    def gen_art(self) -> str:
        """gen_art method"""

        for shape in self.shapes:
            self.canvas += shape.as_svg()
        self.canvas += "\t</svg>\n"
        return self.canvas
    
class PyArtConfig:
    """PyArtConfig class""" 
    # setting the boundaires for the random numbers
    SHA = [0, 1, 3]
    X = (0, 500)
    Y = (0, 500)
    RAD = (0, 100)
    RX = (10, 30)
    RY = (10, 30)
    W = (10, 100)
    H = (10, 100)
    R = (0, 255)
    G = (0, 255)
    B = (0, 255)
    OP = (0, 1.0)

    def __init__(self, CNT, SHA, X, Y, RAD, RX, RY, W, H, R, G, B, OP) -> None:
        """__init__ method"""

        self.CNT = CNT
        self.SHA = SHA
        self.X = X
        self.Y = Y
        self.RAD = RAD
        self.RX = RX
        self.RY = RY
        self.W = W
        self.H = H
        self.R = R
        self.G = G
        self.B = B
        self.OP = OP


class Randomshape:
    """Randomshape class"""

    def __init__(self, config) -> None:
        """__init__ method"""

        self.config = config
        # CNT will increment by 1 for each shape
        self.CNT = config.CNT
        config.CNT += 1
        # using the choice function since 2 can not be included 
        self.SHA = rd.choice(config.SHA)
        self.X = rd.randint(config.X[0], config.X[1])
        self.Y = rd.randint(config.Y[0], config.Y[1])
        self.RAD = rd.randint(config.RAD[0], config.RAD[1])
        self.RX = rd.randint(config.RX[0], config.RX[1])
        self.RY = rd.randint(config.RY[0], config.RY[1])
        self.W = rd.randint(config.W[0], config.W[1])
        self.H = rd.randint(config.H[0], config.H[1])
        self.R = rd.randint(config.R[0], config.R[1])
        self.G = rd.randint(config.G[0], config.G[1])
        self.B = rd.randint(config.B[0], config.B[1])
        # using the round function to round the opacity to 1 decimal place
        self.OP = round(rd.uniform(config.OP[0], config.OP[1]), 1)
    
    def as_svg (self) -> str:
        """as_svg method"""

        if self.SHA == 0:
            # call class CircleShape
            return CircleShape((self.X, self.Y), self.RAD, (self.R, self.G, self.B), self.OP).gen_svg()
        elif self.SHA == 1:
            # call class EllipseShape
            return EllipseShape((self.X, self.Y), self.RX, self.RY, (self.R, self.G, self.B), self.OP).gen_svg()
        elif self.SHA == 3:
            # call class RectangleShape
            return RectangleShape(self.X, self.Y, self.W, self.H, (self.R, self.G, self.B), self.OP).gen_svg()
        


class CircleShape:
    """CircleShape class"""

    def __init__(self, center, radius, fill, fill_opacity) -> None:
        """__init__ method"""

        self.center = center
        self.radius = radius
        self.fill = fill
        self.fill_opacity = fill_opacity
    def gen_svg(self) -> str:
        """gen_svg method"""

        cx, cy, r = self.center[0], self.center[1], self.radius
        fill = self.fill
        fill_opacity = self.fill_opacity
        return f'\t \t <circle cx="{cx}" cy="{cy}" r="{r}" fill="rgb{fill}"  fill-opacity="{fill_opacity}"></circle>\n'



class EllipseShape:
    """EllipseShape class"""
    def __init__(self, center, radius_x, radius_y, fill, fill_opacity) -> None:
        """initialize the ellipse shape"""

        self.center = center
        self.radius_x = radius_x
        self.radius_y = radius_y
        self.fill = fill
        self.fill_opacity = fill_opacity
    def gen_svg(self) -> str:
        """gen_svg method"""

        cx, cy, rx, ry = self.center[0], self.center[1], self.radius_x, self.radius_y
        fill = self.fill
        fill_opacity = self.fill_opacity
        return f'\t \t <ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="rgb{fill}"  fill-opacity="{fill_opacity}"></ellipse>\n'
    


class RectangleShape:
    """RectangleShape class"""

    def __init__(self, x, y, width, height, fill, fill_opacity) -> None:
        """__init__ method"""

        self.corner = (x, y)
        self.width = width
        self.height = height
        self.fill = fill
        self.fill_opacity = fill_opacity

    def gen_svg(self) -> str:
        """gen_svg method"""

        x, y, w, h = self.corner[0], self.corner[1], self.width, self.height
        fill = self.fill
        fill_opacity = self.fill_opacity
        return f'\t \t <rect x="{x}" y="{y}" width="{w}" height="{h}" fill="rgb{fill}"  fill-opacity="{fill_opacity}"></rect>\n'
    



def main() -> None:
    """main method"""

    # number of shapes to generate
    num_shapes = 1000
    
    # config for the random shapes
    config = PyArtConfig(0, PyArtConfig.SHA, PyArtConfig.X, PyArtConfig.Y, PyArtConfig.RAD, PyArtConfig.RX, PyArtConfig.RY, PyArtConfig.W, PyArtConfig.H, PyArtConfig.R, PyArtConfig.G, PyArtConfig.B, PyArtConfig.OP)

    # boundaries for the canvas
    svg_canvas = SvgCanvas(600, 600)

    # add each shape to the html document
    for x in range(num_shapes):
        shape = Randomshape(config)
        # new line after each shape
        svg_canvas.add_shape(shape)


    doc = HtmlDocument()
    doc.add_svg_canvas(svg_canvas.gen_art())
    doc.write_html("art.html")



if __name__ == "__main__":
    main()
