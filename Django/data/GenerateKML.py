import itertools
from lxml import etree
from pykml.factory import KML_ElementMaker as KML
from pykml.factory import GX_ElementMaker as GX
#from seasight_forecasting import global_vars

def CreateKML(data, coordiantes):
    kml = KML.kml(
    KML.Document(
        KML.Placemark(
            KML.name('Weather'),
            KML.ExtendedData(
                KML.Data(
                    KML.value(data[0]),
                    name="Temperature:"
                ),
                KML.Data(
                    KML.value(data[1]),
                    name="Pressure:"
                ),
                KML.Data(
                    KML.value(data[2]),
                    name="Precipitation:"
                ),
                KML.Data(
                    KML.value(data[3]),
                    name="Humidity:"
                ),
                KML.Data(
                    KML.value(data[4]),
                    name="Wind speed:"
                ),
                KML.Data(
                    KML.value(data[5]),
                    name="Wind direction:"
                )
            ),
            KML.Polygon(
                KML.outerBoundaryIs(
                    KML.LinearRing(
                        KML.coordinates(coordiantes)
                    ),
                    KML.extrude(1),
                    KML.altitudeMode("relativeToGround")
                )
            ),
            KML.Style(
                KML.BalloonStyle(
                    KML.bgColor("ff88F452")
                ),
                KML.PolyStyle(
                    KML.color("ff0000ff"),
                    KML.outline(10)
                )
            ),
            GX.balloonVisibility(1)
        )
    )
    )
    
    f = open("data/static/destination.kml", "w")
    out = etree.tostring(kml, pretty_print=True).decode("utf-8")
    f.write(out)
    f.close()
