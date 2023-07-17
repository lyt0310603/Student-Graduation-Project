document.addEventListener('DOMContentLoaded', function () {
  var links = document.getElementsByTagName("a");
  for (var i = 0; i < links.length; i++) {
      (function () {
          var ln = links[i];
          var location = ln.href;
          ln.onclick = function () {
              chrome.tabs.create({active: true, url: location});
          };
      })();
  }

  var button_open = document.getElementById("open")
  var button_close = document.getElementById("close")
  button_open.onclick = function(){
    chrome.runtime.sendMessage({content: "open"})
  }
  button_close.onclick = function(){
    chrome.runtime.sendMessage({content: "close"})
  }
});
