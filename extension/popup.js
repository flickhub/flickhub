function clickHandler(e) {
  chrome.runtime.sendMessage({ directive: "popup-click" }, function (response) {
    chrome.windows.create({
      // Just use the full URL if you need to open an external page
      url: "http://localhost:3000?id=3443",
    });
  });
}

document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("click-me").addEventListener("click", clickHandler);
});
