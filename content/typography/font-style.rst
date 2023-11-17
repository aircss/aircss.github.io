Font style
##########


While italics are mainly used to draw attention to certain words or passages, the font
style also plays an important role in differentiating the titles and names of things
such as novels, movies, or vehicle names from other text.


Mnemonics
=========

.. mnemonics:: air/src/typography/font-style.css


Shorthand
=========

It is possible to use the class name ``.i`` instead of ``.fs-italic``.


Examples
========

.. code:: html

  <p class="fs-italic">The quick brown fox ...</p>
  <p class="i">The quick brown fox ...</p>

.. raw:: html

      <p class="f3 fs-italic lh-title mt0 mb6 truncate">
        The quick brown fox jumps over the lazy dog.
      </p>


.. code:: html

  <p class="fs-normal">The quick brown fox ...</p>

.. raw:: html

      <div class="f3 fs-normal lh-title mt0 mb6 truncate">
        The quick brown fox jumps over the lazy dog.
      </div>


Source code
===========

.. include:: ../../air/src/typography/font-style.css
    :code: css
    :start-after: */
