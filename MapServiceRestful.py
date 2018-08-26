#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by vellhe 2018/8/25
from flask import Flask,jsonify
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
#parser.add_argument(' ')

global null,true,false
null=''
true=True
false=False

#地图信息字典，模拟参数
MapServiceList={
    "serviceDescription": "Test Map Service Description",
    "mapName": "JiangSu",
    "description": "Map Jiangsu",
    "copyrightText": "Esri",
    "layers": [
        {"id" : 0, "name" : "Cities", "defaultVisibility" :true,"parentLayerId" : -1, "subLayerIds" : null},
        {"id" : 1, "name" : "States", "defaultVisibility" : true,"parentLayerId" : -1, "subLayerIds" : null},
        {"id" : 2, "name" : "Counties", "defaultVisibility" : false,"parentLayerId" : -1, "subLayerIds" : [3, 4]},
        {"id" : 3, "name" : "Large Counties", "defaultVisibility" :false, "parentLayerId" : 2, "subLayerIds" : null},
        {"id" : 4, "name" : "Small Counties", "defaultVisibility" :false, "parentLayerId" : 2, "subLayerIds" : null}
    ],
    "spatialReference" : {"wkid" : 4326},
    "singleFusedMapCache" : true,
    "tileInfo": {
        "rows" : 512, "cols" : 512, "dpi" : 96, "format" : "JPEG",
        "compressionQuality" : 75,
        "origin" : {"x" : -130.0, "y" : 50.0},
        "spatialReference" : {"wkid" : 4326},
        "lods": [
            {"level" : 0, "resolution" : 8.46, "scale" : 32000.0 },
            {"level" : 1, "resolution" : 4.23, "scale" : 16000.0 },
            {"level" : 2, "resolution" : 2.11, "scale" : 8000.0 },
            {"level" : 3, "resolution" : 1.05, "scale" : 4000.0 },
            {"level" : 4, "resolution" : 0.52, "scale" : 2000.0 }
        ]
    },
    "initialExtent" : {
        "xmin":-109.55,
        "ymin":25.76,
        "xmax":-86.39,
        "ymax":49.94,
        "spatialReference":{"wkid":4326}
    },
    "fullExtent" : {
        "xmin" : -130.0,
        "ymin" : 24.0,
        "xmax" : -65.0,
        "ymax" : 50.0,
        "spatialReference" : {"wkid" : 4326}
    },
    "units" : "esriDecimalDegrees",
    "supportedImageFormatTypes":
    "PNG32,PNG24,PNG,JPG,DIB,TIFF,EMF,PS,PDF,GIF,SVG,SVGZ",
    "documentInfo": {
        "Title" : "StreetMap USA.mxd",
        "Author" : "Esri Data Team",
        "Comments" : "Esri Data and Maps 2004",
        "Subject" : "Street level data for the US",
        "Category" : "vector",
        "Keywords" : "StreetMap USA"
    } ,
    "capabilities" : "Map,Query,Data"
}

#读地图属性
def propertyRead():
    #MapServiceList["serviceDescription"]="Test Map Service Description"
    #MapServiceList["mapName"]= "JiangSu"
    #MapServiceList["description"]="Map Jiangsu"
    #MapServiceList["copyrightText"]="Esri"
    #MapServiceList["layers"]=
    #MapServiceList["spatialReference"]=
    pass


#Parent Resource of MapServ ice
class Catalog(Resource):
    def get(self):
        pass


class MapService(Catalog):
    def get(self):

        return jsonify(MapServiceList)



class MapTile(MapService):
    def get(self,level,row,column):
        #读cache文件
        pass


class LayerTable(MapService):
    def get(self,layerOrTableId):
        pass

class AllLayersAndTables(MapService):
    def get(self):
        pass

##
## Actually setup the Api resource routing here
##
api.add_resource(MapService, '/MapServer')
api.add_resource(MapTile, '/MapServer/tile/<int:level>/<int:row>/<int:column>')
api.add_resource(LayerTable, '/MapServer/<int:layerOrTableId>')
api.add_resource(AllLayersAndTables, '/MapServer/layers')

if __name__ == '__main__':
    app.run(debug=True)
