const sidebar = document.getElementById('sidebar');

if (window.innerWidth >= 768) {
	sidebar.classList.remove('hide');
  } else {
	sidebar.classList.add('hide');
  }

window.addEventListener('resize', function () {
	if (window.innerWidth < 768) {
	  sidebar.classList.add('hide');
	} else {
	  sidebar.classList.remove('hide');
	}
  });
