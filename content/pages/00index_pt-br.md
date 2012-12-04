Title: Home
Slug: index
Lang: pt-br
Icon: icon-home

<div class="row">
    <div class="span8 offset2 columns">
        <h1>Ajude as florestas do planeta</h1>
            <h6 class="hidden-phone">Um projeto de ciência cidadã para o monitoramento de florestas</h6>

            <div id="myCarousel" class="carousel slide">
                <div class="carousel-inner">
                    <div class="item active">
                        <!--<a href="http://www.flickr.com/photos/leoffreitas/789157023/">-->
                        <a href="/pybossa/app/besttile/newtask">
                            <img src="|filename|/images/carousel/forest.jpg" alt="">
                        </a>
                        <div class="carousel-caption">
                            <h4>As florestas estão em perigo 
                                <small class="pull-right hidden-phone">Photo by Leonardo F. Freitas (BY-NC-SA 2.0)</small>
                            </h4>
                        </div>
                    </div>
                    <div class="item">
                        <!--<a href="http://www.flickr.com/photos/leoffreitas/1469377935/">-->
                        <a href="/pybossa/app/besttile/newtask">
                            <img src="|filename|/images/carousel/burning.jpg" alt="">
                        </a>
                        <div class="carousel-caption">
                            <h4>Queimadas, extração ilegal de madeira, ...
                                <small class="pull-right hidden-phone">Photo by Leonardo F. Freitas (BY-NC-SA 2.0)</small>
                            </h4>
                        </div>
                    </div>
                    <div class="item">
                        <!--<a href="http://www.flickr.com/photos/mcgarry/111003432/">-->
                        <a href="/pybossa/app/besttile/newtask">
                            <img src="|filename|/images/carousel/crowd.jpg" alt="">
                        </a>
                        <div class="carousel-caption">
                            <h4>Mas o povo pode ajudar!
                                <small class="pull-right hidden-phone">Photo by Kevin McGarry (BY-NC-SA 2.0)</small>
                            </h4>
                        </div>
                    </div>
                </div>
                <a class="left carousel-control" href="#myCarousel" data-slide="prev">&lsaquo;</a>
                <a class="right carousel-control" href="#myCarousel" data-slide="next">&rsaquo;</a>
            </div>
        </div>

<div class="row">
    <div class="span8 offset2" style="text-align:center;">
    <a href="/mission.html" class="btn btn-primary btn-large"><i class="icon-book"></i> Saiba mais</a>
    <a href="#" class="btn btn-large btn-inverse" onclick="showVideo()"><i class="icon-play-circle"></i> Vídeo</a>
    <a href="/pybossa" class="btn btn-success btn-large"><i class="icon-heart"></i> Contribua</a>
    </div>
</div>

<div id="videocontainer">
    <div id="video">
        <div style="text-align:center; padding:20px">
            <a href="#" class="btn btn-warning btn-large" onclick="closeVideo()"><i class="icon icon-white icon-remove"></i> Fechar vídeo</a>
        </div>

        <script type="text/javascript" src="http://s3.amazonaws.com/s3.www.universalsubtitles.org/embed.js">
            (
                {"video_url": "http://www.youtube.com/watch?v=eXMlCWmCzEs&enablejsapi=1",
                    'video_config': {
                        'playerapiid': 'amarayoutube',
                    }
        }
        )
        </script>
    </div>
</div>

<script>
    function showVideo() {
        $("#videocontainer").show();
    }
    function closeVideo() {
        $("#videocontainer").hide();
    }
</script>
