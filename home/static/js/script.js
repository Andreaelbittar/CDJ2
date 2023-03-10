document.addEventListener('DOMContentLoaded', function() {
    var elemssidenav = document.querySelectorAll('.sidenav');
    var instancessidenav = M.Sidenav.init(elemssidenav);
   });

   $(document).ready(function() {
    $('.link').click(function() {
      $('.link').removeClass('active-link');
      $(this).addClass('active-link');
    });
  });

  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.dropdown-trigger');
    var instances = M.Dropdown.init(elems, options);
  });

  // Or with jQuery

  $('.dropdown-trigger').dropdown();