$(function(){
  const container = $("#seat-map");
  const slotId = container.data("slot-id");
  const protocol = window.location.protocol === "https:" ? "wss" : "ws";
  const ws = new WebSocket(`${protocol}://${window.location.host}/ws/seats/${slotId}/`);

  ws.onmessage = function(e) {
    const data = JSON.parse(e.data);
    const booked = data.booked;
    container.find(".seat").each(function(){
      const el = $(this);
      const id = el.data("seat-id");
      if (booked.includes(id)) {
        el.addClass("bg-danger text-white").removeClass("bg-success");
      } else {
        el.removeClass("bg-danger text-white");
      }
    });
  };

  container.on("click", ".seat", function(){
    const el = $(this);
    const seatId = el.data("seat-id");
    const action = el.hasClass("bg-danger") ? "release" : "reserve";
    ws.send(JSON.stringify({ action, seat_id: seatId }));
  });
});
