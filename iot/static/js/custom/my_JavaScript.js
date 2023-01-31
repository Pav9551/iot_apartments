



function callback(data, status) {
                if (status == "success") {
                var roomid = data.options['roomid']
                var ctx = document.getElementById("myChart"+roomid).getContext("2d");
                var myChart = new Chart(ctx, {type: 'line', data: data.data,options: data.options,

                });
                myChart.destroy();

                myChart = new Chart(ctx, {
                    type: 'line', data: data.data,options: data.options,

                });

                //alert(roomid);
                }
                else {
		                alert("There was a problem");
            	}


                //setTimeout(getReading, 3000);
            }

function callback_temp(data, status) {

                if (status == "success") {
//https://question-it.com/questions/1205756/kak-ochistit-diagrammu-ot-holsta-chtoby-sobytija-pri-navedenii-ne-mogli-byt-vyzvany
               // $('#tempChart').remove(); // this is my <canvas> element
               // $('#graph-container').append('<canvas id="tempChart" width="100%" height="40"></canvas>');
                canvas = document.querySelector('#tempChart');
                var ctx = canvas.getContext('2d');


                //var ctx = document.getElementById("tempChart").getContext("2d");
                new Chart(ctx, {
                    type: 'line', data: data.data,options: data.options,
                });
                //alert(roomid);
                }
                else {
		                alert("There was a problem");
            	}

                //setTimeout(getReading, 3000);

            }
function callback_hum(data, status) {
                if (status == "success") {
                var ctx = document.getElementById("humChart").getContext("2d");
                new Chart(ctx, {
                    type: 'line', data: data.data,options: data.options,
                });
                //alert(roomid);
                }
                else {
		                alert("There was a problem");
            	}
                //setTimeout(getReading, 3000);

            }