Line length (measure)
#####################

:slug: measure


Measure or line length is the distance between the left and right edges of a text block.
Overly long lines are a common problem, but they're easy to correct. Shorter lines will
make a big difference in the legibility and professionalism of your layout.


Mnemonics
=========

.. mnemonics:: air/src/typography/measure.css


Examples
========

.. code:: html

    <p class="ll-narrow">lorem ipsum ...</p>

.. raw:: html

    <div class="db tl lh-body ll-narrow fw3 mb6">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Delectus temporibus
        soluta veritatis dolorum rerum vero quibusdam at repellendus qui? Ad aliquam
        nesciunt voluptate aspernatur cumque excepturi necessitatibus neque maxime
        obcaecati!
    </div>


.. code:: html

    <p class="ll-medium">lorem ipsum ...</p>
    <p class="llm">lorem ipsum ...</p>

.. raw:: html

    <div class="db tl lh-body ll-medium fw3 mb6">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Delectus temporibus
        soluta veritatis dolorum rerum vero quibusdam at repellendus qui? Ad aliquam
        nesciunt voluptate aspernatur cumque excepturi necessitatibus neque maxime
        obcaecati!
    </div>


.. code:: html

    <p class="ll-wide">lorem ipsum ...</p>

.. raw:: html

    <div class="db tl lh-body ll-wide fw3 mb6">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Delectus temporibus
        soluta veritatis dolorum rerum vero quibusdam at repellendus qui? Ad aliquam
        nesciunt voluptate aspernatur cumque excepturi necessitatibus neque maxime
        obcaecati!
    </div>


Source code
===========

.. include:: ../../air/src/typography/measure.css
    :code: css
    :start-after: */
