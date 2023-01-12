function callback(data, status) {
                if (status == "success") {
                var roomid = data.options['roomid']
                var ctx = document.getElementById("myChart"+roomid).getContext("2d");
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

function callback_temp(data, status) {
                if (status == "success") {
                var ctx = document.getElementById("tempChart").getContext("2d");
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