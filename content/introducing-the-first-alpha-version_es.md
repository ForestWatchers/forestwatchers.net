Title: La primera versión alfa
Date: 2012-06-19
Author: Daniel Lombraña González
Slug: introducing-the-first-alpha-version
Lang: es

Desde el proyecto estamos muy contentos al anunciar que desde hoy mismo ya se puede comenzar a probar la primera aplicación básica que hemos creado para analizar áreas deforestadas del Amazonas.

Esta [primera versión **alfa**](http://forestwatchers.net/pybossa/app/deforestedareas/presenter) permite dibujar áreas o líneas (<a title="Estamos utilizando el framework CSS Twiitter Bootstrap para la barra de herramientas" href="#" rel="tooltip"> utilizando la barra de herramientas que hay debajo del mapa</a>) para marcar o identificar aquellas zonas que podrían estar afectadas por la deforestación y que la capa de segmentación no está mostrando.

También se pueden añadir <a title="OpenLayers.JS proporciona todas estas características!" href="#" rel="tooltip">marcadores al mapa</a> para avisarnos de que hay algo relevante que necesita ser revisado posteriormente por los expertos. 

<ul class="thumbnails">
<li class="span8">
<div class="thumbnail well">
<div class="caption">
<h5>Pantallazo de la aplicación Áreas deforestadas</h5>
<p>Este pantallazo muestra cómo un usuario puede dibujar polígonos para identificar áreas deforestadas, así como añadir marcadores que permitan revisar posteriormente algún elemento interesante de la imagen por los expertos.</p>
</div>
<p><img class="visible-desktop" src="/static/images/demo400.png" alt="" /></p>
</div>
</li>
</ul>
<p style="text-align: center;"><a class="btn btn-large btn-primary" href="/pybossa/app/deforestedareas/presenter"><em class="icon icon-white icon-heart"></em> Si te gusta puedes probar la aplicación!</a></p>
<p>&nbsp;</p>

Por el momento solo estamos trabajando con una única imagen, pero habrá muchas más en el futuro. La capa de segmentación se ha creado con varios errores para que así se puedan identificar áreas deforestadas que no han sido correctamente identificadas.

Por favor, añadid tantos polígonos como queráis (líneas y/o puntos también) al mapa, dado que esta es una aplicación de demostración, no os preocupéis no vais a <a title="Si algo falla, por favor decídnoslo! Estaremos encantados en arreglarlo!" href="#" rel="tooltip">estropear nada</a>.

<p><span class="label label-warning"><em class="icon icon-white icon-bullhorn"></em> Aviso</span> <em>La página web está en <a title="Estamos mejorando PyBossa, las tareas, las aplicaciones, ..." href="#" rel="tooltip">contínuo desarrollo</a>, por lo que de vez en cuando lanzaremos de nuevo las aplicaciones pudiendo borrar todos los datos de la base de datos.</em></p>

Esperamos que disfrutéis de esta primera versión, y nos gustaría oir vuestra opinión, así que si queréis, poneros en contacto con nosotros por <a href="/contact.html">correo electrónico<em class="icon icon-envelope"></em></a> y enviadnos vuestros comentarios, ideas, etc.
<p><script>
  $("[rel=tooltip]").tooltip();
</script></p>
