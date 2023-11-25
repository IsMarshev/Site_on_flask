const sidebar = document.getElementById('sidebar');


window.addEventListener('resize', function () {
  if (window.innerWidth < 600) {
    sidebar.classList.add('hide');
  } else {
    sidebar.classList.remove('hide');
  }
});

window.onload = function() {
	// Уменьшаем окно на 1px
	window.resizeBy(-100, 0);
  
	// Возвращаем окно в полноэкранный режим
	window.document.documentElement.requestFullscreen();
  }