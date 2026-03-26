self.addEventListener("push", function(event) {
  var data = {};
  try { data = event.data.json(); } catch(e) {}
  var title = data.title || "Новый лид";
  var options = {
    body: data.body || "",
    icon: "/icon-192.png",
    badge: "/icon-96.png",
    vibrate: [200, 100, 200],
    data: data.data || {},
    actions: [
      { action: "open", title: "Открыть сделку" },
      { action: "close", title: "Закрыть" }
    ]
  };
  event.waitUntil(self.registration.showNotification(title, options));
});

self.addEventListener("notificationclick", function(event) {
  event.notification.close();
  if(event.action === "open" || !event.action) {
    var url = (event.notification.data && event.notification.data.url) || "/";
    event.waitUntil(clients.openWindow(url));
  }
});
