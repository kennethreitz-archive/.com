CSS With a Hint of DRY
######################

:date: 2009-08-20 02:57
:category: Code


I am a DRY (*Don’t Repeat Yourself*) programmer. I’m not positive,
but I most likely inherited my love for this concept from my
intensive Python immersion. I'm so grateful for it. Anyway, DRY is
an essential stage of any developer's workflow. It drastically
enforces good structure, and significantly increases your logical
skills. As with everything in life, there’s a time and place for
DRY. Object oriented programming is one of those places. ## CSS Is
Not DRY Let it be said: CSS is *not* a programming language. It is
*not* a programmer’s language. It is not supposed to be. It is a
styling markup language. But for those of us who like to take a
more structured and programmatic approach, CSS is far from ideal. I
want my CSS to do math. I want it to be dynamic. So, that's where
fun little libraries come in to play that generate CSS on the fly
based on logic and rules! I implore you to take a look at
`CleverCSS <http://sandbox.pocoo.org/clevercss>`_. The awesome
Python CSS generator. It supports variables, code manipulation,
inheritance, and oh, so much more. I’ll be writing a Django helper
module soon that generates this CSS on the fly. ###See Also: There
is also `SASS <http://sass-lang.com>`_, or
`Syntactically Awesome StyleSheets <http://sass-lang.com>`_. I must
credit it: it seems to be the originator of the concept, has a
significantly cooler name, and is a bit more widely accepted in the
world. Oh, but that’s not written in Python, is it?
