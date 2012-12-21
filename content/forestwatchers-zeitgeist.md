Title: 2012 Zeitgeist
Date: 2012-12-21
Author: Daniel Lombraña González
Slug: 2012-zeitgeist
Lang: en

**Zeitgeist** the *spirit of the time* [according to Wikipedia](http://en.wikipedia.org/wiki/Zeitgeist) is a term usually employed to do a summary of the achievements of the current year.

For ForestWatchers 2012 has been a great year! We started in January creating a road map for the project, with the goals of creating a tool that could be useful for fighting the deforestation in the forests of the world.

Our goal is simple: build a global network of volunteers to monitor forests across the world.

In March we had a meeting in Sao Paulo at [INPE](http://www.inpe.br/ingles/), leaders in deforestation monitoring, where the developers and researchers of the project participated in a hands on session about how INPE is tackling deforestation and making a great success thanks to the program [DETER](http://www.obt.inpe.br/deter/).

Thanks to this hands-on session we learned how difficult is sometimes to find a deforested area, clouds will be covering the forest, a recovered area could look as a deforested one, etc.

With all the acquired knowledge we started to set up the servers, the software and the data to start studying if volunteers without training (like the developers of the project) could help in monitoring forests within the project.

In August we launched the first real application of the project: [Best Tile](http://forestwatchers.net/pybossa/app/besttile) where the volunteers could help cleaning areas of a satellite image choosing the best photo from the same area taken in different days by the satellite. 

The application was presented in the second Brazil@Home event that took place in Sao Paulo. We had several hackfests and workshops were we got really good feedback from the participants and nice suggestions for the project (and also [a set of videos explaining what is the project](http://www.youtube.com/user/ForestWatchersVids)).

You can see all the cleaned areas by the volunteers in this beautiful map:


<div id="map" style="width:800px; height:400px;border: 1px solid black;"></div>
<script src="http://forestwatchers.net/pybossa/static/openlayers/OpenLayers.js"></script>
<script type="text/javascript">
     <!--
     var map, layer1, layer1b, layer2, layer2b, vector1, vector2, vector3, vector4, vector5, point1, point2;
     var mapfile = "map=/home/forestwatchers/map/maps2012.map"
     var infomapfile = "map=/home/forestwatchers/map/infoshapes.map"
     var server1 = "http://forestwatchers.net/cgi-bin/mapserv?" + mapfile
     var server2 = "http://forestwatchers.net/cgi-bin/mapserv?" + infomapfile

     point1 = new OpenLayers.Geometry.Point(-58.6, -13.2);
     point2 = new OpenLayers.Geometry.Point(-49.4, 5.7);

     var bounds = new OpenLayers.Bounds();
     bounds.extend(point1);
     bounds.extend(point2);
     bounds.toBBOX();

     function init(){
         map = new OpenLayers.Map( 'map' );
         layer1 = new OpenLayers.Layer.WMS( "All tasks", server1, 
           {
             layers: 'preliminaryall',
             isBaseLayer: true
            } );
         layer1b = new OpenLayers.Layer.WMS( "Heat map All tasks", server1, 
           {
             layers: 'heatall',
            } );
         layer2 = new OpenLayers.Layer.WMS( "Completed tasks", server1, 
           {
             layers: 'preliminarycompleted',
            } );
         layer2b = new OpenLayers.Layer.WMS( "Heat map Completed tasks", server1, 
           {
             layers: 'heatcompleted',
            } );
         vector1 = new OpenLayers.Layer.WMS( "Brazil (political map)", server2, 
           {
             layers: 'shp_brazil',
             transparent: true
           }, {
             opacity: 1.0
            } );
        vector2 = new OpenLayers.Layer.WMS( "Indigenous reserve", server2, 
           {
             layers: 'shp_indigenous',
             transparent: true,
           }, {
             visibility: false,
             opacity: 0.5
            } );
        vector3 = new OpenLayers.Layer.WMS( "Federal Conservation Areas", server2, 
           {
             layers: 'shp_conservation',
             transparent: true
           }, {
             visibility: false,
             opacity: 0.5
            } );
        vector4 = new OpenLayers.Layer.WMS( "Brazilian Amazon Hydrography", server2, 
           {
             layers: 'amazonhydro',
             transparent: true
           }, {
             visibility: false,
             opacity: 0.5
            } );
        vector5 = new OpenLayers.Layer.WMS( "World (political map)", server2, 
           {
             layers: 'shp_world',
             transparent: true
           }, {
             visibility: false,
             opacity: 1.0
            } );
         map.addLayer(layer1);
         map.addLayer(layer1b);
         map.addLayer(layer2);
         map.addLayer(layer2b);
         map.addLayer(vector5);
         map.addLayer(vector1);
         map.addLayer(vector2);
         map.addLayer(vector3);
         map.addLayer(vector4);
         map.zoomToExtent(bounds);
         map.zoomTo(8);
         map.addControl(new OpenLayers.Control.LayerSwitcher());

     }
     init();
</script>

October was a great month for us because the project was featured in the popular web site [Slashdot.org](http://science.slashdot.org/story/12/10/01/0613243/forestwatchers-lets-anyone-monitor-a-patch-of-forest) bringing the day of the publication almost **8,000 tasks completed** in just one day. Wow!

Meanwhile the volunteers were helping (and they still doing!) cleaning clouds from the images, we started to create our second and probably most important application for the project: [Deforested Areas](http://forestwatchers.net/pybossa/app/deforestedareas).

This application was designed to actually allow our contributors to identify and mark deforested areas on previously cleaned images by them. The application provides two simple tools for marking deforested areas:

 * **A drawing polygon tool** that can be used to draw the shape of one or more deforested areas in one task, and
 * **A marker tool** that can be used to identify interesting areas that may need a revision by an expert, as you don't know as a volunteer if it is a deforested area or not.

As with the previous application, we provide in *almost* real time the results provided by the volunteers:

<div id="map2" style="width:800px; height:400px;border:1px solid black;"></div>
<script type="text/javascript">
     var map, layerBestTile, layerPoly, layerPoint, layerDeter, layerIntersec, vector1;
     var mapfile = "map=/home/forestwatchers/map/maps2012.map"
     var infofile = "map=/home/forestwatchers/map/infoshapes.map"
     var server = "http://forestwatchers.net/cgi-bin/mapserv?"
     var resultserver = server + mapfile
     var infoserver = server + infofile

     var point1 = new OpenLayers.Geometry.Point(-58.6, -13.2);
     var point2 = new OpenLayers.Geometry.Point(-49.4, 5.7);

     var bounds = new OpenLayers.Bounds();
     bounds.extend(point1);
     bounds.extend(point2);
     bounds.toBBOX();
     var bounds2;

     function init(){
         map = new OpenLayers.Map( 'map2' );
         layerBestTile = new OpenLayers.Layer.WMS( "Cleaned Image by Best Tile", resultserver, 
           {
             layers: 'preliminaryall',
             isBaseLayer: true
            },
           {
             opacity: 0.9
           } );
         layerPoly = new OpenLayers.Layer.WMS( "Deforestation areas", resultserver, 
           {
             layers: 'shapePolyDeforVol',
             transparent: true
            } );
         layerPoint = new OpenLayers.Layer.WMS( "Interesting Points", resultserver, 
           {
             layers: 'shapePointDeforVol',
             transparent: true
            },
           {
             visibility: true
           } );
         vector1 = new OpenLayers.Layer.WMS( "Brazil (political map)", infoserver, 
           {
             layers: 'shp_brazil',
             transparent: true
           }, {
             opacity: 0.4
            } );
         map.addLayer(layerBestTile);
         map.addLayer(layerPoly);
         map.addLayer(layerPoint);
         map.addLayer(vector1);

         //map.zoomToMaxExtent();
         map.zoomToExtent(bounds);
         map.setOptions({
             maxExtent: bounds,
             restrictedExtent: bounds
         });
         map.setCenter(new OpenLayers.LonLat(-40.4,-13.2 ),8);
         map.zoomTo(8);
         map.addControl(new OpenLayers.Control.LayerSwitcher());

     };

     init();
 </script>


In the last months of the year we have been improving the project by giving more tools for you, the volunteers, like:

 * A new theme for the applications,
 * Access to the [statistics of the project](http://forestwatchers.net/stats/),
 * A multi-lingual web site (we speak English, Portuguese and Spanish),
 * and several features in the servers that will make the whole experience much better.

We would like to say thank you to you for all your contributions, [feedback](http://forestwatchers.net/forums.html) and the support that you have showed in the project.
We wish you a merry Christmas and a happy New Year 2013!

The team

PS: We would like to say thank you to our top contributors:

 * Martin: 1028 tasks completed!
 * Santiago: 973 tasks completed!
 * Simon Christensen: 735 tasks completed!
