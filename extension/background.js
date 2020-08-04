// chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
//   switch (request.directive) {
//     case "popup-click":
//       // execute the content script
//       chrome.tabs.executeScript(null, {
//         // defaults to the current tab
//         file: "contentscript.js", // script to inject into page and run in sandbox
//         allFrames: true, // This injects script into iframes in the page and doesn't work before 4.0.266.0.
//       });
//       sendResponse({}); // sending back empty response to sender
//       break;
//     default:
//       // helps debug when request directive doesn't match
//       alert(
//         "Unmatched request of '" +
//           request +
//           "' from script to background.js from " +
//           sender
//       );
//   }
// });

chrome.browserAction.onClicked.addListener(function (tab) {
  chrome.windows.create({
    // Just use the full URL if you need to open an external page
    url: "www.youtube.com",
  });
});
