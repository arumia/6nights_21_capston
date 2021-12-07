(function() {

    const socket = new WebSocket('ws://localhost:8080/ws');
     
    socket.onopen = function () {  
      console.log('connected');
      sendMessage({ method: 'open', args: { port: '/dev/ttyACM1', baudrate: 115200, msg: 'Port is opened' } });
    }; 

    socket.onmessage = function (message) {
      var received_data = $('#received-data');

      if (message.data == 'Port name not found.') {
        $('#cmd-port').text('Open Port').removeClass('btn-danger').addClass('btn-success');
      }
      received_data.val(received_data.val() + message.data + '\n');
      received_data.scrollTop(received_data[0].scrollHeight);
    };

    socket.onclose = function () {
      console.log('disconnected'); 
    };

    const sendMessage = function (message) {
      socket.send(JSON.stringify(message))
    };

    // $('#cmd-port').on('click', function (evt) {
    //       var cmd = "Open Port",
    //       port = $('#port').val();
    //
    //   if (cmd == 'Open Port') {
    //     if (port.length < 4) {
    //         alertify.set('notifier', 'position', 'top-right');
    //         alertify.error('Port Name invalid.');
    //         return false;
    //     }
    //     $(this).text('Close Port').removeClass('btn-success').addClass('btn-danger');
    //     sendMessage({ method: 'open', args: { port: '/dev/ttyACM0', baudrate: 115200, msg: 'Port is opened' } });
    //   }
    //   else {
    //       $(this).text('Open Port').removeClass('btn-danger').addClass('btn-success');
    //       sendMessage({ method: 'close', args: { msg: 'Port is closed' } })
    //   }
    // });

    $('#message').on('keydown', function (evt) {
      if (evt.keyCode == 13) {
        $('#send-message').trigger('click');
        return false;
      }  
    });

    $('#send-message').on('click', function (evt) {
        sendMessage({ method: 'send', args: { data: $('#message').val(), msg: false } });
    });

    $('#startbtn').on('click', function (evt) {
        sendMessage({ method: 'send', args: { data: "d", msg: false } });
        sendMessage({ method: 'send', args: { data: "u", msg: false } });
    });
    $('#clear').on('click', function(evt) {
        $('#received-data').val('');
    });
})();