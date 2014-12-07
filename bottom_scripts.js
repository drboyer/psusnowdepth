/* Scripts run once the page is loaded */

$(document).ready(function(){
  $.ajax('http://thecloudonline.net/psusnowdepth/getdata.php', {
    success: function(data) {
      var rawdata = $.parseJSON(data);

      var curdepthval = rawdata[rawdata.length - 1][1];
      $('#currentdepth').text((curdepthval == -1) ? '&lt; 1' : curdepthval);
      var curdepthdate = new Date(rawdata[rawdata.length - 1][0]);
      $('#currentdatelabel').text(" as of " + (curdepthdate.getUTCMonth()+1) + '/' + curdepthdate.getUTCDate() + '/' + 
        curdepthdate.getUTCFullYear());

      var graphdata = rawdata;
      for (var i = 0; i < graphdata.length; i++) {
        if(graphdata[i][1] == -1) {
          graphdata[i][1] = 0.5;
        } 
      };

      $.plot($("#depthgraph"), [graphdata], {
        xaxis: {
          mode: "time",
          timeformat: "%m/%d/%y"
        },
        series: {
          lines: {
            show: true
          },
          points: {
            show: true
          }
        },
        colors: ['#000D56']
      });
    }
  })
});
