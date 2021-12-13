function getRFID(){
    var received_data = $('#received-data');
    // var x = $("#test_value").val();        // x에 위에 '1'로 입력되는 값 저장
    // ajax 통신
    $.ajax({
      type: 'POST',
      url: '/rfid/',
      // data: {number:x},                    // x를 number라는 이름으로 views로 넘겨준다.
      dataType: 'json',
      async: false,
      // 통신 성공
      success: function(result){
          received_data.val(received_data.val() + result["uid"] + '\n');
      },
      // 통신 error
      error: function(e) { console.log('error:'+e.status);}
    });
}
(function() {

    var received_data = $('#received-data');

    received_data.val(received_data.val() + "NFC에 카드를 접촉해주세요..." + '\n');
    getRFID();

    const socket = new WebSocket('ws://localhost:8080/ws');

     
    socket.onopen = function () {  
//      console.log('connected');
      received_data.val(received_data.val() + "연결 시도중..." + '\n');
      received_data.scrollTop(received_data[0].scrollHeight);
      sendMessage({ method: 'open', args: { port: '/dev/ttyACM1', baudrate: 115200, msg: '연결 성공! 작동 대기중...' } });
    }; 

    socket.onmessage = function (message) {

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
        sendMessage({ method: 'send', args: { data: "p  ", msg: false } });
    });
    $('#testbtn').on('click', function (evt) {
        sendMessage({ method: 'send', args: { data: "d", msg: false } });
        sendMessage({ method: 'send', args: { data: "u", msg: false } });
    });
    $('#upbtn').on('click', function (evt) {
        sendMessage({ method: 'send', args: { data: "u", msg: false } });
    });
    $('#pushbtn').on('click', function (evt) {
        sendMessage({ method: 'send', args: { data: "p", msg: false } });
    });
    $('#clear').on('click', function(evt) {
        $('#received-data').val('');
    });
})();