Django ORM for Online Payment Systems?
######################################

:date: 2009-08-21 23:26
:category: Code


I’ve been spending an increasingly large amount of time with some
rapid development frameworks, primarily Django (Python!), Grails
(Groovy / Java), and Symfony (PHP). I’ve been enjoying it. Alot.
Life has never been better.

DRY tactics. Code portability. Who likes to repeat themselves
anyway? It’s a great idea.

My favorite concept to date is the Object Relational Model (ORM).
Database-agnostcisty is fantastic. Not sure what database you want
to use? Worry about it later. A client wants to switch to MySQL
because SQLServer is costing too much? No problem. How much of my
codebase will I have to change? About six charecters. Wow.

So why not take this concept, and apply it elsewhere? I’m currently
doing some work for a startup, and we are having trouble deciding
which online payment service to use/support: PayPal, Amazon
Payments, or Google Checkout.

My solution is to write a webPaySystem module that integrates all
of these payment systems into one single class. But, before I spend
the time to write this, I’d like to extend this question to the
Python / Django community:

Would you find this useful in your web (and business desktop)
applications?

Comment and let me know what you think!
