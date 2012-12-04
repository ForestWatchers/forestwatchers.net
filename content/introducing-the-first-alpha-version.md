Title: Introducing the first alpha version
Date: 2012-06-19
Author: Daniel Lombraña González
Slug: introducing-the-first-alpha-version
Lang: en

We are really happy to announce that since today you can start playing with the base application that we have created for tracking deforested areas from real satellite imagery from the Amazon.

This [first **alpha** version](http://forestwatchers.net/pybossa/app/deforestedareas/presenter) lets you draw areas or lines (<a title="We are using the Twitter Bootstrap CSS framework for the toolbar" href="#" rel="tooltip"> check the black toolbar below the map</a>) to mark zones that could be affected by deforestation and that the segmentation layer is not showing.

You can also add <a title="OpenLayers.JS gives us all this flexibility!" href="#" rel="tooltip">different markers to the map</a>, just to warn us that something is relevant and needs to be reviewed.

<ul class="thumbnails">
<li class="span8">
<div class="thumbnail well">
<div class="caption">
<h5>Deforested Areas Demo Application Screenshot</h5>
<p>This screenshot shows how a user can draw areas to mark deforested zones, as well as add markers to warn the project about something interesting.</p>
</div>
<p><img class="visible-desktop" src="|filename|/images/demo400.png" alt="" /></p>
</div>
</li>
</ul>
<p style="text-align: center;"><a class="btn btn-large btn-primary" href="/pybossa/app/deforestedareas/presenter"><em class="icon icon-white icon-heart"></em> If you like it, you can try it yourself!</a></p>
<p>&nbsp;</p>
<p>For the moment there is only one satellite image available, but we have more in the pipeline. The segmentation layer was created with some errors, so there should be deforested areas not covered at all and it will be possible to draw a polygon around them.</p>
<p>Please, feel free to add as many polygons, lines and/or points to the map, as this is just a demo, don&#8217;t be afraid, <a title="If you break something let us know! We would love to fix it!" href="#" rel="tooltip">you will not break anything!</a></p>
<p><span class="label label-warning"><em class="icon icon-white icon-bullhorn"></em> Warning</span> <em>The site is under <a title="We are improving PyBossa, the tasks, the application, ..." href="#" rel="tooltip">heavy development</a>, so from time to time we may re-deploy the whole site erasing all the data from the database.</em></p>
<p>We hope you enjoy this very first version, and we would love to hear from you, so please, feel free to <a href="/contact.html">send us an e-mail <em class="icon icon-envelope"></em></a> with your comments, suggestions, ideas, etc.</p>
<p><script>
  $("[rel=tooltip]").tooltip();
</script></p>
