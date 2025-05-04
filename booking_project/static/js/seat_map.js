$(function(){
    const pan = $('#floorplan-panzoom').panzoom({
      contain:'invert',$zoomIn:$('#zoom-in'),$zoomOut:$('#zoom-out'),minScale:1,maxScale:3
    }); pan.panzoom('zoom',1.5,{animate:false});
    function renderSeats(seats){
      $('#seat-overlay').empty(); seats.forEach(s=>{
        const icon = s.status==='free'?'🟩':s.status==='using'?'💻':'👤';
        $('<div>').addClass('seat-btn').attr({'data-id':s.id,'data-status':s.status})
          .css({position:'absolute',top:s.y+'px',left:s.x+'px',cursor:'pointer',pointerEvents:'auto'})
          .text(icon).appendTo('#seat-overlay');
      });
    }
    function updateSeat(s){ const b=$(`.seat-btn[data-id="${s.id}"]`);
      b.attr('data-status',s.status).text(s.status==='free'?'🟩':s.status==='using'?'💻':'👤');
    }
    $('#seat-overlay').on('click','.seat-btn',function(){ if(this.dataset.status!=='free') return;
      const id=this.dataset.id; const start=prompt('開始 (YYYY-MM-DDTHH:MM)'); const end=prompt('結束');
      $.post('/by-time/',{csrfmiddlewaretoken:''+$('input[name=csrfmiddlewaretoken]').val(),room:ROOM_ID,seat_id:id,start:start,end:end});
    });
    const ws=new WebSocket((location.protocol==='https:'?'wss':'ws')+`://${location.host}/ws/seats/${ROOM_ID}/`);
    ws.onmessage=e=>{const m=JSON.parse(e.data); m.type==='seat_list'?renderSeats(m.data):updateSeat(m.data)};
  });