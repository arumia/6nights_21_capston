var received_data = $('#received-data');

received_data.val(received_data.val() + "초기화중..." + '\n');

var uid = null;        // x에 위에 '1'로 입력되는 값 저장
// ajax 통신
$.ajax({
  type: 'POST',
  url: '/rfid/',
  dataType: 'json',
  async: true,
  // 통신 error
  error: function(e) { received_data.val(received_data.val() + "NFC오류: NFC 접촉 후 새로고침 해주세요!"+'\n');}
}).done(function(result) { // 통신 성공
    received_data.val(received_data.val() + "NFC가 인식되었습니다: " + result["uid"] + "지금부터 작업이 가능합니다!"+'\n');
    uid = result["uid"];
});

const socket = new WebSocket('ws://localhost:8080/ws');

socket.onopen = function () {
//      console.log('connected');
  received_data.val(received_data.val() + "연결 시도중..." + '\n');
  received_data.scrollTop(received_data[0].scrollHeight);
  sendMessage({ method: 'open', args: { port: '/dev/ttyACM1', baudrate: 115200, msg: '제어보드 연결 성공! 작동 대기중...' } });
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

// $('#message').on('keydown', function (evt) {
//   if (evt.keyCode == 13) {
//     $('#send-message').trigger('click');
//     return false;
//   }
// });

$('#send-message').on('click', function (evt) {
    if(uid!=null) {
        sendMessage({method: 'send', args: {data: $('#message').val(), msg: false}});
    }
    else{
        received_data.val(received_data.val() + "작업 시작전 NFC에 카드를 접촉해주세요..." + '\n');
    }
});

$('#startbtn').on('click', function (evt) {
    if(uid!=null) {
        sendMessage({ method: 'send', args: { data: "d", msg: false } });
        sendMessage({ method: 'send', args: { data: "u", msg: false } });
        sendMessage({ method: 'send', args: { data: "p  ", msg: false } });
    }
    else{
        received_data.val(received_data.val() + "작업 시작전 NFC에 카드를 접촉해주세요..." + '\n');
    }
});
$('#testbtn').on('click', function (evt) {
    if(uid!=null) {
    sendMessage({ method: 'send', args: { data: "d", msg: false } });
    sendMessage({ method: 'send', args: { data: "u", msg: false } });
    }
    else{
        received_data.val(received_data.val() + "작업 시작전 NFC에 카드를 접촉해주세요..." + '\n');
    }
});
$('#upbtn').on('click', function (evt) {
    if(uid!=null) {
    sendMessage({ method: 'send', args: { data: "u", msg: false } });
    }
    else{
        received_data.val(received_data.val() + "작업 시작전 NFC에 카드를 접촉해주세요..." + '\n');
    }
});
$('#pushbtn').on('click', function (evt) {
    if(uid!=null) {
    sendMessage({ method: 'send', args: { data: "p", msg: false } });
    }
    else{
        received_data.val(received_data.val() + "작업 시작전 NFC에 카드를 접촉해주세요..." + '\n');
    }
});
$('#clear').on('click', function(evt) {
    $('#received-data').val('');
});
$('#endjob').on('click', function(evt) {
    if(uid!=null){
        $.ajax({
          type: 'POST',
          url: '/job/',
          dataType: 'json',
          async: true,
          data: {'uid':uid},
          // 통신 error
          error: function(e) { received_data.val(received_data.val() + "데이터 저장 요류: 작업 종료 버튼을 다시 눌러주세요."+'\n');}
        }).done(function(result) { // 통신 성공
            alert('작업내역이 저장되었습니다.');
            location.href="/index.html";
        });
    }
    alert('NFC카드부터 접촉해 주세요.');
});