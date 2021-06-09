document.addEventListener('keydown', function() {
  if (event.keyCode == 123) {
    alert("Haha u cant see my code noob");
    return false;
  } else if (event.ctrlKey && event.shiftKey && event.keyCode == 73) {
    alert("Haha u cant see my code noob");
    return false;
  } else if (event.ctrlKey && event.keyCode == 85) {
    alert("Haha u cant see my code noob");
    return false;
  }
}, false);

if (document.addEventListener) {
  document.addEventListener('contextmenu', function(e) {
    alert("Haha u cant see my code noob");
    e.preventDefault();
  }, false);
} else {
  document.attachEvent('oncontextmenu', function() {
    alert("Haha u cant see my code noob");
    window.event.returnValue = false;
  });
}
