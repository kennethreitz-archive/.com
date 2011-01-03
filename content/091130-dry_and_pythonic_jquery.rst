DRY and Pythonic jQuery?
########################

:date: 2009-11-30 17:16
:category: Code


Apparently, **groovy:spring:java** as **jabs:jquery:javascript**.
As if jQuery wasn't short enough already.

`Jabs <http://github.com/collin/jabs>`_ lets you write this jQuery
code:

::

    jQuery(function() {
      var $ = jQuery;
    
      $("[default_value]")
        .blur(function() {
          var self = $(this);
          if(self.val() === "") {
            self.val(self.attr("default_value"));
          }
        })
        .focus(function() {
          var self = $(this);
          if(self.val === self.attr("default_value")) {
            self.val("");
          }
        })
        .blur(); 
    });

By typing this:

::

    $ [default_value]
      :blur
        if @value === ""
          @value = @default_value
      :focus
        if @value === @default_value
          @value = ""
      .blur

`HAML <http://haml-lang.com/>`_ tactics FTW.
